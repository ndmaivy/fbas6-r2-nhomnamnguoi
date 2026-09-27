# Data Standardization Log

## Scope

This step maps the two primary raw review datasets to a common schema. It does not clean text, remove rows, deduplicate by text, detect language, assign sentiment, select a time range, or perform analytical classification.

## Input Files

- Google Play: `01_data/raw/google_play/2026-09-22_google_play_raw.csv`
- App Store primary v2: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv`
- The historical 447-row App Store snapshot is not used as a primary input.

## Output Files

- `01_data/interim/google_play_standardized.csv`
- `01_data/interim/app_store_standardized.csv`
- `01_data/interim/reviews_merged_standardized.csv`

## Raw Schema Inspection — Google Play

| Column | pandas dtype | Example value |
|---|---|---|
| `reviewId` | `string` | 6638c299-2864-4386-837e-41064b75be48 |
| `userName` | `str` | Thanh Son Huynh |
| `userImage` | `str` | https://play-lh.googleusercontent.com/a-/ALV-UjWVYyexHJs75plCofmmf_iI7Pk1lf4Io7Z1kkaN4-AfMoEUGsE |
| `content` | `str` | sao cứ cứng đơ không nhích nhút gõ bất kỳ một chữ nào được.... |
| `score` | `int64` | 1 |
| `thumbsUpCount` | `int64` | 0 |
| `reviewCreatedVersion` | `str` | 6.4.5 |
| `at` | `str` | 2026-09-21 12:13:27 |
| `replyContent` | `str` | TCBS trân trọng cảm ơn các góp ý của Quý khách. Hiện nay mạng internet thường bị nghẽn do lượng người online nhiều, d… |
| `repliedAt` | `str` | 2021-09-22 17:22:38 |
| `appVersion` | `str` | 6.4.5 |
| `source` | `str` | Google Play |
| `collection_language` | `str` | vi |
| `collection_country` | `str` | vn |
| `collection_locale` | `str` | vi_vn |
| `retrieved_from_locales` | `str` | vi_vn |

## Raw Schema Inspection — App Store

| Column | pandas dtype | Example value |
|---|---|---|
| `review_id` | `string` | 14548034358 |
| `user_name` | `str` | Lethuylinh1004 |
| `rating` | `int64` | 1 |
| `title` | `str` | Liên tục lỗi không thể truy cập |
| `content` | `str` | Là một người dùng lâu năm của tech, ban đầu rất hài lòng về chất lượng và giao diện của app, dễ giao dịch. Nhưng vài … |
| `app_version` | `str` | 6.4.6 |
| `updated_at` | `str` | 2026-09-14T00:44:28-07:00 |
| `vote_sum` | `int64` | 0 |
| `vote_count` | `int64` | 0 |
| `source` | `str` | App Store |
| `endpoint` | `str` | vn\|json\|default\|page=1 |
| `lang` | `str` | unknown |
| `storefront` | `str` | vn |
| `raw_occurrence_count` | `int64` | 5 |
| `raw_source_files` | `str` | diagnostics/recency_2026-09-22/vn_page_01_default.json;diagnostics/recency_2026-09-22/vn_page_01_mostHelpful.xml;diag… |
| `source_groups` | `str` | diagnostic_recency_2026-09-22 |
| `endpoint_groups` | `str` | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1… |
| `belongs_to_tcinvest_response` | `bool` | True |
| `substantive_conflict_fields` | `str` | null only |

## Field Mappings

| Common field | Google Play raw field | App Store raw field |
|---|---|---|
| `review_id` | `reviewId` | `review_id` |
| `source` | `source` | `source` |
| `review_date` | `at` | `updated_at` |
| `rating` | `score` | `rating` |
| `title` | null (not supplied) | `title` |
| `review_text_raw` | `content` | `content` |
| `app_version` | `reviewCreatedVersion` | `app_version` |
| `user_name` | `userName` | `user_name` |
| `developer_reply` | `replyContent` | null (not supplied) |
| `developer_reply_date` | `repliedAt` | null (not supplied) |
| collection metadata | `collection_country`, `collection_language`, `collection_locale` | null; `storefront` retained separately |
| `detected_language` / method | null | null |
| `source_endpoint` | null (not supplied) | `endpoint_groups` |
| `raw_source_file` | primary raw input path | `raw_source_files` |
| `google_thumbs_up_count` | `thumbsUpCount` | null |
| App Store vote fields | null | `vote_sum`, `vote_count` |

## Equivalent and Source-Specific Fields

- Review identity, content, rating, review date, app version, and user name have direct source-specific equivalents.
- Google Play alone supplies developer-reply fields and thumbs-up count.
- App Store alone supplies title and App Store vote sum/count.
- Google Play collection locale is request metadata, not detected review language.
- App Store storefront is retained as storefront metadata and is not copied into language fields.

## Date Conversion

- Parseable review timestamps are serialized as ISO-8601 UTC without changing the represented instant.
- Google Play timestamps are timezone-naive in the raw CSV; they are interpreted as UTC to remain consistent with the validated raw collection summary.
- Rows with parse failures would be retained with null standardized dates and logged. No parse failures occurred in this run.
- Date parse failures: 0

## Null Handling

- Missing source fields become null/empty CSV fields in the common schema.
- Missing values are not imputed.
- `detected_language` and `language_detection_method` are null for every row because language detection has not been run.
- Review text is copied verbatim; no lowercase, whitespace normalization, punctuation removal, translation, accent removal, spam filtering, or short-review filtering is performed.

## Assumptions and Unmapped Raw Fields

- Global identity is the pair `(source, review_id)`, not `review_id` alone.
- Google Play `reviewCreatedVersion` and `appVersion` differ in 0 rows where both are present. `reviewCreatedVersion` is mapped to the common `app_version`; raw `appVersion` remains unmapped as a redundant field in this dataset.
- Google Play `userImage` and `retrieved_from_locales` are not part of the requested common schema. `collection_locale` remains available.
- App Store `lang` is not mapped because it is `unknown`/not reliable language ground truth.
- App Store representative `endpoint`, `raw_occurrence_count`, `source_groups`, response-identity flag, and conflict flag are not separate common columns; aggregate `endpoint_groups` and `raw_source_files` are retained.

## Row Counts and Validation

| Dataset | Input rows | Output rows | Unique IDs | Earliest UTC | Latest UTC |
|---|---:|---:|---:|---|---|
| Google Play | 3223 | 3223 | 3223 | 2015-08-13T11:10:30+00:00 | 2026-09-21T12:13:27+00:00 |
| App Store | 522 | 522 | 522 | 2023-04-14T03:22:33+00:00 | 2026-09-14T07:44:28+00:00 |
| Merged | 3745 | 3745 | n/a across platforms | 2015-08-13T11:10:30+00:00 | 2026-09-21T12:13:27+00:00 |

- Google Play rating distribution: {'1': 1799, '2': 205, '3': 150, '4': 134, '5': 935}
- App Store rating distribution: {'1': 217, '2': 31, '3': 25, '4': 17, '5': 232}
- Merged duplicate `(source, review_id)` rows: 0
- Merged missing review ID/date/rating/text: 0/0/0/0

## Raw Input Integrity

- Google Play SHA256 before: `dad62eed262ba7ffa0d3dba6881aa4e48a086e555e5a59d230ef5d4f32379c5a`
- Google Play SHA256 after: `dad62eed262ba7ffa0d3dba6881aa4e48a086e555e5a59d230ef5d4f32379c5a`
- App Store SHA256 before: `f96cd67920d15f704982e722fdd74cc3a6581fcdc6f7055fcd04ad6e375ef2e1`
- App Store SHA256 after: `f96cd67920d15f704982e722fdd74cc3a6581fcdc6f7055fcd04ad6e375ef2e1`
- Raw inputs unchanged: True
