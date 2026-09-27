# App Store Canonical Scope Audit

## 1. Why This Audit Was Needed

The 209-review canonical App Store dataset is fully traceable to saved raw evidence, but the saved JSON/XML evidence contains 447 unique review IDs. This leaves 238 IDs outside the canonical file. This diagnostic audit characterizes those IDs without modifying or merging any raw or canonical data.

## 2. Raw Review Universe

- Raw evidence files parsed: 219
- Parse failures: 0
- Parsed review occurrences: 750
- Unique raw review IDs: 447
- Canonical IDs found in raw universe: 209
- Outside-canonical IDs: 238
- Identity check: 209 + 238 = 447

Each raw ID is retained independently. Records were deduplicated only by exact `review_id`; equal content or author did not cause IDs to be merged.

## 3. Canonical vs Outside Dataset

| Population | Unique IDs | Earliest review | Latest review |
|---|---:|---|---|
| Canonical | 209 | 2024-09-18T11:23:11+00:00 | 2026-04-29T02:36:56+00:00 |
| Outside canonical | 238 | 2024-09-18T10:02:07+00:00 | 2025-11-05T03:39:52+00:00 |
| Combined raw universe | 447 | 2024-09-18T10:02:07+00:00 | 2026-04-29T02:36:56+00:00 |

- Outside rating distribution: 1=68, 2=13, 3=11, 4=7, 5=139
- Outside app-version distribution: 5.7=120, 5.8=10, 5.8.2=14, 5.9=42, 6.0=14, 6.0.2=13, 6.1=25
- Missing content: 0
- Missing rating: 0
- Missing date: 0
- Missing app version: 0
- Missing title: 0

## 4. Temporal Coverage

- Outside before canonical range: 50
- Outside inside canonical range: 188
- Outside after canonical range: 0

The outside IDs are compared against the exact canonical timestamp boundaries, not merely calendar dates.

### Counts by year

| Year | Canonical | Outside | Combined raw universe |
|---|---:|---:|---:|
| 2024 | 62 | 144 | 206 |
| 2025 | 66 | 94 | 160 |
| 2026 | 81 | 0 | 81 |

### Counts by month

| Month | Canonical | Outside | Combined raw universe |
|---|---:|---:|---:|
| 2024-09 | 59 | 122 | 181 |
| 2024-10 | 0 | 12 | 12 |
| 2024-11 | 0 | 8 | 8 |
| 2024-12 | 3 | 2 | 5 |
| 2025-01 | 6 | 0 | 6 |
| 2025-02 | 8 | 0 | 8 |
| 2025-03 | 13 | 0 | 13 |
| 2025-04 | 18 | 0 | 18 |
| 2025-05 | 2 | 9 | 11 |
| 2025-06 | 0 | 30 | 30 |
| 2025-07 | 0 | 12 | 12 |
| 2025-08 | 0 | 18 | 18 |
| 2025-09 | 0 | 9 | 9 |
| 2025-10 | 0 | 15 | 15 |
| 2025-11 | 11 | 1 | 12 |
| 2025-12 | 8 | 0 | 8 |
| 2026-01 | 27 | 0 | 27 |
| 2026-02 | 17 | 0 | 17 |
| 2026-03 | 21 | 0 | 21 |
| 2026-04 | 16 | 0 | 16 |

## 5. Endpoint / Sort / Page Contribution

Counts by mechanism can overlap because the same review ID may be present in multiple saved responses.

| Run group | Format | Sort mode | Page | Raw records | Unique IDs | Canonical IDs | Outside IDs |
|---|---|---|---|---:|---:|---:|---:|
| legacy_raw_json | JSON | mostrecent | 4 | 50 | 50 | 0 | 50 |
| legacy_raw_json | JSON | mostrecent | 8 | 50 | 50 | 0 | 50 |
| unprefixed_legacy_raw_responses | JSON | mostHelpful | 7 | 50 | 50 | 6 | 44 |
| unprefixed_legacy_raw_responses | JSON | default | 2 | 50 | 50 | 50 | 0 |
| unprefixed_legacy_raw_responses | JSON | mostrecent | 9 | 50 | 50 | 50 | 0 |
| unprefixed_legacy_raw_responses | XML | mostHelpful | 10 | 50 | 50 | 0 | 50 |
| unprefixed_legacy_raw_responses | XML | mostHelpful | 5 | 50 | 50 | 0 | 50 |
| unprefixed_legacy_raw_responses | XML | default | 3 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | JSON | default | 2 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | JSON | default | 6 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | JSON | default | 9 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | XML | mostHelpful | 9 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | XML | default | 3 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | XML | mostrecent | 3 | 50 | 50 | 50 | 0 |
| vn_prefixed_raw_responses | XML | default | 9 | 50 | 50 | 50 | 0 |

