#!/usr/bin/env python3
"""Create the finalized 24-month TCInvest analysis dataset without re-cleaning."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "01_data/processed/reviews_clean_full.csv"
OUTPUT_PATH = ROOT / "01_data/processed/reviews_analysis_24m.csv"
MONTHLY_PATH = ROOT / "05_outputs/tables/analysis_24m_monthly_counts.csv"
SCOPE_PATH = ROOT / "00_docs/methodology/analysis_scope.md"

START = pd.Timestamp("2024-09-22T00:00:00Z")
END = pd.Timestamp("2026-09-22T23:59:59Z")
WINDOW_LABEL = "2024-09-22_to_2026-09-22"
EXPECTED_ROWS = 3745
EXPECTED_SOURCES = {"Google Play": 3223, "App Store": 522}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def missing(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip().eq("").fillna(True)


def bool_true(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip().str.casefold().eq("true").fillna(False)


def pct(count: int, total: int) -> float:
    return round(100 * count / total, 2) if total else 0.0


def main() -> None:
    input_hash_before = sha256(INPUT_PATH)
    source = pd.read_csv(INPUT_PATH, dtype=str, keep_default_na=False)
    if len(source) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} input rows, found {len(source)}")
    if source["source"].value_counts().to_dict() != EXPECTED_SOURCES:
        raise RuntimeError(f"Unexpected source counts: {source['source'].value_counts().to_dict()}")

    parsed_dates = pd.to_datetime(source["review_date"], utc=True, errors="coerce")
    if parsed_dates.isna().any():
        raise RuntimeError(f"Input contains {int(parsed_dates.isna().sum())} unparseable review_date values")

    in_window = parsed_dates.between(START, END, inclusive="both")
    analysis = source.loc[in_window].copy()
    analysis_dates = parsed_dates.loc[in_window]
    analysis["analysis_window"] = WINDOW_LABEL

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    MONTHLY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SCOPE_PATH.parent.mkdir(parents=True, exist_ok=True)
    analysis.to_csv(OUTPUT_PATH, index=False)

    # Re-read the generated CSV for output-level validation.
    check = pd.read_csv(OUTPUT_PATH, dtype=str, keep_default_na=False)
    check_dates = pd.to_datetime(check["review_date"], utc=True, errors="coerce")
    check_ratings = pd.to_numeric(check["rating"], errors="coerce")
    duplicate_keys = int(check.duplicated(["source", "review_id"], keep=False).sum())
    missing_core = {
        "review_id": int(missing(check["review_id"]).sum()),
        "review_date": int(check_dates.isna().sum()),
        "rating": int(check_ratings.isna().sum()),
        "review_text_raw": int(missing(check["review_text_raw"]).sum()),
    }
    if duplicate_keys:
        raise RuntimeError(f"Generated dataset has {duplicate_keys} records with duplicate keys")
    if any(missing_core.values()):
        raise RuntimeError(f"Generated dataset has missing core fields: {missing_core}")
    if not check_dates.between(START, END, inclusive="both").all():
        raise RuntimeError("Generated dataset contains review dates outside the agreed window")

    # Verify all original columns and values equal the selected source rows.
    original_columns = list(source.columns)
    if not analysis[original_columns].reset_index(drop=True).equals(check[original_columns]):
        raise RuntimeError("An original column/value changed while creating the analysis dataset")

    # Monthly counts include zero-count source-month combinations across the full
    # agreed calendar window, with Combined as a separate series.
    monthly_base = check[["source", "review_id"]].copy()
    monthly_base["month"] = check_dates.dt.tz_localize(None).dt.to_period("M").astype(str)
    month_index = pd.period_range(START.tz_localize(None).to_period("M"), END.tz_localize(None).to_period("M"), freq="M").astype(str)
    monthly_rows: list[dict[str, object]] = []
    for source_name in ["Google Play", "App Store"]:
        counts = monthly_base.loc[monthly_base["source"].eq(source_name), "month"].value_counts().reindex(month_index, fill_value=0)
        monthly_rows.extend({"month": month, "source": source_name, "review_count": int(count)} for month, count in counts.items())
    combined = monthly_base["month"].value_counts().reindex(month_index, fill_value=0)
    monthly_rows.extend({"month": month, "source": "Combined", "review_count": int(count)} for month, count in combined.items())
    monthly = pd.DataFrame(monthly_rows)
    monthly.to_csv(MONTHLY_PATH, index=False)

    source_counts = check["source"].value_counts().reindex(["Google Play", "App Store"], fill_value=0)
    rating_rows = []
    descriptive_rows = []
    for scope in ["Google Play", "App Store", "Combined"]:
        ratings = check_ratings if scope == "Combined" else check_ratings[check["source"].eq(scope)]
        counts = ratings.value_counts().reindex(range(1, 6), fill_value=0)
        for rating, count in counts.items():
            rating_rows.append({"source": scope, "rating": int(rating), "count": int(count), "percentage": pct(int(count), len(ratings))})
        descriptive_rows.append({
            "source": scope,
            "average_rating": round(float(ratings.mean()), 3),
            "median_rating": float(ratings.median()),
        })
    ratings = pd.DataFrame(rating_rows)
    descriptive = pd.DataFrame(descriptive_rows)

    quality = {
        "very_short": int(bool_true(check["is_very_short"]).sum()),
        "exact_duplicate_text": int(bool_true(check["is_exact_duplicate_text"]).sum()),
        "missing_app_version": int(bool_true(check["missing_app_version"]).sum()),
        "suspected_spam": int(bool_true(check["suspected_spam"]).sum()),
    }

    scope_doc = f"""# Analysis Scope

