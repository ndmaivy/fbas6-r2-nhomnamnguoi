#!/usr/bin/env python3
"""Create the full-history cleaned TCInvest review dataset.

The script is deliberately conservative: it preserves raw text, keeps short and
duplicate-text reviews, and rejects only records that fail explicit core-field
validity rules. It does not filter by analysis time range.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "01_data/interim/reviews_merged_standardized.csv"
SOURCE_STANDARDIZED_PATHS = [
    ROOT / "01_data/interim/google_play_standardized.csv",
    ROOT / "01_data/interim/app_store_standardized.csv",
]
RAW_PATHS = [
    ROOT / "01_data/raw/google_play/2026-09-22_google_play_raw.csv",
    ROOT / "01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv",
]
CLEAN_PATH = ROOT / "01_data/processed/reviews_clean_full.csv"
REJECTED_PATH = ROOT / "01_data/processed/reviews_rejected.csv"
FLAGS_SUMMARY_PATH = ROOT / "05_outputs/tables/reviews_quality_flags_summary.csv"
LOG_PATH = ROOT / "00_docs/methodology/data_cleaning_log.md"

EXPECTED_ROWS = 3745
EXPECTED_SOURCE_COUNTS = {"Google Play": 3223, "App Store": 522}
CORE_RATINGS = {1.0, 2.0, 3.0, 4.0, 5.0}
QUALITY_COLUMNS = [
    "review_text_clean",
    "review_char_length",
    "review_word_count",
    "is_very_short",
    "is_exact_duplicate_text",
    "exact_duplicate_group_id",
    "missing_app_version",
    "suspected_spam",
    "is_valid_for_analysis",
    "removal_reason",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_text(value: str) -> str:
    """Apply only the approved display/analysis-safe whitespace operations."""
    normalized_line_breaks = value.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", normalized_line_breaks).strip()


def word_count(value: str) -> int:
    return len(re.findall(r"\S+", value))


def duplicate_group_id(value: str) -> str:
    return "exact_" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def percentage(count: int, denominator: int) -> float:
    return round(100 * count / denominator, 2) if denominator else 0.0


def iso(value: pd.Timestamp) -> str:
    return value.isoformat() if pd.notna(value) else ""


def main() -> None:
    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    FLAGS_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    protected_paths = [INPUT_PATH, *SOURCE_STANDARDIZED_PATHS, *RAW_PATHS]
    hashes_before = {str(path.relative_to(ROOT)): sha256_file(path) for path in protected_paths}

    # Reading all fields as strings prevents pandas from converting literal review
    # text such as "NA" into a missing value. Empty CSV fields remain empty strings.
    source = pd.read_csv(INPUT_PATH, dtype=str, keep_default_na=False)
    if len(source) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} input rows, found {len(source)}")
    actual_source_counts = source["source"].value_counts(dropna=False).to_dict()
    if actual_source_counts != EXPECTED_SOURCE_COUNTS:
        raise RuntimeError(f"Unexpected source counts: {actual_source_counts}")
    if source["source"].str.strip().eq("").any():
        raise RuntimeError("Missing source value prevents construction of the global review key")

    duplicate_key_mask = source.duplicated(["source", "review_id"], keep=False)
    if duplicate_key_mask.any():
        examples = source.loc[duplicate_key_mask, ["source", "review_id"]].head(10).to_dict("records")
        raise RuntimeError(f"Unexpected duplicate (source, review_id) keys; no rows written. Examples: {examples}")

    work = source.copy()
    parsed_dates = pd.to_datetime(work["review_date"], utc=True, errors="coerce")
    parsed_ratings = pd.to_numeric(work["rating"], errors="coerce")

    missing_id = work["review_id"].str.strip().eq("")
    invalid_date = parsed_dates.isna()
    invalid_rating = parsed_ratings.isna() | ~parsed_ratings.isin(CORE_RATINGS)
    empty_text = work["review_text_raw"].str.strip().eq("")

    # No deterministic confirmed-spam removal rule is justified for this dataset.
    # Suspicion alone must not remove a review, so every record defaults to False.
    confirmed_invalid_spam = pd.Series(False, index=work.index)
    work["suspected_spam"] = False

    reasons: list[str] = []
    for idx in work.index:
        row_reasons = []
        if missing_id.at[idx]:
            row_reasons.append("missing_review_id")
        if invalid_date.at[idx]:
            row_reasons.append("invalid_or_missing_review_date")
        if invalid_rating.at[idx]:
            row_reasons.append("invalid_or_missing_rating")
        if empty_text.at[idx]:
            row_reasons.append("empty_or_whitespace_review_text")
        if confirmed_invalid_spam.at[idx]:
            row_reasons.append("confirmed_invalid_spam")
        reasons.append("; ".join(row_reasons))

    work["removal_reason"] = reasons
    work["is_valid_for_analysis"] = work["removal_reason"].eq("")

    # Preserve review_text_raw byte-for-byte as parsed from the standardized CSV.
    work["review_text_clean"] = work["review_text_raw"].map(clean_text)
    work["review_char_length"] = work["review_text_clean"].str.len()
    work["review_word_count"] = work["review_text_clean"].map(word_count)
    work["is_very_short"] = work["review_char_length"].le(10)
    work["missing_app_version"] = work["app_version"].str.strip().eq("")

    exact_counts = work["review_text_raw"].value_counts(dropna=False)
    duplicate_text_values = set(exact_counts[exact_counts > 1].index)
    work["is_exact_duplicate_text"] = work["review_text_raw"].isin(duplicate_text_values)
    work["exact_duplicate_group_id"] = ""
    duplicate_mask = work["is_exact_duplicate_text"]
    work.loc[duplicate_mask, "exact_duplicate_group_id"] = work.loc[
        duplicate_mask, "review_text_raw"
    ].map(duplicate_group_id)

    # Quality columns are appended without altering standardized columns.
    output_columns = list(source.columns) + QUALITY_COLUMNS
    clean = work.loc[work["is_valid_for_analysis"], output_columns].copy()
    rejected = work.loc[
        ~work["is_valid_for_analysis"],
        ["source", "review_id", "review_date", "rating", "review_text_raw", "removal_reason"],
    ].copy()

    clean.to_csv(CLEAN_PATH, index=False)
    rejected.to_csv(REJECTED_PATH, index=False)

    flag_definitions = [
        ("very_short", "is_very_short"),
        ("exact_duplicate_text", "is_exact_duplicate_text"),
        ("missing_app_version", "missing_app_version"),
        ("suspected_spam", "suspected_spam"),
        ("invalid_rejected", None),
    ]
    summary_rows: list[dict[str, object]] = []
    for scope in ["Total", "Google Play", "App Store"]:
        scoped_all = work if scope == "Total" else work[work["source"].eq(scope)]
        scoped_rejected = rejected if scope == "Total" else rejected[rejected["source"].eq(scope)]
        denominator = len(scoped_all)
        for flag_name, column in flag_definitions:
            count = len(scoped_rejected) if column is None else int(scoped_all[column].sum())
            summary_rows.append({
                "quality_flag": flag_name,
                "source": scope,
                "count": count,
                "denominator": denominator,
                "percentage": percentage(count, denominator),
                "treatment": "rejected" if flag_name == "invalid_rejected" else "retained unless independently invalid",
            })
    flags_summary = pd.DataFrame(summary_rows)
    flags_summary.to_csv(FLAGS_SUMMARY_PATH, index=False)

    clean_dates = pd.to_datetime(clean["review_date"], utc=True, errors="coerce")
    clean_ratings = pd.to_numeric(clean["rating"], errors="coerce")
    clean_source_counts = clean["source"].value_counts().reindex(["Google Play", "App Store"], fill_value=0)
    rating_distribution = clean_ratings.value_counts().sort_index()
    rating_lines = "\n".join(f"- {int(rating)} star: {int(count):,}" for rating, count in rating_distribution.items())

    removed_counts = {
        "missing_review_id": int(missing_id.sum()),
        "invalid_or_missing_review_date": int(invalid_date.sum()),
        "invalid_or_missing_rating": int(invalid_rating.sum()),
        "empty_or_whitespace_review_text": int(empty_text.sum()),
        "confirmed_invalid_spam": int(confirmed_invalid_spam.sum()),
    }
    exact_group_count = int((exact_counts > 1).sum())
    exact_record_count = int(work["is_exact_duplicate_text"].sum())
    timezone_note = (
        "All retained dates parse consistently to UTC."
        if clean_dates.notna().all()
        else "Some retained dates failed UTC parsing; investigate before analysis."
    )

    log = f"""# Data Cleaning Log

