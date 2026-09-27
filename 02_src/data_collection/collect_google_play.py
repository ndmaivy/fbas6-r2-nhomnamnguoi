"""Collect the canonical raw Google Play review dataset for TCInvest.

This production collector keeps review payloads unchanged and adds only
collection metadata. Collection locale is deliberately kept separate from
review-language detection; language detection belongs in a later processing
phase and is not inferred here.
"""

from __future__ import annotations

import json
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
from google_play_scraper import Sort, reviews


APP_NAME = "TCInvest"
APP_ID = "com.fss.tcbs.mobiletrading"
COLLECTION_DATE = "2026-09-22"

COLLECTION_CONFIGS = [
    {
        "collection_language": "vi",
        "collection_country": "vn",
        "collection_locale": "vi_vn",
    },
    {
        "collection_language": "en",
        "collection_country": "vn",
        "collection_locale": "en_vn",
    },
]

BATCH_SIZE = 200
MAX_BATCHES_PER_LOCALE = 1000
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = (1, 2, 4)
SUCCESS_DELAY_SECONDS = 0.25

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "01_data" / "raw" / "google_play"
OUTPUT_FILE = OUTPUT_DIR / f"{COLLECTION_DATE}_google_play_raw.csv"
SUMMARY_FILE = OUTPUT_DIR / f"{COLLECTION_DATE}_google_play_collection_summary.json"

MINIMUM_RAW_FIELDS = [
    "reviewId",
    "userName",
    "userImage",
    "content",
    "score",
    "thumbsUpCount",
    "reviewCreatedVersion",
    "at",
    "replyContent",
    "repliedAt",
    "appVersion",
]
METADATA_FIELDS = [
    "source",
    "collection_language",
    "collection_country",
    "collection_locale",
    "retrieved_from_locales",
]


