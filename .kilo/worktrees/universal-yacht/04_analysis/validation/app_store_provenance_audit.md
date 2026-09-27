# App Store Provenance Audit

This read-only audit answers one question: can each canonical review be traced back to saved raw response evidence?

## Canonical Dataset

- File: `01_data/raw/app_store/2026-09-22_app_store_raw.csv`
- Rows: 209
- Unique `review_id`: 209
- Duplicate `review_id` rows: 0
- Columns: `review_id`, `user_name`, `rating`, `title`, `content`, `app_version`, `updated_at`, `vote_sum`, `vote_count`, `source`, `endpoint`, `lang`, `storefront`

## Raw Evidence Inventory

- Files scanned: 219 (120 JSON, 99 XML)
- Files parsed successfully: 219
- Parse failures: 0
- Review-bearing files: 15
- Total parsed review occurrences: 750
- Unique raw review IDs: 447

| Inferred raw group | Files scanned | Review-bearing files | Unique review IDs |
|---|---:|---:|---:|
| legacy raw_json collection/retry | 21 | 2 | 100 |
| unprefixed legacy raw_responses collection | 66 | 6 | 300 |
| us-prefixed multi-endpoint collection | 66 | 0 | 0 |
| vn-prefixed multi-endpoint collection | 66 | 7 | 209 |

## Canonical-to-Raw Traceability

- Canonical reviews: 209
- Traced to at least one raw response: 209
- Not traced: 0
- Traceability: 100.00%
- Raw review IDs present in canonical: 209

A review is counted as traced only when its canonical `review_id` occurs in at least one parsed saved JSON/XML review entry.

## Field Integrity

Comparisons first use exact strings. Only when exact comparison fails are line-ending/HTML-escape equivalence, numeric equivalence, or timestamp equivalence considered. A substantive mismatch means no saved occurrence for that ID matched the canonical value under the stated comparison.

| Field | Exact match | Serialization-equivalent | Substantive mismatch | Not found |
|---|---:|---:|---:|---:|
| Content | 209 | 0 | 0 | 0 |
| Title | 209 | 0 | 0 | 0 |
| Rating | 209 | 0 | 0 | 0 |
| Date | 0 | 209 | 0 | 0 |
| App version | 209 | 0 | 0 | 0 |

Canonical field integrity is judged against any saved occurrence of the same ID. Saved occurrences with multiple distinct raw values are reported separately and are not silently collapsed:

- Canonical IDs with conflicting saved title values: 0
- Canonical IDs with conflicting saved content values: 0
- Canonical IDs with conflicting saved rating values: 0
- Canonical IDs with conflicting saved date values: 0
- Canonical IDs with conflicting saved app-version values: 0

## Untraced Canonical Reviews

None. All 209 canonical review IDs were found in saved raw response evidence.

## Raw Reviews Outside Canonical Dataset

- Total unique raw review IDs: 447
- Raw review IDs present in canonical: 209
- Raw review IDs absent from canonical: 238
- Outside-ID date range: 2024-09-18T10:02:07+00:00 to 2025-11-05T03:39:52+00:00
- Outside-ID rating distribution: 1=68, 2=13, 3=11, 4=7, 5=139

Outside IDs by inferred source group (groups can overlap when the same ID appears in multiple saved runs):

| Inferred source group | Unique outside IDs | Interpretation |
|---|---:|---|
| legacy raw_json collection/retry | 100 | Older JSON page/retry collection artifacts. |
| unprefixed legacy raw_responses collection | 144 | Earlier unprefixed multi-endpoint collection artifacts. |

Review-bearing raw files containing IDs outside the canonical dataset:

| Raw source file | Unique outside IDs | Inferred storefront | Sort mode | Page/retry metadata |
|---|---:|---|---|---|
| `raw_json/page_04.json` | 50 | not encoded | not encoded | page=04; retry=none |
| `raw_json/page_08.json` | 50 | not encoded | not encoded | page=08; retry=none |
| `raw_responses/page_05_mostHelpful.xml` | 50 | not encoded | mostHelpful | page=05; retry=none |
| `raw_responses/page_07_mostHelpful.json` | 44 | not encoded | mostHelpful | page=07; retry=none |
| `raw_responses/page_10_mostHelpful.xml` | 50 | not encoded | mostHelpful | page=10; retry=none |

