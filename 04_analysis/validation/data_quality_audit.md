# Data Quality Audit

## Dataset Overview

This is a read-only audit of the standardized TCInvest review data. It does not clean, remove, impute, classify, or modify records.

| Source | Rows | Unique review IDs | Earliest | Latest |
| --- | --- | --- | --- | --- |
| Google Play | 3223 | 3223 | 2015-08-13T11:10:30+00:00 | 2026-09-21T12:13:27+00:00 |
| App Store | 522 | 522 | 2023-04-14T03:22:33+00:00 | 2026-09-14T07:44:28+00:00 |

- Merged rows: **3,745**
- Unique `(source, review_id)` keys: **3,745**
- Duplicate `(source, review_id)` records involved: **0**
- Merged columns: **21 standardized fields** (temporary audit columns excluded)

## Missingness

| source | Field | count | percentage | classification |
| --- | --- | --- | --- | --- |
| Google Play | review_id | 0 | 0.00 | complete |
| Google Play | review_date | 0 | 0.00 | complete |
| Google Play | rating | 0 | 0.00 | complete |
| Google Play | review_text_raw | 0 | 0.00 | complete |
| Google Play | title | 3223 | 100.00 | source-unavailable |
| Google Play | app_version | 459 | 14.24 | data-quality limitation |
| Google Play | developer_reply | 2111 | 65.50 | natural/source-specific missingness |
| Google Play | collection_country | 0 | 0.00 | complete |
| Google Play | collection_language | 0 | 0.00 | complete |
| Google Play | collection_locale | 0 | 0.00 | complete |
| Google Play | storefront | 3223 | 100.00 | natural/source-specific missingness |
| Google Play | detected_language | 3223 | 100.00 | methodological limitation |
| App Store | review_id | 0 | 0.00 | complete |
| App Store | review_date | 0 | 0.00 | complete |
| App Store | rating | 0 | 0.00 | complete |
| App Store | review_text_raw | 0 | 0.00 | complete |
| App Store | title | 0 | 0.00 | complete |
| App Store | app_version | 0 | 0.00 | data-quality limitation |
| App Store | developer_reply | 522 | 100.00 | source-unavailable |
| App Store | collection_country | 522 | 100.00 | source-unavailable |
| App Store | collection_language | 522 | 100.00 | source-unavailable |
| App Store | collection_locale | 522 | 100.00 | source-unavailable |
| App Store | storefront | 0 | 0.00 | complete |
| App Store | detected_language | 522 | 100.00 | methodological limitation |

Missing title on Google Play and missing developer-reply/collection-locale fields on App Store reflect source availability, not malformed rows. Missing `detected_language` is a methodological gap: collection locale and storefront must not be treated as actual review language.

## Rating Quality

- Rating minimum: **1**; maximum: **5**.
- Ratings outside 1–5: **0**.

| rating | App Store | Google Play | Total |
| --- | --- | --- | --- |
| 1 | 217 | 1799 | 2016 |
| 2 | 31 | 205 | 236 |
| 3 | 25 | 150 | 175 |
| 4 | 17 | 134 | 151 |
| 5 | 232 | 935 | 1167 |

## Text Quality

Length metrics are descriptive only. Token-like length counts whitespace-separated non-empty sequences; it is not linguistic tokenization.

| source | records | characters_min | characters_p25 | characters_median | characters_mean | characters_p75 | characters_p90 | characters_p95 | characters_max | token_like_min | token_like_p25 | token_like_median | token_like_mean | token_like_p75 | token_like_p90 | token_like_p95 | token_like_max | empty_or_missing | whitespace_only | characters_le_2 | characters_le_5 | characters_le_10 | characters_le_20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total | 3745 | 1.00 | 23.00 | 47.00 | 74.37 | 97.00 | 170.00 | 232.00 | 739.00 | 1.00 | 5.00 | 11.00 | 16.61 | 22.00 | 38.00 | 52.00 | 165.00 | 0 | 0 | 112 | 264 | 533 | 855 |
| Google Play | 3223 | 1.00 | 22.00 | 46.00 | 74.33 | 97.00 | 171.00 | 233.80 | 739.00 | 1.00 | 5.00 | 11.00 | 16.61 | 22.00 | 38.00 | 51.90 | 165.00 | 0 | 0 | 104 | 238 | 476 | 759 |
| App Store | 522 | 1.00 | 28.00 | 49.00 | 74.60 | 98.00 | 162.90 | 220.95 | 570.00 | 1.00 | 5.00 | 11.00 | 16.56 | 22.00 | 36.00 | 51.95 | 129.00 | 0 | 0 | 8 | 26 | 57 | 96 |