## Input Dataset

- File: `01_data/interim/reviews_merged_standardized.csv`
- Rows: {len(source):,}
- Google Play: {actual_source_counts.get('Google Play', 0):,}
- App Store: {actual_source_counts.get('App Store', 0):,}
- Duplicate `(source, review_id)` keys: 0

## Cleaning Rules

A record is rejected only when at least one reproducible core validity rule fails:

1. `review_id` is missing or whitespace-only.
2. `review_date` is missing or cannot be parsed as a datetime.
3. `rating` cannot be parsed or is not one of 1, 2, 3, 4, or 5.
4. `review_text_raw` is missing, empty, or whitespace-only.
5. A deterministic rule confirms invalid/spam content. No such rule was justified or applied in this run.

Duplicate keys cause the script to stop rather than choose a record automatically. No time-range filter is applied. Ratings, dates, app versions, collection locales, language fields, and review polarity are not used to remove otherwise valid records.

## Records Removed

- Missing review ID: {removed_counts['missing_review_id']:,}
- Invalid/missing date: {removed_counts['invalid_or_missing_review_date']:,}
- Invalid/missing rating: {removed_counts['invalid_or_missing_rating']:,}
- Empty/whitespace-only text: {removed_counts['empty_or_whitespace_review_text']:,}
- Confirmed invalid/spam: {removed_counts['confirmed_invalid_spam']:,}
- Total rejected: {len(rejected):,}

