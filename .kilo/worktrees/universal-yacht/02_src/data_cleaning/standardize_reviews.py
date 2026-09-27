"""Standardize TCInvest raw review datasets without cleaning or filtering.

This script maps the primary App Store and Google Play raw files to a common
schema, validates row-level identity and required fields, and writes interim
CSV files. Review text is copied verbatim. No deduplication, language
detection, sentiment analysis, or content transformation is performed.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]

GOOGLE_PLAY_INPUT = (
    ROOT / "01_data/raw/google_play/2026-09-22_google_play_raw.csv"
)
APP_STORE_INPUT = (
    ROOT / "01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv"
)

GOOGLE_PLAY_OUTPUT = ROOT / "01_data/interim/google_play_standardized.csv"
APP_STORE_OUTPUT = ROOT / "01_data/interim/app_store_standardized.csv"
MERGED_OUTPUT = ROOT / "01_data/interim/reviews_merged_standardized.csv"
LOG_OUTPUT = ROOT / "00_docs/methodology/data_standardization_log.md"

EXPECTED_GOOGLE_PLAY_ROWS = 3_223
EXPECTED_APP_STORE_ROWS = 522
EXPECTED_MERGED_ROWS = 3_745

COMMON_COLUMNS = [
    "review_id",
    "source",
    "review_date",
    "rating",
    "title",
    "review_text_raw",
    "app_version",
    "user_name",
    "developer_reply",
    "developer_reply_date",
    "collection_country",
    "collection_language",
    "collection_locale",
    "storefront",
    "detected_language",
    "language_detection_method",
    "source_endpoint",
    "raw_source_file",
    "google_thumbs_up_count",
    "app_store_vote_sum",
    "app_store_vote_count",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def null_series(index: pd.Index) -> pd.Series:
    return pd.Series(pd.NA, index=index, dtype="object")


def empty_as_null(series: pd.Series) -> pd.Series:
    """Represent absent metadata as null without altering non-empty values."""
    result = series.astype("object").copy()
    return result.mask(result.eq(""), pd.NA)


def to_utc_iso(
    series: pd.Series,
    field_label: str,
) -> tuple[pd.Series, list[dict[str, object]]]:
    """Convert parseable timestamps to UTC ISO-8601 and retain failed rows."""
    raw = series.astype("string")
    missing = raw.isna() | raw.eq("")
    parsed = pd.to_datetime(raw.mask(missing), errors="coerce", utc=True)
    failed = (~missing) & parsed.isna()
    failures = [
        {
            "row_index": int(index),
            "field": field_label,
            "raw_value": raw.loc[index],
        }
        for index in raw.index[failed]
    ]
    standardized = parsed.map(
        lambda value: value.isoformat() if not pd.isna(value) else pd.NA
    )
    return standardized, failures


def numeric_field(series: pd.Series) -> pd.Series:
    """Map numeric source metadata to nullable numbers without dropping rows."""
    return pd.to_numeric(series.mask(series.eq(""), pd.NA), errors="coerce")


def standardize_google_play(
    raw: pd.DataFrame,
) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    review_dates, date_failures = to_utc_iso(raw["at"], "Google Play at")
    reply_dates, reply_date_failures = to_utc_iso(
        raw["repliedAt"], "Google Play repliedAt"
    )

    standardized = pd.DataFrame(index=raw.index)
    standardized["review_id"] = raw["reviewId"].astype("string")
    standardized["source"] = raw["source"]
    standardized["review_date"] = review_dates
    standardized["rating"] = numeric_field(raw["score"])
    standardized["title"] = null_series(raw.index)
    standardized["review_text_raw"] = raw["content"]
    standardized["app_version"] = empty_as_null(raw["reviewCreatedVersion"])
    standardized["user_name"] = empty_as_null(raw["userName"])
    standardized["developer_reply"] = empty_as_null(raw["replyContent"])
    standardized["developer_reply_date"] = reply_dates
    standardized["collection_country"] = empty_as_null(
        raw["collection_country"]
    )
    standardized["collection_language"] = empty_as_null(
        raw["collection_language"]
    )
    standardized["collection_locale"] = empty_as_null(
        raw["collection_locale"]
    )
    standardized["storefront"] = null_series(raw.index)
    standardized["detected_language"] = null_series(raw.index)
    standardized["language_detection_method"] = null_series(raw.index)
    standardized["source_endpoint"] = null_series(raw.index)
    standardized["raw_source_file"] = str(GOOGLE_PLAY_INPUT.relative_to(ROOT))
    standardized["google_thumbs_up_count"] = numeric_field(
        raw["thumbsUpCount"]
    )
    standardized["app_store_vote_sum"] = null_series(raw.index)
    standardized["app_store_vote_count"] = null_series(raw.index)

    return standardized[COMMON_COLUMNS], date_failures + reply_date_failures


def standardize_app_store(
    raw: pd.DataFrame,
) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    review_dates, date_failures = to_utc_iso(
        raw["updated_at"], "App Store updated_at"
    )

    standardized = pd.DataFrame(index=raw.index)
    standardized["review_id"] = raw["review_id"].astype("string")
    standardized["source"] = raw["source"]
    standardized["review_date"] = review_dates
    standardized["rating"] = numeric_field(raw["rating"])
    standardized["title"] = empty_as_null(raw["title"])
    standardized["review_text_raw"] = raw["content"]
    standardized["app_version"] = empty_as_null(raw["app_version"])
    standardized["user_name"] = empty_as_null(raw["user_name"])
    standardized["developer_reply"] = null_series(raw.index)
    standardized["developer_reply_date"] = null_series(raw.index)
    standardized["collection_country"] = null_series(raw.index)
    standardized["collection_language"] = null_series(raw.index)
    standardized["collection_locale"] = null_series(raw.index)
    standardized["storefront"] = empty_as_null(raw["storefront"])
    standardized["detected_language"] = null_series(raw.index)
    standardized["language_detection_method"] = null_series(raw.index)
    standardized["source_endpoint"] = empty_as_null(raw["endpoint_groups"])
    standardized["raw_source_file"] = empty_as_null(raw["raw_source_files"])
    standardized["google_thumbs_up_count"] = null_series(raw.index)
    standardized["app_store_vote_sum"] = numeric_field(raw["vote_sum"])
    standardized["app_store_vote_count"] = numeric_field(raw["vote_count"])

    return standardized[COMMON_COLUMNS], date_failures


def distribution(series: pd.Series) -> dict[str, int]:
    return {
        str(int(key) if isinstance(key, float) and key.is_integer() else key): int(value)
        for key, value in series.value_counts(dropna=False).sort_index().items()
        if not pd.isna(key)
    }


def missing_count(series: pd.Series) -> int:
    textual = series.astype("string")
    return int((series.isna() | textual.str.strip().eq("")).sum())


def validation_summary(df: pd.DataFrame, id_column: str = "review_id") -> dict:
    dates = pd.to_datetime(df["review_date"], errors="coerce", utc=True)
    return {
        "rows": len(df),
        "unique_review_ids": int(df[id_column].nunique(dropna=True)),
        "duplicate_review_id_rows": int(
            df[id_column].duplicated(keep=False).sum()
        ),
        "earliest_review": dates.min().isoformat() if dates.notna().any() else None,
        "latest_review": dates.max().isoformat() if dates.notna().any() else None,
        "rating_distribution": distribution(df["rating"]),
        "missing_review_id": missing_count(df[id_column]),
        "missing_review_date": missing_count(df["review_date"]),
        "missing_rating": missing_count(df["rating"]),
        "missing_review_text_raw": missing_count(df["review_text_raw"]),
    }


def sample_value(series: pd.Series) -> str:
    values = series.loc[~series.isna() & series.astype("string").ne("")]
    if values.empty:
        return "null only"
    value = str(values.iloc[0]).replace("\n", " ↵ ").replace("|", "\\|")
    return value[:117] + "…" if len(value) > 120 else value


def schema_table(raw: pd.DataFrame) -> list[str]:
    lines = ["| Column | pandas dtype | Example value |", "|---|---|---|"]
    for column in raw.columns:
        lines.append(
            f"| `{column}` | `{raw[column].dtype}` | {sample_value(raw[column])} |"
        )
    return lines


def write_log(
    google_raw: pd.DataFrame,
    app_raw: pd.DataFrame,
    google_summary: dict,
    app_summary: dict,
    merged_summary: dict,
    date_failures: list[dict[str, object]],
    input_hashes_before: dict[str, str],
    input_hashes_after: dict[str, str],
) -> None:
    google_both_versions = (
        google_raw["reviewCreatedVersion"].ne("")
        & google_raw["appVersion"].ne("")
    )
    google_version_differences = int(
        (
            google_raw.loc[google_both_versions, "reviewCreatedVersion"]
            != google_raw.loc[google_both_versions, "appVersion"]
        ).sum()
    )

    lines = [
        "# Data Standardization Log",
        "",
        "## Scope",
        "",
        "This step maps the two primary raw review datasets to a common schema. It does not clean text, remove rows, deduplicate by text, detect language, assign sentiment, select a time range, or perform analytical classification.",
        "",
        "## Input Files",
        "",
        f"- Google Play: `{GOOGLE_PLAY_INPUT.relative_to(ROOT)}`",
        f"- App Store primary v2: `{APP_STORE_INPUT.relative_to(ROOT)}`",
        "- The historical 447-row App Store snapshot is not used as a primary input.",
        "",
        "## Output Files",
        "",
        f"- `{GOOGLE_PLAY_OUTPUT.relative_to(ROOT)}`",
        f"- `{APP_STORE_OUTPUT.relative_to(ROOT)}`",
        f"- `{MERGED_OUTPUT.relative_to(ROOT)}`",
        "",
        "## Raw Schema Inspection — Google Play",
        "",
        *schema_table(google_raw),
        "",
        "## Raw Schema Inspection — App Store",
        "",
        *schema_table(app_raw),
        "",
        "## Field Mappings",
        "",
        "| Common field | Google Play raw field | App Store raw field |",
        "|---|---|---|",
        "| `review_id` | `reviewId` | `review_id` |",
        "| `source` | `source` | `source` |",
        "| `review_date` | `at` | `updated_at` |",
        "| `rating` | `score` | `rating` |",
        "| `title` | null (not supplied) | `title` |",
        "| `review_text_raw` | `content` | `content` |",
        "| `app_version` | `reviewCreatedVersion` | `app_version` |",
        "| `user_name` | `userName` | `user_name` |",
        "| `developer_reply` | `replyContent` | null (not supplied) |",
        "| `developer_reply_date` | `repliedAt` | null (not supplied) |",
        "| collection metadata | `collection_country`, `collection_language`, `collection_locale` | null; `storefront` retained separately |",
        "| `detected_language` / method | null | null |",
        "| `source_endpoint` | null (not supplied) | `endpoint_groups` |",
        "| `raw_source_file` | primary raw input path | `raw_source_files` |",
        "| `google_thumbs_up_count` | `thumbsUpCount` | null |",
        "| App Store vote fields | null | `vote_sum`, `vote_count` |",
        "",
        "## Equivalent and Source-Specific Fields",
        "",
        "- Review identity, content, rating, review date, app version, and user name have direct source-specific equivalents.",
        "- Google Play alone supplies developer-reply fields and thumbs-up count.",
        "- App Store alone supplies title and App Store vote sum/count.",
        "- Google Play collection locale is request metadata, not detected review language.",
        "- App Store storefront is retained as storefront metadata and is not copied into language fields.",
        "",
        "## Date Conversion",
        "",
        "- Parseable review timestamps are serialized as ISO-8601 UTC without changing the represented instant.",
        "- Google Play timestamps are timezone-naive in the raw CSV; they are interpreted as UTC to remain consistent with the validated raw collection summary.",
        "- Rows with parse failures would be retained with null standardized dates and logged. No parse failures occurred in this run.",
        f"- Date parse failures: {len(date_failures)}",
        "",
        "## Null Handling",
        "",
        "- Missing source fields become null/empty CSV fields in the common schema.",
        "- Missing values are not imputed.",
        "- `detected_language` and `language_detection_method` are null for every row because language detection has not been run.",
        "- Review text is copied verbatim; no lowercase, whitespace normalization, punctuation removal, translation, accent removal, spam filtering, or short-review filtering is performed.",
        "",
        "## Assumptions and Unmapped Raw Fields",
        "",
        "- Global identity is the pair `(source, review_id)`, not `review_id` alone.",
        f"- Google Play `reviewCreatedVersion` and `appVersion` differ in {google_version_differences} rows where both are present. `reviewCreatedVersion` is mapped to the common `app_version`; raw `appVersion` remains unmapped as a redundant field in this dataset.",
        "- Google Play `userImage` and `retrieved_from_locales` are not part of the requested common schema. `collection_locale` remains available.",
        "- App Store `lang` is not mapped because it is `unknown`/not reliable language ground truth.",
        "- App Store representative `endpoint`, `raw_occurrence_count`, `source_groups`, response-identity flag, and conflict flag are not separate common columns; aggregate `endpoint_groups` and `raw_source_files` are retained.",
        "",
        "## Row Counts and Validation",
        "",
        "| Dataset | Input rows | Output rows | Unique IDs | Earliest UTC | Latest UTC |",
        "|---|---:|---:|---:|---|---|",
        f"| Google Play | {len(google_raw)} | {google_summary['rows']} | {google_summary['unique_review_ids']} | {google_summary['earliest_review']} | {google_summary['latest_review']} |",
        f"| App Store | {len(app_raw)} | {app_summary['rows']} | {app_summary['unique_review_ids']} | {app_summary['earliest_review']} | {app_summary['latest_review']} |",
        f"| Merged | {len(google_raw) + len(app_raw)} | {merged_summary['rows']} | n/a across platforms | {merged_summary['earliest_review']} | {merged_summary['latest_review']} |",
        "",
        f"- Google Play rating distribution: {google_summary['rating_distribution']}",
        f"- App Store rating distribution: {app_summary['rating_distribution']}",
        f"- Merged duplicate `(source, review_id)` rows: {merged_summary['duplicate_source_review_id_rows']}",
        f"- Merged missing review ID/date/rating/text: {merged_summary['missing_review_id']}/{merged_summary['missing_review_date']}/{merged_summary['missing_rating']}/{merged_summary['missing_review_text_raw']}",
        "",
        "## Raw Input Integrity",
        "",
        f"- Google Play SHA256 before: `{input_hashes_before[str(GOOGLE_PLAY_INPUT)]}`",
        f"- Google Play SHA256 after: `{input_hashes_after[str(GOOGLE_PLAY_INPUT)]}`",
        f"- App Store SHA256 before: `{input_hashes_before[str(APP_STORE_INPUT)]}`",
        f"- App Store SHA256 after: `{input_hashes_after[str(APP_STORE_INPUT)]}`",
        f"- Raw inputs unchanged: {input_hashes_before == input_hashes_after}",
    ]
    LOG_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    LOG_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    input_hashes_before = {
        str(GOOGLE_PLAY_INPUT): sha256(GOOGLE_PLAY_INPUT),
        str(APP_STORE_INPUT): sha256(APP_STORE_INPUT),
    }

    # keep_default_na=False protects literal raw strings such as "nan" from
    # being converted into missing values during ingestion.
    google_raw = pd.read_csv(
        GOOGLE_PLAY_INPUT,
        dtype={"reviewId": "string"},
        keep_default_na=False,
    )
    app_raw = pd.read_csv(
        APP_STORE_INPUT,
        dtype={"review_id": "string"},
        keep_default_na=False,
    )

    if len(google_raw) != EXPECTED_GOOGLE_PLAY_ROWS:
        raise RuntimeError(
            f"Google Play input has {len(google_raw)} rows; expected "
            f"{EXPECTED_GOOGLE_PLAY_ROWS}. No output was written."
        )
    if len(app_raw) != EXPECTED_APP_STORE_ROWS:
        raise RuntimeError(
            f"App Store input has {len(app_raw)} rows; expected "
            f"{EXPECTED_APP_STORE_ROWS}. No output was written."
        )

    google_standardized, google_date_failures = standardize_google_play(
        google_raw
    )
    app_standardized, app_date_failures = standardize_app_store(app_raw)
    merged = pd.concat(
        [google_standardized, app_standardized],
        ignore_index=True,
    )

    google_summary = validation_summary(google_standardized)
    app_summary = validation_summary(app_standardized)
    merged_summary = validation_summary(merged)
    merged_summary["duplicate_source_review_id_rows"] = int(
        merged.duplicated(subset=["source", "review_id"], keep=False).sum()
    )
    merged_summary["rows_by_source"] = {
        str(key): int(value)
        for key, value in merged["source"].value_counts().items()
    }

    if google_summary["rows"] != EXPECTED_GOOGLE_PLAY_ROWS:
        raise RuntimeError("Google Play standardized row count changed; stopping.")
    if app_summary["rows"] != EXPECTED_APP_STORE_ROWS:
        raise RuntimeError("App Store standardized row count changed; stopping.")
    if merged_summary["rows"] != EXPECTED_MERGED_ROWS:
        raise RuntimeError("Merged standardized row count changed; stopping.")
    if google_summary["unique_review_ids"] != EXPECTED_GOOGLE_PLAY_ROWS:
        raise RuntimeError("Google Play review IDs are not unique; stopping.")
    if app_summary["unique_review_ids"] != EXPECTED_APP_STORE_ROWS:
        raise RuntimeError("App Store review IDs are not unique; stopping.")
    if merged_summary["duplicate_source_review_id_rows"] != 0:
        raise RuntimeError("Merged (source, review_id) keys are duplicated; stopping.")

    GOOGLE_PLAY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    google_standardized.to_csv(
        GOOGLE_PLAY_OUTPUT,
        index=False,
        encoding="utf-8-sig",
    )
    app_standardized.to_csv(
        APP_STORE_OUTPUT,
        index=False,
        encoding="utf-8-sig",
    )
    merged.to_csv(
        MERGED_OUTPUT,
        index=False,
        encoding="utf-8-sig",
    )

    input_hashes_after = {
        str(GOOGLE_PLAY_INPUT): sha256(GOOGLE_PLAY_INPUT),
        str(APP_STORE_INPUT): sha256(APP_STORE_INPUT),
    }
    if input_hashes_before != input_hashes_after:
        raise RuntimeError("A primary raw input changed during standardization.")

    write_log(
        google_raw=google_raw,
        app_raw=app_raw,
        google_summary=google_summary,
        app_summary=app_summary,
        merged_summary=merged_summary,
        date_failures=google_date_failures + app_date_failures,
        input_hashes_before=input_hashes_before,
        input_hashes_after=input_hashes_after,
    )

    print("=" * 50)
    print("STANDARDIZATION VALIDATION")
    print("=" * 50)
    print(f"Google Play: {google_summary}")
    print(f"App Store: {app_summary}")
    print(f"Merged: {merged_summary}")
    print(f"Date parse failures: {len(google_date_failures + app_date_failures)}")
    print(f"Raw files unchanged: {input_hashes_before == input_hashes_after}")


if __name__ == "__main__":
    main()