Short reviews are retained. They may be valid customer voice but contain less context for downstream analysis.

## Duplicate Text

| scope | groups | records_involved |
| --- | --- | --- |
| Google Play | 63 | 378 |
| App Store | 8 | 22 |
| All sources | 69 | 417 |

- Exact-text groups appearing in both sources: **19**, involving **248 records**.
- Whitespace-only normalized duplicate groups with more than one exact serialization: **0**.
- Exact same text is not evidence of the same user or invalidity; no review was removed.

Examples:

| source_scope | representative_text | record_count | unique_review_ids |
| --- | --- | --- | --- |
| App Store, Google Play | Ok | 69 | 69 |
| App Store, Google Play | Tốt | 41 | 41 |
| App Store, Google Play | Good | 39 | 39 |
| App Store, Google Play | Quá tệ | 27 | 27 |
| App Store, Google Play | Tệ | 19 | 19 |
| Google Play | ok | 14 | 14 |
| App Store, Google Play | 105CTOIYEUVN | 14 | 14 |
| Google Play | Rất tốt | 12 | 12 |
| Google Play | Tuyệt vời | 11 | 11 |
| Google Play | "105CTOIYEUVN tôi thích bảng giá" | 7 | 7 |

## App Version Coverage

| source | available | missing | coverage_pct |
| --- | --- | --- | --- |
| Google Play | 2764 | 459 | 85.76 |
| App Store | 522 | 0 | 100.00 |

Top versions and their observed review-date ranges:

| source | app_version | reviews | earliest | latest |
| --- | --- | --- | --- | --- |
| Google Play | 3.1.1 | 760 | 2021-07-30T13:45:13+00:00 | 2023-12-16T10:53:10+00:00 |
| Google Play | 2.8.1 | 253 | 2020-11-12T17:28:51+00:00 | 2023-12-20T20:31:47+00:00 |
| Google Play | 3.0 | 142 | 2021-05-03T08:06:37+00:00 | 2023-12-18T12:32:14+00:00 |
| Google Play | 5.2.1 | 135 | 2023-11-17T13:16:43+00:00 | 2026-04-29T09:50:43+00:00 |
| Google Play | 2.6.3 | 130 | 2020-06-05T16:44:23+00:00 | 2024-03-11T15:24:20+00:00 |
| Google Play | 5.4.1 | 114 | 2024-02-29T15:26:17+00:00 | 2024-04-01T09:03:13+00:00 |
| Google Play | 5.1.3 | 90 | 2023-09-03T18:08:45+00:00 | 2025-02-02T18:47:35+00:00 |
| Google Play | 3.3.5 | 87 | 2022-10-26T10:39:20+00:00 | 2024-07-10T03:57:41+00:00 |
| Google Play | 5.0.1 | 86 | 2023-04-11T09:45:08+00:00 | 2025-12-22T15:43:44+00:00 |
| Google Play | 2.6.1 | 70 | 2020-03-12T09:58:43+00:00 | 2021-08-24T08:30:52+00:00 |
| App Store | 5.7 | 192 | 2024-09-10T07:01:09+00:00 | 2024-09-29T14:19:44+00:00 |
| App Store | 5.9 | 69 | 2025-03-27T22:42:52+00:00 | 2025-07-04T05:01:01+00:00 |
| App Store | 6.4.3 | 44 | 2026-03-17T07:15:18+00:00 | 2026-05-11T07:18:29+00:00 |
| App Store | 6.1 | 33 | 2025-09-02T14:38:41+00:00 | 2025-11-18T05:22:54+00:00 |
| App Store | 6.3 | 26 | 2025-12-20T11:10:48+00:00 | 2026-01-15T01:36:41+00:00 |
| App Store | 6.4.4 | 25 | 2026-06-04T06:40:04+00:00 | 2026-08-25T04:00:51+00:00 |
| App Store | 6.4.1 | 20 | 2026-01-30T05:51:04+00:00 | 2026-03-01T01:58:26+00:00 |
| App Store | 5.8.2 | 20 | 2024-10-23T03:37:04+00:00 | 2025-01-10T07:05:02+00:00 |
| App Store | 5.8.5 | 17 | 2025-02-12T10:04:36+00:00 | 2025-03-27T07:58:51+00:00 |
| App Store | 6.0 | 14 | 2025-07-14T06:07:33+00:00 | 2025-08-05T00:42:38+00:00 |