- Outside storefront distribution (unique-ID contributions): vn=238
- Outside endpoint-format distribution: json=144, xml=100
- Outside sort-mode distribution: mostHelpful=144, mostrecent=100
- Outside page distribution: 10=50, 4=50, 5=50, 7=44, 8=50
- Outside source-file-group distribution: legacy_raw_json=100, unprefixed_legacy_raw_responses=144

## 6. JSON vs XML Overlap

- IDs only in JSON: 238
- IDs only in XML: 153
- IDs present in both JSON and XML: 56
- JSON unique IDs: 294
- XML unique IDs: 209

These are ID-level sets; JSON/XML serialization copies are not counted as separate reviews.

## 7. Storefront Analysis

- Outside IDs from `vn`: 238
- Outside IDs from `us`: 0
- Outside IDs with unknown storefront: 0

Storefront is derived from the saved feed URL when available, then from an explicit filename prefix only as fallback. It is not inferred from review language.

The 66 saved US-prefixed responses contain 0 parsed review records. Therefore, the saved US response set contributes no real review entries to this raw universe.

## 8. Structural Validity of Outside Reviews

- Structurally valid outside reviews: 238
- Invalid or incomplete outside records: 0
- Belonging to a TCInvest App ID `1037255487` response: 238
- Having all required core fields: 238

Definitions used:

- `belongs_to_tcinvest_response`: at least one saved occurrence is in a feed or entry link targeting App ID `1037255487`.
- `has_required_core_fields`: non-empty review ID, rating, content, author, and date.
- `is_structurally_valid_review`: required core fields are present, rating is 1–5, date parses successfully, and the response targets the TCInvest App ID.

Short or low-information text is not treated as invalid.

## 9. Possible Review-Version / Same-Author Effects

- Authors associated with multiple review IDs: 0 authors / 0 raw-universe IDs / 0 outside IDs
- Exact content values shared by different IDs: 7 content groups / 17 raw-universe IDs / 8 outside IDs
- Same-author, non-identical content pairs with similarity >= 0.90 and minimum length 10: 0 pairs / 0 outside IDs
- Review IDs with multiple saved field states: 0 raw-universe IDs / 0 outside IDs
- Outside IDs appearing in multiple inferred run groups: 6

These are signals for human review, not automatic deduplication rules. Multiple IDs from one author can be legitimate repeat reviews; equal or similar content does not prove that Apple treated the records as versions of one review.

### Exact-content groups with multiple IDs

| Content preview | Review IDs |
|---|---|
| 105CTOIYEUVN | 11737235462, 11737875975, 11739561202 |
| Good | 11736891062, 11739650810, 11739674478 |
| Tệ | 12301648806, 12605203687, 13276981462 |
| Hài lòng | 11737569918, 11740117898 |
| Ok | 11737005757, 11737301876 |
| Rất hay | 11737242792, 12727113643 |
| Tốt | 11737168948, 11737205326 |

## 10. Manual QA Sample

The reproducible selection contains 47 unique outside IDs after overlap removal. Random, one-star, and five-star selections use `random_state=42`; oldest/newest use stable date and ID ordering.

### 1. Oldest — `11736875655`

- Author: jsjdhdksyssh
- Rating: 5
- Date: 2024-09-18T03:02:07-07:00
- Title: Hữu ích
- Content (first 250 characters): Giao dịch tiện lợi và nhanh chóng
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 2. Oldest — `11736877477`

- Author: 105CG78688
- Rating: 5
- Date: 2024-09-18T03:02:55-07:00
- Title: Rất là ok
- Content (first 250 characters): Nhanh gọn thuận tiện
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 3. Oldest — `11736879163`

- Author: BTHV.SSV
- Rating: 5
- Date: 2024-09-18T03:03:40-07:00
- Title: App rất dễ sử dụng
- Content (first 250 characters): Nhiều tiện ích Stk 105CH91198
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 4. Oldest — `11736881714`