## Main Analysis Window

**22 September 2024 → 22 September 2026**

Filter definition, applied to UTC-parsed `review_date` without changing stored timestamps:

- `review_date >= 2024-09-22 00:00:00+00:00`
- `review_date <= 2026-09-22 23:59:59+00:00`

## Reason for Selecting 24 Months

- Focuses on customer feedback closer to the current product state.
- Retains a sufficiently large sample for analysis.
- Provides better source balance than the full available history.
- Reduces domination by historical Google Play reviews dating back to 2015.
- Is appropriate for identifying current recurring pain points.

## Primary Analysis Dataset

`01_data/processed/reviews_analysis_24m.csv`

- Rows: **{len(check):,}**
- Google Play: **{int(source_counts['Google Play']):,}** ({pct(int(source_counts['Google Play']), len(check)):.2f}%)
- App Store: **{int(source_counts['App Store']):,}** ({pct(int(source_counts['App Store']), len(check)):.2f}%)
- Earliest observed review: **{check_dates.min().isoformat()}**
- Latest observed review: **{check_dates.max().isoformat()}**
- Unique `(source, review_id)` keys: **{check.drop_duplicates(['source', 'review_id']).shape[0]:,}**
- Duplicate key records: **{duplicate_keys}**

The dataset retains every current clean-dataset column and adds `analysis_window={WINDOW_LABEL}`. No review text, date, rating, quality flag, or other existing value is changed. Very short reviews, duplicate text with distinct review IDs, missing app versions, and suspected-spam flags are not removed by this time filter.

Monthly source counts are available in `05_outputs/tables/analysis_24m_monthly_counts.csv`.

## Important Limitations

- Public reviewers are self-selected.
- Results do not represent all TCInvest customers.
- App Store public endpoint coverage is not guaranteed to be complete.
- The **{len(check):,} reviews are review records, not unique customers**.
- The window is an analytical scope decision and does not imply that reviews outside it are invalid.
"""
    SCOPE_PATH.write_text(scope_doc, encoding="utf-8")

    input_hash_after = sha256(INPUT_PATH)
    if input_hash_before != input_hash_after:
        raise RuntimeError("The clean full-history input changed during analysis filtering")

    print("ANALYSIS DATASET 24M RESULT")
    print(f"Input rows: {len(source)}")
    print(f"Output rows: {len(check)}")
    print(f"Source counts: {source_counts.to_dict()}")
    print(f"Source shares: GP={pct(int(source_counts['Google Play']), len(check)):.2f}%, AS={pct(int(source_counts['App Store']), len(check)):.2f}%")
    print(f"Observed range: {check_dates.min().isoformat()} to {check_dates.max().isoformat()}")
    print(f"Unique keys: {check.drop_duplicates(['source', 'review_id']).shape[0]}; duplicate records: {duplicate_keys}")
    print(f"Missing core fields: {missing_core}")
    print(f"Quality flags: {quality}")
    print("Rating distribution:")
    print(ratings.to_string(index=False))
    print("Rating descriptives:")
    print(descriptive.to_string(index=False))
    print(f"Monthly count sums: {monthly.groupby('source')['review_count'].sum().to_dict()}")
    print(f"Input SHA256 unchanged: YES ({input_hash_after})")


if __name__ == "__main__":
    main()