## Records Retained Intentionally

- Very short reviews (`review_char_length <= 10`): {int(clean['is_very_short'].sum()):,}
- Exact duplicate-text records with distinct review keys: {int(clean['is_exact_duplicate_text'].sum()):,} records across {exact_group_count:,} groups
- Missing `app_version`: {int(clean['missing_app_version'].sum()):,}
- Missing `detected_language`: {int(clean['detected_language'].str.strip().eq('').sum()):,}

These records remain valid. Short or identical wording does not establish that a review or user is duplicated.

## Text Cleaning

`review_text_raw` is preserved unchanged. `review_text_clean` is produced only by:

1. converting CRLF/CR line endings to LF;
2. trimming leading and trailing whitespace;
3. collapsing consecutive whitespace, including line breaks, to one ordinary space.

Vietnamese diacritics, emoji, punctuation, spelling, casing, and wording are preserved. No translation, stemming, lemmatization, stopword removal, or paraphrasing is performed.

## Quality Flags

- `review_char_length`: Unicode character count of `review_text_clean`.
- `review_word_count`: count of non-whitespace token-like sequences.
- `is_very_short`: `True` when cleaned text contains at most 10 characters.
- `is_exact_duplicate_text`: `True` when the exact `review_text_raw` occurs more than once across the full dataset.
- `exact_duplicate_group_id`: stable SHA-256-derived identifier for the exact raw text; null/empty for non-duplicates.
- `missing_app_version`: `True` when `app_version` is empty.
- `suspected_spam`: defaults to `False`; no deterministic suspicion rule was applied.
- `is_valid_for_analysis`: `True` only when all core validity rules pass.
- `removal_reason`: semicolon-separated failed rules; null/empty for retained records.

## Output Dataset