- Author: 105CP01787
- Rating: 5
- Date: 2024-09-18T03:04:46-07:00
- Title: 105CP01787
- Content (first 250 characters): 105CP01787 tôi thích bảng giá
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 5. Oldest — `11736881923`

- Author: Kimmy Thuỷ
- Rating: 5
- Date: 2024-09-18T03:04:51-07:00
- Title: Tài khoản: 105CB49266
- Content (first 250 characters): Tài khoản: 105CB49266 ↵ Áp rất tiện lợi. Giao dịch mua bán cổ phiếu thuận tiện và dễ sử dụng
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 6. Oldest — `11736882017`

- Author: JimmyProDuy
- Rating: 5
- Date: 2024-09-18T03:04:53-07:00
- Title: Tuyệt vời
- Content (first 250 characters): 105CBLBD05 tôi yêu thích bảng giá
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 7. Oldest; Random (random_state=42) — `11736882418`

- Author: Haáionqqqqqq
- Rating: 5
- Date: 2024-09-18T03:05:03-07:00
- Title: Ứng dụng dễ sử dụng
- Content (first 250 characters): Ứng dụng với giao diện và thao tác dễ thực hiện
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 8. Oldest — `11736883334`

- Author: Yên1305
- Rating: 5
- Date: 2024-09-18T03:05:27-07:00
- Title: Oke
- Content (first 250 characters): Ứng dụng tiện ích giúp chúng tôi kiểm soát đc tk bảo mật
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 9. Oldest — `11736883500`

- Author: Naibambi710
- Rating: 5
- Date: 2024-09-18T03:05:31-07:00
- Title: Techcombank
- Content (first 250 characters): Ứng dụng dễ xài, nhiều tiện ích
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 10. Oldest; Random (random_state=42) — `11736886805`

- Author: cocghe14
- Rating: 5
- Date: 2024-09-18T03:06:56-07:00
- Title: 105CF89579
- Content (first 250 characters): 105CF89579 tôi thích bảng giá
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 11. Newest — `13358137009`

- Author: DanhPhm
- Rating: 1
- Date: 2025-11-04T20:39:52-07:00
- Title: Lỗi chuyển tiền
- Content (first 250 characters): Chuyển tiền nhìu lần không được
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 12. Newest — `13332105950`

- Author: sơn3357
- Rating: 1
- Date: 2025-10-29T21:11:36-07:00
- Title: Lỗi bị xoá chart
- Content (first 250 characters): Nhắn hỗ trợ r mà chưa dc. Vẽ 1 2 hôm là bị xoá.
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 13. Newest — `13306623450`

- Author: carolyngp
- Rating: 1
- Date: 2025-10-23T23:33:56-07:00
- Title: càng ngày càng rối
- Content (first 250 characters): rối rắm khó khăn, tạo cái lệnh định kỳ quỹ cũng không cho
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 14. Newest — `13301878527`

- Author: Linhchikemkem
- Rating: 5
- Date: 2025-10-22T19:17:58-07:00
- Title: Mac !!!!!!!!!!!!!!!!
- Content (first 250 characters): Máy mac app vào không được nhé !
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 15. Newest — `13295667287`

- Author: VPN grand master
- Rating: 3
- Date: 2025-10-21T08:06:08-07:00
- Title: Quá phức tạp một cách không cần thiết, rối
- Content (first 250 characters): App nhiều tính năng, tốt, nhưng sắp xếp quá phức tạp một cách không cần thiết, rối. Cần làm cho đơn giản bớt. Một chức năng không cần phải xuất hiện ở nhiều nơi khác nhau.
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 16. Newest — `13290348242`

- Author: HNam9488
- Rating: 1
- Date: 2025-10-20T03:02:17-07:00
- Title: Không mua bán được trên TC Invest
- Content (first 250 characters): Ngày 20/10/2025 thị trường có phiên giảm sâu kỷ lục hơn 94 điểm, nhưng tôi không thể mua bán cổ phiếu trên app làm danh mục của tôi lỗ nặng do không thể mua để DCA
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 17. Newest — `13290082792`

- Author: Nhân viên TCB
- Rating: 1
- Date: 2025-10-20T01:29:13-07:00
- Title: App quá lag
- Content (first 250 characters): App quá lagg, ko chấp nhận nổi, bày đặt đòi wealth tech nhưng app lag lòi mà bày đặt, xem lại căn bản đã
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 18. Newest — `13290030950`