No version was imputed. Google Play missing-version count is **459**.

## Developer Reply Coverage

| source | field_availability | reviews_with_reply | reply_pct |
| --- | --- | --- | --- |
| Google Play | available in source schema | 1112 | 34.50 |
| App Store | unavailable in saved source evidence | 0 | 0.00 |

App Store reply data are unavailable in the saved standardized source; that absence is not treated as a row-level quality failure.

## Temporal Coverage

Yearly review counts:

| year | App Store | Google Play | Total |
| --- | --- | --- | --- |
| 2015 | 0 | 4 | 4 |
| 2016 | 0 | 3 | 3 |
| 2017 | 0 | 3 | 3 |
| 2018 | 0 | 14 | 14 |
| 2019 | 0 | 45 | 45 |
| 2020 | 0 | 260 | 260 |
| 2021 | 0 | 1188 | 1188 |
| 2022 | 0 | 345 | 345 |
| 2023 | 4 | 527 | 531 |
| 2024 | 221 | 477 | 698 |
| 2025 | 166 | 209 | 375 |
| 2026 | 131 | 148 | 279 |

Monthly volume, monthly average rating, low-rating counts, and five-star counts are provided in `monthly_review_volume.csv`. Monthly patterns are descriptive and do not establish causes.

## Source Imbalance

| option | total_reviews | google_play_share_pct | app_store_share_pct | absolute_share_gap_pp |
| --- | --- | --- | --- | --- |
| Full available history | 3745 | 86.06 | 13.94 | 72.12 |
| Cross-platform overlap | 1801 | 71.02 | 28.98 | 42.04 |
| Last 24 months | 736 | 54.76 | 45.24 | 9.52 |
| Last 18 months | 581 | 53.01 | 46.99 | 6.02 |
| Last 12 months | 366 | 54.10 | 45.90 | 8.20 |
| Last 6 months | 166 | 58.43 | 41.57 | 16.86 |

Among these options, **Last 18 months** has the lowest absolute source-share gap, while **Full available history** has the highest. This does not imply a weighting decision.

## Recent Time Windows

Windows are inclusive and anchored to 22 September 2026.

| option | start_date | end_date | total_reviews | google_play_reviews | app_store_reviews | google_play_share_pct | app_store_share_pct | rating_1 | rating_2 | rating_3 | rating_4 | rating_5 | average_rating | median_rating | low_rating_1_2_count | low_rating_1_2_pct | earliest_actual_review | latest_actual_review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last 24 months | 2024-09-22 | 2026-09-22 | 736 | 403 | 333 | 54.76 | 45.24 | 474 | 75 | 45 | 23 | 119 | 1.97 | 1.00 | 549 | 74.59 | 2024-09-22T02:23:34+00:00 | 2026-09-21T12:13:27+00:00 |
| Last 18 months | 2025-03-22 | 2026-09-22 | 581 | 308 | 273 | 53.01 | 46.99 | 376 | 58 | 38 | 18 | 91 | 1.95 | 1.00 | 434 | 74.70 | 2025-03-23T10:02:50+00:00 | 2026-09-21T12:13:27+00:00 |
| Last 12 months | 2025-09-22 | 2026-09-22 | 366 | 198 | 168 | 54.10 | 45.90 | 260 | 36 | 20 | 12 | 38 | 1.72 | 1.00 | 296 | 80.87 | 2025-09-22T05:24:56+00:00 | 2026-09-21T12:13:27+00:00 |
| Last 6 months | 2026-03-22 | 2026-09-22 | 166 | 97 | 69 | 58.43 | 41.57 | 114 | 18 | 7 | 5 | 22 | 1.81 | 1.00 | 132 | 79.52 | 2026-03-23T10:50:55+00:00 | 2026-09-21T12:13:27+00:00 |