- Clean file: `01_data/processed/reviews_clean_full.csv`
- Rejected file: `01_data/processed/reviews_rejected.csv`
- Clean rows: {len(clean):,}
- Google Play: {int(clean_source_counts['Google Play']):,}
- App Store: {int(clean_source_counts['App Store']):,}
- Date range: {iso(clean_dates.min())} to {iso(clean_dates.max())}
- Timezone validation: {timezone_note}
- Rating distribution:
{rating_lines}

## Limitations

- Duplicate content does not imply a duplicate person or review; distinct `(source, review_id)` keys are retained.
- Very short reviews can be valid but may provide insufficient context for later pain-point classification.
- Missing app versions are retained and not imputed.
- Actual review language has not been detected; `collection_locale` is not substituted for `detected_language`.
- `suspected_spam=False` means no deterministic flag rule fired, not that content was manually verified as non-spam.
- This is the full available history and does not represent a selected analysis time range.
"""
    LOG_PATH.write_text(log, encoding="utf-8")

    # Re-read outputs and verify required invariants.
    clean_check = pd.read_csv(CLEAN_PATH, dtype=str, keep_default_na=False)
    rejected_check = pd.read_csv(REJECTED_PATH, dtype=str, keep_default_na=False)
    if len(clean_check) + len(rejected_check) != len(source):
        raise RuntimeError("Clean plus rejected row counts do not equal input row count")
    if clean_check.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Duplicate (source, review_id) key found after cleaning")
    if clean_check["review_id"].str.strip().eq("").any():
        raise RuntimeError("Missing review_id found after cleaning")
    if pd.to_datetime(clean_check["review_date"], utc=True, errors="coerce").isna().any():
        raise RuntimeError("Invalid review_date found after cleaning")
    check_rating = pd.to_numeric(clean_check["rating"], errors="coerce")
    if (~check_rating.isin(CORE_RATINGS)).any():
        raise RuntimeError("Invalid rating found after cleaning")
    if clean_check["review_text_raw"].str.strip().eq("").any():
        raise RuntimeError("Empty review_text_raw found after cleaning")
    if clean_check["review_text_clean"].str.strip().eq("").any():
        raise RuntimeError("Empty review_text_clean found after cleaning")
    # Every raw-text value must match its input row under the global key.
    integrity = source[["source", "review_id", "review_text_raw"]].merge(
        clean_check[["source", "review_id", "review_text_raw"]],
        on=["source", "review_id"], how="inner", suffixes=("_input", "_output"), validate="one_to_one"
    )
    if not integrity["review_text_raw_input"].eq(integrity["review_text_raw_output"]).all():
        raise RuntimeError("review_text_raw changed during cleaning")

    hashes_after = {str(path.relative_to(ROOT)): sha256_file(path) for path in protected_paths}
    if hashes_before != hashes_after:
        raise RuntimeError("A standardized or raw input changed during cleaning")

    print("CLEANING RESULT")
    print(f"Input rows: {len(source)}")
    print(f"Clean rows: {len(clean)}")
    print(f"Rejected rows: {len(rejected)}")
    print(f"Google Play retained: {int(clean_source_counts['Google Play'])}")
    print(f"App Store retained: {int(clean_source_counts['App Store'])}")
    print(f"Duplicate keys after cleaning: {int(clean.duplicated(['source', 'review_id'], keep=False).sum())}")
    print(f"Very short retained: {int(clean['is_very_short'].sum())}")
    print(f"Exact duplicate text retained: {int(clean['is_exact_duplicate_text'].sum())} records / {exact_group_count} groups")
    print(f"Missing app_version retained: {int(clean['missing_app_version'].sum())}")
    print(f"Suspected spam retained: {int(clean['suspected_spam'].sum())}")
    print(f"Clean date range: {iso(clean_dates.min())} to {iso(clean_dates.max())}")
    print("INPUT_HASHES_UNCHANGED: YES")
    for path, digest in hashes_after.items():
        print(f"{digest}  {path}")


if __name__ == "__main__":
    main()