def fetch_batch(config: dict[str, str], continuation_token: Any):
    """Fetch one page, retrying transient failures with exponential backoff."""
    locale = config["collection_locale"]
    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return reviews(
                APP_ID,
                lang=config["collection_language"],
                country=config["collection_country"],
                sort=Sort.NEWEST,
                count=BATCH_SIZE,
                continuation_token=continuation_token,
            )
        except Exception as exc:  # library exposes several network/parser errors
            last_error = exc
            print(f"[{locale}] request attempt {attempt}/{MAX_RETRIES} failed: {exc}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS[attempt - 1])

    raise RuntimeError(
        f"request failed after {MAX_RETRIES} attempts: {last_error}"
    ) from last_error


def collect_locale(config: dict[str, str]):
    """Paginate one locale until the public endpoint or a safety rule stops."""
    locale = config["collection_locale"]
    continuation_token = None
    seen_ids: set[str] = set()
    records: list[dict[str, Any]] = []

    for batch_number in range(1, MAX_BATCHES_PER_LOCALE + 1):
        previous_token_fingerprint = repr(continuation_token)
        try:
            batch, next_token = fetch_batch(config, continuation_token)
        except RuntimeError as exc:
            return records, f"unrecoverable_request_failure: {exc}"

        if not batch:
            return records, "empty_batch"

        batch_ids = {
            str(item["reviewId"])
            for item in batch
            if item.get("reviewId") is not None
        }
        new_ids = batch_ids - seen_ids

        for item in batch:
            record = dict(item)
            record.update(
                {
                    "source": "Google Play",
                    "collection_language": config["collection_language"],
                    "collection_country": config["collection_country"],
                    "collection_locale": locale,
                }
            )
            records.append(record)

        print(
            f"[{locale}] batch {batch_number}: {len(batch)} raw, "
            f"{len(new_ids)} new reviewId"
        )

        if not new_ids:
            return records, "batch_produced_no_new_review_ids"
        seen_ids.update(new_ids)

        if next_token is None:
            return records, "continuation_token_none"
        if repr(next_token) == previous_token_fingerprint:
            return records, "continuation_token_unchanged"

        continuation_token = next_token
        time.sleep(SUCCESS_DELAY_SECONDS)

    return records, f"max_safety_guard_reached_{MAX_BATCHES_PER_LOCALE}_batches"


def deduplicate_records(all_records: list[dict[str, Any]]):
    """Deduplicate by reviewId while retaining locale provenance."""
    locales_by_id: dict[str, set[str]] = defaultdict(set)
    for record in all_records:
        review_id = record.get("reviewId")
        if review_id is not None:
            locales_by_id[str(review_id)].add(record["collection_locale"])

    canonical: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for record in all_records:
        review_id = record.get("reviewId")
        if review_id is None:
            canonical.append(dict(record))
            continue

        review_id_string = str(review_id)
        if review_id_string in seen_ids:
            continue
        seen_ids.add(review_id_string)

        kept = dict(record)
        kept["retrieved_from_locales"] = ",".join(
            sorted(locales_by_id[review_id_string])
        )
        canonical.append(kept)

    return canonical, locales_by_id


def count_missing(df: pd.DataFrame, column: str) -> int:
    if column not in df.columns:
        return len(df)
    if column == "content":
        return int((df[column].isna() | df[column].astype(str).str.strip().eq("")).sum())
    return int(df[column].isna().sum())


def integer_distribution(series: pd.Series) -> dict[str, int]:
    return {
        str(int(key) if isinstance(key, float) and key.is_integer() else key): int(value)
        for key, value in series.value_counts(dropna=False).sort_index().items()
        if not pd.isna(key)
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    records_by_locale: dict[str, list[dict[str, Any]]] = {}
    stop_reasons: dict[str, str] = {}
    all_records: list[dict[str, Any]] = []

    for config in COLLECTION_CONFIGS:
        locale = config["collection_locale"]
        print(f"\n=== Collecting {locale} ===")
        locale_records, stop_reason = collect_locale(config)
        records_by_locale[locale] = locale_records
        stop_reasons[locale] = stop_reason
        all_records.extend(locale_records)
        print(f"[{locale}] stopped: {stop_reason}; raw records: {len(locale_records)}")

    canonical_records, locales_by_id = deduplicate_records(all_records)
    cross_locale_duplicates = sum(
        len(locales) > 1 for locales in locales_by_id.values()
    )
    duplicate_review_ids = len(all_records) - len(canonical_records)

    df = pd.DataFrame(canonical_records)
    ordered_columns = MINIMUM_RAW_FIELDS + METADATA_FIELDS
    for column in ordered_columns:
        if column not in df.columns:
            df[column] = pd.NA
    extra_columns = [column for column in df.columns if column not in ordered_columns]
    df = df[ordered_columns + extra_columns]

    dates = pd.to_datetime(df["at"], errors="coerce", utc=True)
    locale_distribution = {
        str(key): int(value)
        for key, value in df["collection_locale"].value_counts().items()
    }
    rating_distribution = integer_distribution(df["score"])

    summary = {
        "app": APP_NAME,
        "package_id": APP_ID,
        "source": "Google Play",
        "collection_date": COLLECTION_DATE,
        "locale_raw_counts": {
            locale: len(records_by_locale.get(locale, []))
            for locale in ("vi_vn", "en_vn")
        },
        "rows_before_dedupe": len(all_records),
        "rows_after_dedupe": len(df),
        "unique_review_ids": int(df["reviewId"].nunique(dropna=True)),
        "duplicate_review_ids": duplicate_review_ids,
        "cross_locale_duplicates": cross_locale_duplicates,
        "earliest_review": dates.min().isoformat() if dates.notna().any() else None,
        "latest_review": dates.max().isoformat() if dates.notna().any() else None,
        "rating_distribution": rating_distribution,
        "missing_content": count_missing(df, "content"),
        "missing_rating": count_missing(df, "score"),
        "missing_date": count_missing(df, "at"),
        "missing_app_version": count_missing(df, "appVersion"),
        "collection_locale_distribution": locale_distribution,
        "detected_language_distribution": None,
        "stop_reason": stop_reasons,
    }

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    SUMMARY_FILE.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("\n==================================================")
    print("GOOGLE PLAY FULL COLLECTION SUMMARY")
    print("==================================================")
    print(f"vi_vn raw retrieved: {summary['locale_raw_counts']['vi_vn']}")
    print(f"en_vn raw retrieved: {summary['locale_raw_counts']['en_vn']}")
    print(f"\nRows before dedupe: {summary['rows_before_dedupe']}")
    print(f"Rows after dedupe: {summary['rows_after_dedupe']}")
    print(f"\nUnique reviewId: {summary['unique_review_ids']}")
    print(f"Duplicate reviewId: {summary['duplicate_review_ids']}")
    print(f"Cross-locale duplicates: {summary['cross_locale_duplicates']}")
    print(f"\nEarliest: {summary['earliest_review']}")
    print(f"Latest: {summary['latest_review']}")
    print("\nRating distribution:")
    for rating in range(1, 6):
        print(f"{rating}: {rating_distribution.get(str(rating), 0)}")
    print(f"\nMissing content: {summary['missing_content']}")
    print(f"Missing rating: {summary['missing_rating']}")
    print(f"Missing date: {summary['missing_date']}")
    print(f"Missing appVersion: {summary['missing_app_version']}")
    print(f"\nCollection locale distribution: {locale_distribution}")
    print("\nStop reason:")
    print(f"vi_vn: {stop_reasons.get('vi_vn')}")
    print(f"en_vn: {stop_reasons.get('en_vn')}")
    print(f"\nCanonical output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