- Author: Bíbhkdhe
- Rating: 1
- Date: 2025-10-20T01:11:22-07:00
- Title: Chưa thấy cái app nào tệ như cái app này
- Content (first 250 characters): Lần đầu có cái app tệ đến mức mình phải lên app store đánh giá 1 sao. Cứ khi nào thị trường có biến lớn là app bị ngu ko load đc. Mấy lần r chứ ko phải một lần. Mất tiền oan mất lần chỉ vì cái app.
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 19. Newest; One-star (random_state=42) — `13289538564`

- Author: asusdellhp
- Rating: 1
- Date: 2025-10-19T21:46:23-07:00
- Title: Lỗi hệ thống
- Content (first 250 characters): Ngày 20/10 hệ thống trễ quá lớn. Ảnh hưởng nghiêm trong trong giao dịch phái Sinh
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 20. Newest — `13280235898`

- Author: Mr bravia
- Rating: 1
- Date: 2025-10-17T18:03:35-07:00
- Title: Load giá quá chậm
- Content (first 250 characters): Load giá quá chậm đáng 1 sao. Mấy thằng làm app ngu hay sao
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 21. Random (random_state=42) — `11751734326`

- Author: Trung thanh 1
- Rating: 5
- Date: 2024-09-22T03:54:35-07:00
- Title: 105CT91899 tôi thích bảng giá
- Content (first 250 characters): 105CT91899 tôi thích bảng giá
- App version: 5.7
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 22. Random (random_state=42) — `11736890736`

- Author: Kun2714
- Rating: 5
- Date: 2024-09-18T03:08:40-07:00
- Title: App Techcombank
- Content (first 250 characters): Qua 5 năm sử dụng , App Techcombank ổn định, dễ dàng sử dụng và có tính bảo mật cao
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 23. Random (random_state=42) — `13070665657`

- Author: lvb-:
- Rating: 1
- Date: 2025-08-28T07:06:09-07:00
- Title: Hỗ trợ kém
- Content (first 250 characters): Hỗ trợ kém, nhân viên giải thích lung tung, tiền trừ linh tinh nhân viên không tính ra nổi.
- App version: 6.0.2
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 24. Random (random_state=42) — `11809107324`

- Author: lon2002
- Rating: 5
- Date: 2024-10-07T16:07:22-07:00
- Title: OK
- Content (first 250 characters): Được
- App version: 5.8
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 25. Random (random_state=42) — `12764204218`

- Author: Nanaloveu
- Rating: 5
- Date: 2025-06-11T19:59:07-07:00
- Title: TCBS ổn đấy chứ
- Content (first 250 characters): Đã có dịp được ghé vp TCBS, thấy môi trường làm việc của các bạn rất gọn gàng sạch đẹp, thái độ, tác phong phục vụ hỗ trợ Kh cũng rất tốt, chuyên nghiệp, nhanh gọn. Nói chung là hài lòng khi mở tk và gd tại TCBS.
- App version: 5.9
- Source file(s): raw_responses/page_05_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=5
- Storefront: vn
- Structurally valid: Yes

### 26. Random (random_state=42) — `13216345199`

- Author: jbs1080
- Rating: 2
- Date: 2025-10-02T20:16:23-07:00
- Title: App cồng kềnh, phức tạp nhưng chưa tốt
- Content (first 250 characters): App mới (hiện T10/2025) rất nhiều tính năng nhưng đa số không hữu dụng cho NĐT đọc lập, nên rất cồng kềnh. Chức năng vào lệnh (Mua/Bán) rất quan trọng, nhưng giao diện KHÔNG thể hiện các bước giá, không thấy giá SÀN / TRẦN,  cực kỳ khó đặt.  ↵ Phông …
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 27. Random (random_state=42) — `11746998149`

- Author: No name 862
- Rating: 5
- Date: 2024-09-20T21:28:53-07:00
- Title: App lỗi
- Content (first 250 characters): App lỗi ko loád dc tài sản
- App version: 5.7
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 28. Random (random_state=42) — `13177936096`

- Author: nghong
- Rating: 1
- Date: 2025-09-24T03:12:36-07:00
- Title: Trải nghiệm cập nhật thay đổi CCCD tệ
- Content (first 250 characters): Popup yêu cầu thay đổi hiện lên liên tục, lúc qua bước khác cũng không lưu lại, user bấm nhầm một cái là phải làm lại từ đầu.  ↵ Yêu cầu không duyệt kĩ đã từ chối, đã vậy không cho cập nhật/khiếu nại trên yêu cầu cũ mà bắt tạo yêu cầu mới.
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 29. One-star (random_state=42) — `13042326473`