The evidence indicates that the larger raw pool combines multiple collection layouts/runs and overlapping endpoint/page/sort/retry responses. The dated canonical CSV contains the 209 IDs selected by its completed collector run; the additional raw IDs mainly belong to other saved collection attempts or endpoint results. This audit does not add those IDs to the canonical dataset.

## Manual QA Sample

The sample contains 19 unique reviews after overlap removal. Random rating strata use `random_state=42`; earliest/latest strata use stable date and `review_id` ordering.

### 1. Random 1-star (random_state=42) — `12189754220`

- Rating: 1
- Title: Như hạch
- Date: 2025-01-16 02:52:36+00:00
- Content (first 200 characters): Toàn lỗi không đặt được lệnh. Nhiều khi đến tài khoản cũng không hiển thị. Má bực muốn bán ko đc mua ko xong.
- Raw source file(s): raw_responses/vn_page_06_default.json
- Exact content match: Yes

### 2. Random 1-star (random_state=42) — `13934417294`

- Rating: 1
- Title: Dịch vụ quá kém.
- Date: 2026-04-08 03:52:30+00:00
- Content (first 200 characters): Gọi tổng đài báo bận đá sang chát zalo, face... ko giải quyết đc vấn đề
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 3. Random 1-star (random_state=42); Latest dates — `14007797037`

- Rating: 1
- Title: Không nên dùng
- Date: 2026-04-29 02:27:19+00:00
- Content (first 200 characters): App cập nhật dữ liệu lúc thị trường mở cửa, không giao dịch được, xứng đáng 1 sao
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 4. Random 1-star (random_state=42) — `12524926430`

- Rating: 1
- Title: App thường xuyên lỗi
- Date: 2025-04-10 04:07:48+00:00
- Content (first 200 characters): App hoạt động không ổn định, thường xuyên không thể truy cập được. Nên cân nhắc sử dụng app khác
- Raw source file(s): raw_responses/vn_page_06_default.json
- Exact content match: Yes

### 5. Random 1-star (random_state=42) — `12301648806`

- Rating: 1
- Title: Hay bị lỗi chuyển tiền, nhắn tin không xử lý
- Date: 2025-02-12 10:04:36+00:00
- Content (first 200 characters): Tệ
- Raw source file(s): raw_responses/vn_page_06_default.json
- Exact content match: Yes

### 6. Random 5-star (random_state=42) — `13757354364`

- Rating: 5
- Title: Tốt
- Date: 2026-02-16 23:57:51+00:00
- Content (first 200 characters): App rất tuyệt vời chuyên nghiệp
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 7. Random 5-star (random_state=42) — `11737196985`

- Rating: 5
- Title: app ổn định
- Date: 2024-09-18 12:05:59+00:00
- Content (first 200 characters): chất lượng ok
- Raw source file(s): raw_responses/page_09_mostrecent.json;raw_responses/vn_page_09_default.json;raw_responses/vn_page_09_default.xml;raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 8. Random 5-star (random_state=42) — `11739086712`

- Rating: 5
- Title: .
- Date: 2024-09-18 23:19:23+00:00
- Content (first 200 characters): 105CA32888 tôi thích ứng dụng
- Raw source file(s): raw_responses/page_09_mostrecent.json;raw_responses/vn_page_09_default.json;raw_responses/vn_page_09_default.xml;raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 9. Random 5-star (random_state=42) — `14005255766`

- Rating: 5
- Title: Tải app không được
- Date: 2026-04-28 09:55:55+00:00
- Content (first 200 characters): Phải chuyển vùng trên App Store mới tìm đc app này. Trong khi thấy những app khác của các ngân hàng hay SSI thì có. Ngộ vậy?
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 10. Random 5-star (random_state=42) — `11737756821`