## Cross-platform Coverage

- Actual overlap: **2023-04-14T03:22:33+00:00 to 2026-09-14T07:44:28+00:00**.
- Reviews in overlap: **1,801** — Google Play **1,279**, App Store **522**.
- Google Play before App Store coverage: **1,939** reviews (2015-08-13T11:10:30+00:00 to 2023-04-12T10:18:10+00:00).
- Google Play after latest App Store review: **5** reviews (2026-09-14T08:56:29+00:00 to 2026-09-21T12:13:27+00:00).

Rating distribution inside the overlap:

| source | rating | count |
| --- | --- | --- |
| App Store | 1 | 217 |
| App Store | 2 | 31 |
| App Store | 3 | 25 |
| App Store | 4 | 17 |
| App Store | 5 | 232 |
| Google Play | 1 | 472 |
| Google Play | 2 | 82 |
| Google Play | 3 | 45 |
| Google Play | 4 | 37 |
| Google Play | 5 | 643 |

Cross-platform comparisons are not possible in the Google-Play-only periods without changing the population definition.

## Potential Spikes

Rule: for each source independently, a month is flagged when its review count is greater than `Q3 + 1.5 × IQR`, calculated over all calendar months in that source's observed coverage (including zero-review months).

Thresholds:

| source | q1 | q3 | iqr | threshold |
| --- | --- | --- | --- | --- |
| Google Play | 1.00 | 26.00 | 25.00 | 63.50 |
| App Store | 0.00 | 13.00 | 13.00 | 32.50 |

Flagged months:

| month | source | review_count | rating_1 | rating_2 | rating_3 | rating_4 | rating_5 | low_rating_share_pct | threshold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-03 | Google Play | 179 | 148 | 7 | 2 | 4 | 18 | 86.59 | 63.50 |
| 2021-06 | Google Play | 73 | 49 | 4 | 5 | 4 | 11 | 72.60 | 63.50 |
| 2021-11 | Google Play | 550 | 504 | 19 | 10 | 2 | 15 | 95.09 | 63.50 |
| 2021-12 | Google Play | 118 | 93 | 6 | 2 | 3 | 14 | 83.90 | 63.50 |
| 2023-08 | Google Play | 76 | 25 | 2 | 2 | 2 | 45 | 35.53 | 63.50 |
| 2023-10 | Google Play | 67 | 9 | 3 | 1 | 0 | 54 | 17.91 | 63.50 |
| 2023-12 | Google Play | 127 | 22 | 1 | 1 | 2 | 101 | 18.11 | 63.50 |
| 2024-03 | Google Play | 155 | 29 | 5 | 0 | 5 | 116 | 21.94 | 63.50 |
| 2024-08 | Google Play | 97 | 9 | 4 | 1 | 1 | 82 | 13.40 | 63.50 |
| 2024-09 | Google Play | 92 | 8 | 1 | 1 | 4 | 78 | 9.78 | 63.50 |
| 2024-09 | App Store | 194 | 5 | 1 | 1 | 6 | 181 | 3.09 | 32.50 |

These flags are investigation prompts only; no causal explanation is inferred.

## Data Quality Issues