- Author: LaiLuong
- Rating: 1
- Date: 2025-08-21T01:01:23-07:00
- Title: App bị đơ chậm
- Content (first 250 characters): App bị đơ, chậm, ko vào được, tính năng nào quay tít ko thực hiện được. Nói chung là ko ổn.
- App version: 6.0.2
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 30. One-star (random_state=42) — `11989241555`

- Author: beofia
- Rating: 1
- Date: 2024-11-24T22:20:13-07:00
- Title: Không đặt được lệnh bán
- Content (first 250 characters): Mua được nhưng lệnh bán không được ↵ Trong khi mục tài sản vẫn hiện số dư, mà lúc đặt lệnh bán lại hiện lỗi không đủ số dư
- App version: 5.8.2
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 31. One-star (random_state=42) — `11787725265`

- Author: MoL6688
- Rating: 1
- Date: 2024-10-01T22:23:11-07:00
- Title: App update xong không vào được
- Content (first 250 characters): Update xong không vào được app, mấy lần trước cũng vậy, update xong là lỗi .
- App version: 5.8
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 32. One-star (random_state=42) — `11836640608`

- Author: Louis Van
- Rating: 1
- Date: 2024-10-15T06:10:07-07:00
- Title: 1sao chữ Tín.
- Content (first 250 characters): Tcbs đảo các chương trình Review/Giới thiệu, xong không thanh toán.
- App version: 5.8
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 33. One-star (random_state=42) — `12794841521`

- Author: trisleee
- Rating: 1
- Date: 2025-06-19T19:27:16-07:00
- Title: Spam
- Content (first 250 characters): Sáng nay trong vòng 1h tôi nhận 7 thông báo giới thiệu bạn bè từ app. Quá phiền
- App version: 5.9
- Source file(s): raw_responses/page_05_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=5
- Storefront: vn
- Structurally valid: Yes

### 34. One-star (random_state=42) — `12973916991`

- Author: khong biet dat gi
- Rating: 1
- Date: 2025-08-04T00:41:35-07:00
- Title: k có quỹ dcds
- Content (first 250 characters): số lượng quỹ giới hạn.
- App version: 6.0
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 35. One-star (random_state=42) — `13272131452`

- Author: Mit16899
- Rating: 1
- Date: 2025-10-15T20:02:59-07:00
- Title: Đen màn hình
- Content (first 250 characters): Đến giờ giao dịch, app lag ko xem được gì. Đen thui.
- App version: 6.1
- Source file(s): raw_json/page_04.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=4
- Storefront: vn
- Structurally valid: Yes

### 36. One-star (random_state=42) — `11800367652`

- Author: khúc sơn tùng
- Rating: 1
- Date: 2024-10-05T08:00:43-07:00
- Title: Tự động thoát
- Content (first 250 characters): Giờ cứ vào là văng ra
- App version: 5.8
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 37. One-star (random_state=42) — `11871881939`

- Author: Q-Mai
- Rating: 1
- Date: 2024-10-24T22:01:22-07:00
- Title: Ứng dụng ngu si
- Content (first 250 characters): Tổng đài hết sức coi thường khách hàng khi lôi Ai ra hỗ trợ khách hàng
- App version: 5.8.2
- Source file(s): raw_responses/page_07_mostHelpful.json
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|json\|mostHelpful\|page=7
- Storefront: vn
- Structurally valid: Yes

### 38. Five-star (random_state=42) — `12780083348`

- Author: annyahuong
- Rating: 5
- Date: 2025-06-15T23:50:06-07:00
- Title: App
- Content (first 250 characters): App có nhiều tính năng hữu ích
- App version: 5.9
- Source file(s): raw_responses/page_05_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=5
- Storefront: vn
- Structurally valid: Yes

### 39. Five-star (random_state=42) — `11739674478`

- Author: Song Lam 2012
- Rating: 5
- Date: 2024-09-18T20:41:33-07:00
- Title: Good
- Content (first 250 characters): Good
- App version: 5.7
- Source file(s): raw_json/page_08.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=8
- Storefront: vn
- Structurally valid: Yes

### 40. Five-star (random_state=42) — `11736944054`

- Author: 105CD11121
- Rating: 5
- Date: 2024-09-18T03:31:29-07:00
- Title: 105CD11121 đánh giá app
- Content (first 250 characters): 105CD11121 tôi thích bảng giá
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 41. Five-star (random_state=42) — `12722683974`

