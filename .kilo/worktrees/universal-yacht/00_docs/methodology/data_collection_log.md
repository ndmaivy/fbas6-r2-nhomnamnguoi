## Google Play

- App: TCInvest
- Package ID: `com.fss.tcbs.mobiletrading`
- Source: Google Play

### Google Play Test Collection

- File: `01_data/raw/google_play/google_play_test.csv`
- Purpose: Collector validation only; this is not the canonical analytical dataset.
- Test rows: 100
- Test collection locales: `vi_vn` = 50, `en_us` = 50
- Test status: Success

The `lang` field in this legacy test file records the collection locale. It must not be interpreted as the actual language of the review content.

### Google Play Production Collection

- File: `01_data/raw/google_play/2026-09-22_google_play_raw.csv`
- Purpose: Canonical raw Google Play dataset
- Collection date: 2026-09-22
- Collection method: `google-play-scraper`, `Sort.NEWEST`, continuation-token pagination
- Production storefront/country: `vn`
- Raw records retrieved: 3,223
- Unique reviews after `reviewId` deduplication: 3,223
- Collection locale raw counts: `vi_vn` = 2,712, `en_vn` = 511
- Cross-locale duplicate review IDs: 0
- Review date range: 2015-08-13T11:10:30+00:00 to 2026-09-21T12:13:27+00:00
- Rating distribution: 1 = 1,799; 2 = 205; 3 = 150; 4 = 134; 5 = 935
- Stop reason: both locales returned an empty batch after pagination
- Production status: Success

Production collection metadata is represented by three separate fields:

- `collection_language`: language parameter sent to the collector (`vi` or `en`)
- `collection_country`: storefront/country parameter sent to the collector (`vn`)
- `collection_locale`: combined collection configuration (`vi_vn` or `en_vn`)

These collection fields do not establish the actual language of review content. The raw production collector does not infer `detected_language`; uncertain language detection is deferred to a later processing phase.

### Google Play Collection Limitations

- The dataset contains the reviews retrievable through the public library/API at collection time and must not be described as a guaranteed complete lifetime population.
- Pagination ended when each locale returned an empty batch; endpoint behavior may change over time.
- The two collection locales can theoretically overlap, so canonical deduplication is based on `reviewId`, not review text.
- Missing `appVersion` is retained as provided by the source; 459 canonical rows have no app version.

## App Store

- App: TCInvest
- App ID: 1037255487
- Storefront: `vn`
- Collection method: Apple public customer-review RSS feed (multi-endpoint JSON + XML aggregation)
- Pages tested: 1–10
- HTTP response: 200
- Previous canonical snapshot: 209 unique reviews
- Previous snapshot detected-language distribution: `vi` = 194, `en` = 15
- US storefront result: No usable reviews were returned in the current collection
- Test status: Success

209 unique App Store reviews were retrievable through the selected public collection method at the time of collection.

### App Store Expanded Raw-Evidence Canonical

- Previous snapshot file: `01_data/raw/app_store/2026-09-22_app_store_raw.csv`
- Previous snapshot size: 209 unique reviews
- Expanded file: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded.csv`
- Expanded size: 447 unique reviews
- Additional saved-evidence review IDs included: 238
- Deduplication rule: `review_id` only
- Review date range: 2024-09-18T10:02:07+00:00 to 2026-04-29T02:36:56+00:00

A provenance and canonical-scope audit found 238 additional structurally valid TCInvest review IDs in saved raw JSON/XML responses from earlier collection runs and endpoint/sort combinations. The expanded dataset retains reviews with different IDs even when their content is identical.

447 unique App Store review records were retrievable across the saved public-response evidence collected during the data collection process. This expanded dataset does not claim to represent all lifetime App Store reviews.

No language detection was run during the rebuild. The expanded raw file records `lang` as `unknown` because the saved review entries do not provide reliable review-level language metadata.

### App Store Canonical v2 After Recency Audit

- Pre-diagnostic canonical snapshot: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded.csv`
- Pre-diagnostic snapshot size: 447 unique review IDs
- Recency diagnostic date: 2026-09-22
- Diagnostic result: 75 additional unique review IDs validated against saved VN JSON/XML and public-page evidence
- Canonical v2 file: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv`
- Canonical v2 size: 522 unique review IDs
- Deduplication rule: `review_id` only
- Canonical v2 date range: 2023-04-14T03:22:33+00:00 to 2026-09-14T07:44:28+00:00

Public App Store endpoint coverage was observed to be unstable across page, sort-mode, and JSON/XML combinations: identical bounded request sets returned overlapping but different slices, including HTTP 200 responses with empty feeds. All 75 additional IDs passed structural, provenance, App ID, storefront, and cross-source conflict validation.

Canonical v2 is the union of all unique review IDs in the validated saved evidence available to this project at rebuild time. It must not be described as all lifetime App Store reviews.

### App Store Collection Limitations

- Public App Store endpoints may not expose all lifetime reviews.
- The queried JSON/XML endpoints, sort modes, pages, and retries overlap; raw entry counts must not be added together as a sample size.
- The canonical review count is based on deduplicated `review_id` values.
- Storefront identifies the collection endpoint and does not establish the actual language of a review.
- The previous 209-row snapshot's language value is a derived heuristic based on review content, not ground truth. In particular, language cannot be inferred reliably from storefront or collection locale alone.

### Data Source Notes
Due to Apple RSS edge cache behavior (where specific single page/sort combinations intermittently return empty entries), the collector queries across default, `mostrecent`, and `mostHelpful` endpoints in both JSON and XML formats, performing automated deduplication by `review_id`.

The 209-row and 447-row App Store files are preserved as historical snapshots. After the recency diagnostic, the 522-row v2 file is the broadest validated union of saved TCInvest App Store evidence. Google Play test and production files remain separate; only the dated Google Play production file is canonical for the completed collection phase.