| issue | affected_source | affected_rows | percentage | issue_type | severity_for_analysis | recommended_handling | needs_manual_check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Missing app_version | Google Play | 459 | 14.24 | data limitation | medium | Keep null; stratify version analyses by known-version coverage. | No |
| Very short reviews (<=10 characters) | Both | 533 | 14.23 | natural data characteristic | low | Retain; review manually and treat as low-context text. | Yes |
| Exact duplicate review text | Both | 417 | 11.13 | natural/ambiguous duplication | medium | Retain distinct review IDs; inspect groups before text-level modeling. | Yes |
| Missing title | Google Play | 3223 | 100.00 | source-unavailable field | none | Represent as null; do not treat as a quality failure. | No |
| Detected language unavailable | Both | 3745 | 100.00 | methodological limitation | medium | Run language detection later; do not substitute collection locale. | No |
| Developer reply unavailable | App Store | 522 | 100.00 | source-unavailable field | low | Report platform availability separately. | No |
| Collection locale unavailable | App Store | 522 | 100.00 | source-unavailable field | low | Use storefront metadata only; do not infer language. | No |
| Source imbalance | Both | 2701 | 86.06 | methodological limitation | high | Report source shares and consider source-stratified analysis; do not weight automatically. | No |
| Temporal coverage mismatch | Both | 1944 | 51.91 | methodological limitation | high | Use overlap or recent windows for cross-platform comparisons. | No |
| App Store public endpoint instability | App Store | 522 | 100.00 | methodological limitation | high | Preserve provenance and qualify retrievability; do not claim lifetime completeness. | No |

## Time Range Options

| option | start_date | end_date | total_reviews | google_play_reviews | app_store_reviews | google_play_share_pct | app_store_share_pct | low_rating_1_2_count | Advantages | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full available history | 2015-08-13 | 2026-09-21 | 3745 | 3223 | 522 | 86.06 | 13.94 | 2252 | Maximum sample and long-term trend capability. | Large source/coverage imbalance; older product states may be less relevant. |
| Cross-platform overlap | 2023-04-14 | 2026-09-14 | 1801 | 1279 | 522 | 71.02 | 28.98 | 802 | Both sources are observable throughout the defined span. | Still imbalanced and includes several product eras. |
| Last 24 months | 2024-09-22 | 2026-09-22 | 736 | 403 | 333 | 54.76 | 45.24 | 549 | Recent, large sample with both platforms. | May still mix older and current app versions. |
| Last 18 months | 2025-03-22 | 2026-09-22 | 581 | 308 | 273 | 53.01 | 46.99 | 434 | Stronger current-product relevance with trend depth. | Smaller sample and possible source imbalance. |
| Last 12 months | 2025-09-22 | 2026-09-22 | 366 | 198 | 168 | 54.10 | 45.90 | 296 | High recency and both platforms represented. | Less seasonality/history and smaller subgroup samples. |
| Last 6 months | 2026-03-22 | 2026-09-22 | 166 | 97 | 69 | 58.43 | 41.57 | 132 | Most current customer voice. | Smallest sample and weak trend/seasonality capability. |

No overall score or final time range is selected. The team should weigh recency, sample size, cross-platform coverage, source balance, current-product relevance, and trend capability.

## Limitations

- Reviews are self-selected public feedback and are not representative of all TCInvest customers.
- App Store public endpoint coverage has been unstable; 522 records mean retrievable saved evidence, not all lifetime reviews.
- Collection locale/storefront are metadata, not detected review language.
- Exact duplicate text may represent legitimate independent reviews; identity is keyed by `(source, review_id)`.
- Monthly spikes are statistical flags and cannot establish product-event causes.
- Average ratings do not adjust for source mix or review propensity.

## Recommended Next Decisions

1. Select an analysis time range after agreeing on the intended balance between recency, sample size, and cross-platform comparability.
2. Decide whether downstream reporting should be source-stratified and whether any weighting is methodologically justified.
3. Define handling rules for missing app versions, very short reviews, and duplicate text without deleting valid review IDs by default.
4. Plan language detection separately; do not reuse collection locale as language ground truth.
5. Investigate flagged months against documented product/release events before interpreting them.

## Integrity Verification

The audit script reads the three standardized inputs and both primary raw inputs only for analysis/hash verification. It does not write to those files. SHA-256 checks are compared before and after output generation.