- Rating: 5
- Title: 105C1703HV tôi thích bảng giá
- Date: 2024-09-18 14:59:48+00:00
- Content (first 200 characters): 105C1703HV tôi thích bảng giá
- Raw source file(s): raw_responses/page_09_mostrecent.json;raw_responses/vn_page_09_default.json;raw_responses/vn_page_09_default.xml;raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 11. Earliest dates — `11737075811`

- Rating: 5
- Title: Nhận tiền
- Date: 2024-09-18 11:23:11+00:00
- Content (first 200 characters): 105CB45338 ↵ Tôi yêu TCBS
- Raw source file(s): raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 12. Earliest dates — `11737079010`

- Rating: 5
- Title: Tốt
- Date: 2024-09-18 11:24:24+00:00
- Content (first 200 characters): 105C06040O nhớ gửi mình 30 ixu nha
- Raw source file(s): raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 13. Earliest dates — `11737104569`

- Rating: 5
- Title: Ứng dụng rất tốt
- Date: 2024-09-18 11:33:43+00:00
- Content (first 200 characters): 5 sao
- Raw source file(s): raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 14. Earliest dates — `11737118633`

- Rating: 5
- Title: tuyệt vời
- Date: 2024-09-18 11:38:45+00:00
- Content (first 200 characters): 105CI43368 tôi yêu tcbs
- Raw source file(s): raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 15. Earliest dates — `11737153075`

- Rating: 5
- Title: Ứng dụng đầu tư
- Date: 2024-09-18 11:50:54+00:00
- Content (first 200 characters): Ứng dụng giao dịch chứng khoán tốt, đáng dùng
- Raw source file(s): raw_responses/vn_page_09_mostHelpful.xml
- Exact content match: Yes

### 16. Latest dates — `14007818169`

- Rating: 1
- Title: Không nên dùng
- Date: 2026-04-29 02:36:56+00:00
- Content (first 200 characters): Sàn gì mà 29/4/26 k cập nhập, k làm việc. App hay out ra load lại. Không muốn nặng lời nhưng phải dùng từ Ngu. Đã trải nghiệm 1 time
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 17. Latest dates — `14007817541`

- Rating: 1
- Title: Bực mình
- Date: 2026-04-29 02:36:39+00:00
- Content (first 200 characters): Vào ngày giao dịch lại đi cập nhật, đơ ra, làm người ta không giao dịch gì được. Thiệt hại tính bằng tiền đó!
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 18. Latest dates — `14007814276`

- Rating: 1
- Title: App hay bị lỗi không giao dịch được. 29/4/2026 là một ví dụ. Công ty không xin lỗi, không phản hồi
- Date: 2026-04-29 02:35:12+00:00
- Content (first 200 characters): App lỗi không gd được 29/4/2026
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

### 19. Latest dates — `14007807831`

- Rating: 1
- Title: App quá tệ
- Date: 2026-04-29 02:32:14+00:00
- Content (first 200 characters): App lỗi thường xuyên. Gần nhất là sáng 29/4/2026
- Raw source file(s): raw_responses/page_02_default.json;raw_responses/vn_page_02_default.json
- Exact content match: Yes

## Limitations

- This audit establishes traceability to saved local evidence only. It makes no claim about whether a review is currently visible on the App Store website.
- Storefront, endpoint, sort mode, page, retry, and run grouping are inferred from filenames when not explicitly encoded in the response payload.
- Exact-string checks are sensitive to serialization. Serialization-equivalent results are reported separately rather than silently normalized.
- The same review ID may occur in several overlapping raw files; occurrence counts are not sample-size counts.
- Language labels are outside the provenance comparison and are not treated as ground truth.

## Conclusion

209 of 209 canonical App Store reviews (100.00%) can be traced by `review_id` to saved raw JSON/XML evidence. All compared canonical fields are supported by at least one saved raw occurrence, subject to the exact-versus-serialization classifications above.
