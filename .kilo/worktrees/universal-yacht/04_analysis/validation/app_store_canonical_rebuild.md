# App Store Canonical Rebuild

## Scope Change

- Previous canonical snapshot: 209 unique review IDs
- Saved raw-evidence universe: 447 unique review IDs
- Added to expanded canonical: 238 review IDs
- Expanded canonical file: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded.csv`

## Inclusion Rule

Include every unique review ID parsed as a normal review entry from saved JSON/XML evidence tied to TCInvest App ID `1037255487`. No rating, text, date, language, or endpoint filter was applied.

## Deduplication Rule

Deduplicate only by identical `review_id`. When an ID occurs in multiple raw files, keep one record and merge its provenance fields. Content, title, author, and rating are not identity keys.

All duplicate raw occurrences were compared across content, title, rating, timestamp, and app version. Substantive conflicts found: 0.

## Exact-Content Duplicates

Eight previously ambiguous outside IDs share exact content with another review ID. They remain included because each has its own review ID, author/date/source evidence, VN storefront evidence, and TCInvest App ID evidence. Short generic text such as “Good”, “Tệ”, “Ok”, or “Tốt” is not grounds for deletion.

| review_id | user_name | rating | updated_at | raw source files | storefront | App ID |
|---|---|---:|---|---|---|---|
| 11736891062 | フォローカイ | 5 | 2024-09-18T03:08:49-07:00 | raw_responses/page_10_mostHelpful.xml | vn | 1037255487 |
| 11737005757 | huỷ diệt áp sờ to | 5 | 2024-09-18T03:56:38-07:00 | raw_responses/page_10_mostHelpful.xml | vn | 1037255487 |
| 11739561202 | Trade and Stock | 5 | 2024-09-18T19:47:55-07:00 | raw_json/page_08.json | vn | 1037255487 |
| 11739650810 | Sinbad_dao | 5 | 2024-09-18T20:30:05-07:00 | raw_json/page_08.json | vn | 1037255487 |
| 11739674478 | Song Lam 2012 | 5 | 2024-09-18T20:41:33-07:00 | raw_json/page_08.json | vn | 1037255487 |
| 11740117898 | Abcvtai | 5 | 2024-09-19T00:28:12-07:00 | raw_json/page_08.json | vn | 1037255487 |
| 12727113643 | zumi ng | 5 | 2025-06-02T05:18:56-07:00 | raw_responses/page_05_mostHelpful.xml | vn | 1037255487 |
| 13276981462 | TTungwwđ | 1 | 2025-10-17T00:44:07-07:00 | raw_json/page_04.json | vn | 1037255487 |

## Temporal Range

- Earliest: 2024-09-18T10:02:07+00:00
- Latest: 2026-04-29T02:36:56+00:00

No time-range filter was applied.

## Why 447 Is Preferred for Downstream Analysis

The 447-row dataset uses the full set of unique, structurally valid TCInvest review IDs present in saved raw evidence rather than limiting analysis to one 209-row collector snapshot. It provides broader endpoint, sort-mode, page, and collection-run coverage while preserving review-level provenance.

## Limitations

- The expanded dataset does not claim to contain all lifetime App Store reviews.
- Public response endpoints can expose different overlapping slices at different collection times.
- The previous 209-row canonical snapshot is intentionally preserved as historical evidence.
- Language was not detected or inferred during this rebuild; `lang` is recorded as `unknown`.
- Exact-content duplicates with different IDs were retained and may require contextual review downstream.

No raw file, prior canonical file, or existing audit artifact was modified by this rebuild.
