# Analysis Scope

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

- Rows: **736**
- Google Play: **403** (54.76%)
- App Store: **333** (45.24%)
- Earliest observed review: **2024-09-22T02:23:34+00:00**
- Latest observed review: **2026-09-21T12:13:27+00:00**
- Unique `(source, review_id)` keys: **736**
- Duplicate key records: **0**

The dataset retains every current clean-dataset column and adds `analysis_window=2024-09-22_to_2026-09-22`. No review text, date, rating, quality flag, or other existing value is changed. Very short reviews, duplicate text with distinct review IDs, missing app versions, and suspected-spam flags are not removed by this time filter.

Monthly source counts are available in `05_outputs/tables/analysis_24m_monthly_counts.csv`.

## Important Limitations

- Public reviewers are self-selected.
- Results do not represent all TCInvest customers.
- App Store public endpoint coverage is not guaranteed to be complete.
- The **736 reviews are review records, not unique customers**.
- The window is an analytical scope decision and does not imply that reviews outside it are invalid.
