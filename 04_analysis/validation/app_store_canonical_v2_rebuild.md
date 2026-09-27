# App Store Canonical v2 Rebuild

## Inputs

- Previous canonical: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded.csv` (447 IDs)
- Validated candidates: `05_outputs/tables/app_store_candidate_validation.csv` (75 VALID IDs)

## Rebuild decision

All 75 candidate IDs were traceable to saved VN diagnostic evidence for TCInvest App ID `1037255487`, with valid core fields and no substantive multi-source conflicts. Canonical v2 was therefore built as a union without overwriting the prior snapshot.

## Identity and duplicate policy

- Union key: `review_id`
- Exact content, title, author, or rating is not a deduplication key.
- Reviews with different IDs remain separate even when text is identical.

## v2 validation

- Rows: 522
- Unique review IDs: 522
- Duplicate review IDs: 0
- Date range: 2023-04-14T03:22:33+00:00 to 2026-09-14T07:44:28+00:00
- Rating distribution: {'1': 217, '2': 31, '3': 25, '4': 17, '5': 232}
- Missing content/rating/date/version: 0/0/0/0

## Provenance

The original 447 rows preserve their prior provenance fields. Added rows record diagnostic raw files, endpoint groups, raw occurrence counts, VN storefront, and TCInvest response identity. Review text was not cleaned or normalized.

## Limitations

- Public App Store endpoint coverage is unstable across otherwise identical runs and across page/sort/format routes.
- v2 is the union of validated saved evidence available to this project, not all lifetime App Store reviews.
- Additional retrievable IDs may appear in future bounded diagnostics.