- Author: Fat fit shark
- Rating: 5
- Date: 2025-06-01T02:05:15-07:00
- Title: Xứng đáng app đầu tu số 1 VN
- Content (first 250 characters): TCInvest mang đến một môi trường làm việc năng động, không ngừng phát triển, nơi những ý tưởng đột phá luôn được khuyến khích và triển khai nhanh chóng. Đội ngũ tại đây luôn nỗ lực sáng tạo, mang đến trải nghiệm tuyệt vời cho khách hàng, xứng đáng là…
- App version: 5.9
- Source file(s): raw_responses/page_05_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=5
- Storefront: vn
- Structurally valid: Yes

### 42. Five-star (random_state=42) — `11737009269`

- Author: itnguyen
- Rating: 5
- Date: 2024-09-18T03:58:00-07:00
- Title: 105CA60279
- Content (first 250 characters): Tuyệt vời. rất mượt
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 43. Five-star (random_state=42) — `11736888952`

- Author: Speculator688
- Rating: 5
- Date: 2024-09-18T03:07:55-07:00
- Title: 105CHNQ688
- Content (first 250 characters): 105CHNQ688 ↵ Bảng giá mượt mà, nhiều công cụ hữu ích để phục vụ nhu cầu của nhà đầu tư.
- App version: 5.7
- Source file(s): raw_responses/page_10_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=10
- Storefront: vn
- Structurally valid: Yes

### 44. Five-star (random_state=42) — `11739343587`

- Author: MeTiNi86
- Rating: 5
- Date: 2024-09-18T18:12:44-07:00
- Title: Rất hài lòng
- Content (first 250 characters): 105CTINI86 tôi thích TCBS
- App version: 5.7
- Source file(s): raw_json/page_08.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=8
- Storefront: vn
- Structurally valid: Yes

### 45. Five-star (random_state=42) — `11739853644`

- Author: dkdjcjkfnvevd
- Rating: 5
- Date: 2024-09-18T22:12:05-07:00
- Title: 105CG88661 tôi thích bảng giá
- Content (first 250 characters): 105CG88661 tôi thích bảng giá
- App version: 5.7
- Source file(s): raw_json/page_08.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=8
- Storefront: vn
- Structurally valid: Yes

### 46. Five-star (random_state=42) — `12733793429`

- Author: Hiihahaahoho
- Rating: 5
- Date: 2025-06-03T22:58:44-07:00
- Title: Hiihaha
- Content (first 250 characters): App tuyệt vời ông mặt trời, xịn xò con bò cười!!!
- App version: 5.9
- Source file(s): raw_responses/page_05_mostHelpful.xml
- Endpoint/sort group(s): unprefixed_legacy_raw_responses\|xml\|mostHelpful\|page=5
- Storefront: vn
- Structurally valid: Yes

### 47. Five-star (random_state=42) — `11739448167`

- Author: zynnnn🫦
- Rating: 5
- Date: 2024-09-18T18:58:26-07:00
- Title: rate app
- Content (first 250 characters): cx okla nha:))) đầu tư an toàn lành mạnh he
- App version: 5.7
- Source file(s): raw_json/page_08.json
- Endpoint/sort group(s): legacy_raw_json\|json\|mostrecent\|page=8
- Storefront: vn
- Structurally valid: Yes

## 11. Implications for Canonical Dataset

This audit does not merge or rebuild the canonical dataset. It classifies evidence as follows:

| Evidence category | Count | Objective rule |
|---|---:|---|
| A. Strong candidates for inclusion | 230 | Structurally valid TCInvest review evidence with no exact-content, same-author high-similarity, or multi-state signal detected. |
| B. Likely technical/collection artifacts | 0 | Missing required structure, invalid rating/date, or no saved evidence tying the record to App ID `1037255487`. |
| C. Ambiguous — needs human decision | 8 | Structurally valid, but has an exact-content duplicate, same-author high-similarity signal, or multiple saved states. |

The fact that a record came from a legacy run, retry, alternate page, sort mode, JSON, or XML is not by itself evidence that the review is invalid. A human scope decision should determine whether the canonical dataset represents one specific completed collector run (209 IDs) or the union of all structurally valid saved TCInvest evidence, with an explicit policy for duplicate/version signals.

No raw or canonical input was changed by this audit.
