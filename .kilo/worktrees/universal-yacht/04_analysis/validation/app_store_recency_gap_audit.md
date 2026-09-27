# App Store Recency Gap Audit

## Audit question

Why does the retrievable App Store dataset stop at 29 April 2026 despite collection in September 2026?

## Existing canonical

- File: `01_data/raw/app_store/2026-09-22_app_store_raw_expanded.csv`
- Rows: 447
- Unique review IDs: 447
- Date range: 2024-09-18T10:02:07+00:00 to 2026-04-29T02:36:56+00:00
- Latest review: `14007818169` at 2026-04-29T02:36:56+00:00

## Collector review

- The existing collector defines both `vn` and `us` storefronts; this diagnostic used `vn` only.
- It tests `default`, `mostrecent`, and `mostHelpful` routes for top-level endpoints and fixed pages 1–10.
- It requests both JSON and XML, producing 66 combinations per storefront.
- Pagination is a fixed page sweep, not continuation-driven pagination. It does not stop early when a page is empty.
- There is no date filter. After parsing, it deduplicates only by `review_id` and sorts by parsed date.
- JSON/XML parsers skip non-review feed entries without `im:rating`; no valid rated review is intentionally excluded by date/schema logic observed in the code.
- Each request permits up to three attempts. HTTP failures receive a short retry; network/JSON failures use exponential backoff. Multiple formats and sort routes function as coverage fallbacks, but endpoint responses remain cache-dependent.

## Saved raw evidence before this diagnostic

- Files scanned: 219
- Parsed occurrences: 750
- Unique IDs: 447
- Newest saved-raw date: 2026-04-29T02:36:56+00:00
- Newest review ID: `14007818169`
- Source files: `raw_responses/page_02_default.json`, `raw_responses/vn_page_02_default.json`
- Inferred endpoint metadata: VN storefront, JSON format, `default` sort route, page 2.
- Saved-raw records from 30 April 2026 VN onward: 0

## Methods tested

- Storefront: VN only
- Requests: 67 (66 RSS JSON/XML combinations plus one public HTML page)
- HTTP status distribution: {'200': 67}
- Review-bearing responses: 39
- HTTP 200 responses with zero parsed reviews: 28
- Diagnostic parser failures: 0

| Response file | Format | Sort | Page | HTTP | Content type | Bytes | Parsed | Unique IDs | New IDs | From 30 Apr | Newest |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---|
| `vn_top_default.json` | json | default | top | 200 | text/javascript; charset=UTF-8 | 833 | 0 | 0 | 0 | 0 | — |
| `vn_top_default.xml` | xml | default | top | 200 | application/xml | 819 | 0 | 0 | 0 | 0 | — |
| `vn_top_mostrecent.json` | json | mostrecent | top | 200 | text/javascript; charset=UTF-8 | 40307 | 50 | 50 | 50 | 34 | 2026-09-14T07:44:28+00:00 |
| `vn_top_mostrecent.xml` | xml | mostrecent | top | 200 | application/xml | 855 | 0 | 0 | 0 | 0 | — |
| `vn_top_mostHelpful.json` | json | mostHelpful | top | 200 | text/javascript; charset=UTF-8 | 40802 | 50 | 50 | 50 | 34 | 2026-09-14T07:44:28+00:00 |
| `vn_top_mostHelpful.xml` | xml | mostHelpful | top | 200 | application/xml | 116456 | 50 | 50 | 50 | 34 | 2026-09-14T07:44:28+00:00 |
| `vn_page_01_default.json` | json | default | 1 | 200 | text/javascript; charset=UTF-8 | 40241 | 50 | 50 | 50 | 34 | 2026-09-14T07:44:28+00:00 |
| `vn_page_01_default.xml` | xml | default | 1 | 200 | application/xml | 833 | 0 | 0 | 0 | 0 | — |
| `vn_page_01_mostrecent.json` | json | mostrecent | 1 | 200 | text/javascript; charset=UTF-8 | 883 | 0 | 0 | 0 | 0 | — |
| `vn_page_01_mostrecent.xml` | xml | mostrecent | 1 | 200 | application/xml | 869 | 0 | 0 | 0 | 0 | — |
| `vn_page_01_mostHelpful.json` | json | mostHelpful | 1 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_01_mostHelpful.xml` | xml | mostHelpful | 1 | 200 | application/xml | 116498 | 50 | 50 | 50 | 34 | 2026-09-14T07:44:28+00:00 |
| `vn_page_02_default.json` | json | default | 2 | 200 | text/javascript; charset=UTF-8 | 40403 | 50 | 50 | 0 | 0 | 2026-04-29T02:36:56+00:00 |
| `vn_page_02_default.xml` | xml | default | 2 | 200 | application/xml | 833 | 0 | 0 | 0 | 0 | — |
| `vn_page_02_mostrecent.json` | json | mostrecent | 2 | 200 | text/javascript; charset=UTF-8 | 40511 | 50 | 50 | 0 | 0 | 2026-04-29T02:36:56+00:00 |
| `vn_page_02_mostrecent.xml` | xml | mostrecent | 2 | 200 | application/xml | 115829 | 50 | 50 | 0 | 0 | 2026-04-29T02:36:56+00:00 |
| `vn_page_02_mostHelpful.json` | json | mostHelpful | 2 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_02_mostHelpful.xml` | xml | mostHelpful | 2 | 200 | application/xml | 871 | 0 | 0 | 0 | 0 | — |
| `vn_page_03_default.json` | json | default | 3 | 200 | text/javascript; charset=UTF-8 | 40595 | 50 | 50 | 0 | 0 | 2026-02-04T06:30:34+00:00 |
| `vn_page_03_default.xml` | xml | default | 3 | 200 | application/xml | 116335 | 50 | 50 | 0 | 0 | 2026-02-04T06:30:34+00:00 |
| `vn_page_03_mostrecent.json` | json | mostrecent | 3 | 200 | text/javascript; charset=UTF-8 | 40703 | 50 | 50 | 0 | 0 | 2026-02-04T06:30:34+00:00 |
| `vn_page_03_mostrecent.xml` | xml | mostrecent | 3 | 200 | application/xml | 869 | 0 | 0 | 0 | 0 | — |
| `vn_page_03_mostHelpful.json` | json | mostHelpful | 3 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_03_mostHelpful.xml` | xml | mostHelpful | 3 | 200 | application/xml | 871 | 0 | 0 | 0 | 0 | — |
| `vn_page_04_default.json` | json | default | 4 | 200 | text/javascript; charset=UTF-8 | 38710 | 50 | 50 | 0 | 0 | 2025-11-05T03:39:52+00:00 |
| `vn_page_04_default.xml` | xml | default | 4 | 200 | application/xml | 112459 | 50 | 50 | 0 | 0 | 2025-11-05T03:39:52+00:00 |
| `vn_page_04_mostrecent.json` | json | mostrecent | 4 | 200 | text/javascript; charset=UTF-8 | 883 | 0 | 0 | 0 | 0 | — |
| `vn_page_04_mostrecent.xml` | xml | mostrecent | 4 | 200 | application/xml | 112567 | 50 | 50 | 0 | 0 | 2025-11-05T03:39:52+00:00 |
| `vn_page_04_mostHelpful.json` | json | mostHelpful | 4 | 200 | text/javascript; charset=UTF-8 | 39329 | 50 | 50 | 0 | 0 | 2025-11-12T12:53:27+00:00 |
| `vn_page_04_mostHelpful.xml` | xml | mostHelpful | 4 | 200 | application/xml | 113578 | 50 | 50 | 0 | 0 | 2025-11-12T12:53:27+00:00 |
| `vn_page_05_default.json` | json | default | 5 | 200 | text/javascript; charset=UTF-8 | 847 | 0 | 0 | 0 | 0 | — |
| `vn_page_05_default.xml` | xml | default | 5 | 200 | application/xml | 833 | 0 | 0 | 0 | 0 | — |
| `vn_page_05_mostrecent.json` | json | mostrecent | 5 | 200 | text/javascript; charset=UTF-8 | 37542 | 50 | 50 | 6 | 0 | 2025-07-17T08:11:52+00:00 |
| `vn_page_05_mostrecent.xml` | xml | mostrecent | 5 | 200 | application/xml | 869 | 0 | 0 | 0 | 0 | — |
| `vn_page_05_mostHelpful.json` | json | mostHelpful | 5 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_05_mostHelpful.xml` | xml | mostHelpful | 5 | 200 | application/xml | 110221 | 50 | 50 | 0 | 0 | 2025-07-31T00:56:38+00:00 |
| `vn_page_06_default.json` | json | default | 6 | 200 | text/javascript; charset=UTF-8 | 37723 | 50 | 50 | 0 | 0 | 2025-05-01T03:08:57+00:00 |
| `vn_page_06_default.xml` | xml | default | 6 | 200 | application/xml | 833 | 0 | 0 | 0 | 0 | — |
| `vn_page_06_mostrecent.json` | json | mostrecent | 6 | 200 | text/javascript; charset=UTF-8 | 883 | 0 | 0 | 0 | 0 | — |
| `vn_page_06_mostrecent.xml` | xml | mostrecent | 6 | 200 | application/xml | 869 | 0 | 0 | 0 | 0 | — |
| `vn_page_06_mostHelpful.json` | json | mostHelpful | 6 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_06_mostHelpful.xml` | xml | mostHelpful | 6 | 200 | application/xml | 110110 | 50 | 50 | 6 | 0 | 2025-05-22T06:02:22+00:00 |
| `vn_page_07_default.json` | json | default | 7 | 200 | text/javascript; charset=UTF-8 | 36049 | 50 | 50 | 6 | 0 | 2024-12-20T11:30:44+00:00 |
| `vn_page_07_default.xml` | xml | default | 7 | 200 | application/xml | 107209 | 50 | 50 | 6 | 0 | 2024-12-20T11:30:44+00:00 |
| `vn_page_07_mostrecent.json` | json | mostrecent | 7 | 200 | text/javascript; charset=UTF-8 | 883 | 0 | 0 | 0 | 0 | — |
| `vn_page_07_mostrecent.xml` | xml | mostrecent | 7 | 200 | application/xml | 107317 | 50 | 50 | 6 | 0 | 2024-12-20T11:30:44+00:00 |
| `vn_page_07_mostHelpful.json` | json | mostHelpful | 7 | 200 | text/javascript; charset=UTF-8 | 885 | 0 | 0 | 0 | 0 | — |
| `vn_page_07_mostHelpful.xml` | xml | mostHelpful | 7 | 200 | application/xml | 108625 | 50 | 50 | 0 | 0 | 2025-01-10T07:05:02+00:00 |
| `vn_page_08_default.json` | json | default | 8 | 200 | text/javascript; charset=UTF-8 | 34545 | 50 | 50 | 0 | 0 | 2024-09-19T13:11:20+00:00 |
| `vn_page_08_default.xml` | xml | default | 8 | 200 | application/xml | 833 | 0 | 0 | 0 | 0 | — |
| `vn_page_08_mostrecent.json` | json | mostrecent | 8 | 200 | text/javascript; charset=UTF-8 | 34653 | 50 | 50 | 0 | 0 | 2024-09-19T13:11:20+00:00 |
| `vn_page_08_mostrecent.xml` | xml | mostrecent | 8 | 200 | application/xml | 869 | 0 | 0 | 0 | 0 | — |
| `vn_page_08_mostHelpful.json` | json | mostHelpful | 8 | 200 | text/javascript; charset=UTF-8 | 34709 | 50 | 50 | 2 | 0 | 2024-09-19T16:10:25+00:00 |
| `vn_page_08_mostHelpful.xml` | xml | mostHelpful | 8 | 200 | application/xml | 104290 | 50 | 50 | 2 | 0 | 2024-09-19T16:10:25+00:00 |
| `vn_page_09_default.json` | json | default | 9 | 200 | text/javascript; charset=UTF-8 | 33720 | 50 | 50 | 0 | 0 | 2024-09-19T00:31:29+00:00 |
| `vn_page_09_default.xml` | xml | default | 9 | 200 | application/xml | 102493 | 50 | 50 | 0 | 0 | 2024-09-19T00:31:29+00:00 |
| `vn_page_09_mostrecent.json` | json | mostrecent | 9 | 200 | text/javascript; charset=UTF-8 | 33828 | 50 | 50 | 0 | 0 | 2024-09-19T00:31:29+00:00 |
| `vn_page_09_mostrecent.xml` | xml | mostrecent | 9 | 200 | application/xml | 102601 | 50 | 50 | 0 | 0 | 2024-09-19T00:31:29+00:00 |
| `vn_page_09_mostHelpful.json` | json | mostHelpful | 9 | 200 | text/javascript; charset=UTF-8 | 33980 | 50 | 50 | 0 | 0 | 2024-09-18T23:36:19+00:00 |
| `vn_page_09_mostHelpful.xml` | xml | mostHelpful | 9 | 200 | application/xml | 102899 | 50 | 50 | 0 | 0 | 2024-09-18T23:36:19+00:00 |
| `vn_page_10_default.json` | json | default | 10 | 200 | text/javascript; charset=UTF-8 | 33778 | 50 | 50 | 7 | 0 | 2024-09-18T12:04:39+00:00 |
| `vn_page_10_default.xml` | xml | default | 10 | 200 | application/xml | 835 | 0 | 0 | 0 | 0 | — |
| `vn_page_10_mostrecent.json` | json | mostrecent | 10 | 200 | text/javascript; charset=UTF-8 | 33886 | 50 | 50 | 7 | 0 | 2024-09-18T12:04:39+00:00 |
| `vn_page_10_mostrecent.xml` | xml | mostrecent | 10 | 200 | application/xml | 102660 | 50 | 50 | 7 | 0 | 2024-09-18T12:04:39+00:00 |
| `vn_page_10_mostHelpful.json` | json | mostHelpful | 10 | 200 | text/javascript; charset=UTF-8 | 34435 | 50 | 50 | 0 | 0 | 2024-09-18T11:23:08+00:00 |
| `vn_page_10_mostHelpful.xml` | xml | mostHelpful | 10 | 200 | application/xml | 873 | 0 | 0 | 0 | 0 | — |
| `public_reviews_page.html` | html | public selection | see-all | 200 | text/html | 249040 | 10 | 10 | 10 | 3 | 2026-07-24T04:57:36+00:00 |

## Public App Store page check

- URL: `https://apps.apple.com/vn/app/tcinvest/id1037255487?see-all=reviews`
- HTTP status: 200
- Content type: text/html
- Response size: 249040 bytes
- Parsed ProductReview objects exposed in HTML: 10
- ProductReview IDs after 29 April window: 3
- Newest public-page ProductReview: 2026-07-24T04:57:36+00:00

The public HTML exposes a selective set of review objects, including reviews after 29 April 2026. It is not an exhaustive or reliably most-recent listing, so absence from the page cannot establish absence from the App Store.

## Current retrievable coverage

- Parsed review occurrences, including the public-page copies: 1910
- Unique diagnostic review IDs: 522
- Oldest: 2023-04-14T03:22:33+00:00
- Newest: 2026-09-14T07:44:28+00:00
- Overlap with canonical: 447
- New IDs vs canonical: 75
- IDs later than the canonical latest timestamp: 50
- New-ID date range: 2023-04-14T03:22:33+00:00 to 2026-09-14T07:44:28+00:00

## Reviews after 29 April 2026

- Count from 30 April 2026 VN onward: 34
- Date range: 2026-05-06T04:15:56+00:00 to 2026-09-14T07:44:28+00:00
- All are new vs the current canonical: True

| review_id | Date (UTC) | Rating | Title | Source endpoints |
|---|---|---:|---|---|
| 14033216115 | 2026-05-06T04:15:56+00:00 | 1 | App ngày càng tệ! | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14034900836 | 2026-05-06T15:43:12+00:00 | 5 | Tuyệt vời | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14040031598 | 2026-05-08T02:14:26+00:00 | 1 | 1 vấn đề gặp hoài mà ko xử lý | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14045600270 | 2026-05-09T15:32:29+00:00 | 5 | lỗi rồi | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14051715882 | 2026-05-11T07:18:29+00:00 | 1 | Quá tệ cho 1 sàn do ngân hàng đầu ngành vận hành | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14141897416 | 2026-06-04T06:40:04+00:00 | 5 | Good | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14142865973 | 2026-06-04T13:07:36+00:00 | 1 | Ai như tôi không nạo tiền vào không lâu tiền bay hết sạch | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|public_html\|see-all-reviews;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14147186413 | 2026-06-05T15:28:37+00:00 | 1 | Ứng dụng hệ thống như một tên bịp bợm. | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14149839961 | 2026-06-06T08:12:27+00:00 | 1 | Cái ipower lúc ẩn lúc hiện như ma | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14162695649 | 2026-06-09T15:53:51+00:00 | 2 | Số liệu sai | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14223394760 | 2026-06-25T05:43:41+00:00 | 1 | App tệ | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14280577109 | 2026-07-09T04:08:14+00:00 | 3 | Ok | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14296658625 | 2026-07-13T04:19:17+00:00 | 1 | App rất thường bị lỗi | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14313162800 | 2026-07-17T06:45:43+00:00 | 1 | Giam Tiền cổ tức | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|public_html\|see-all-reviews;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14341132155 | 2026-07-24T04:57:36+00:00 | 5 | Dùng thích | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|public_html\|see-all-reviews;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14352633073 | 2026-07-27T02:34:31+00:00 | 1 | Không có nhân viên hỗ trợ | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14352635121 | 2026-07-27T02:35:18+00:00 | 1 | App lỗi rất nhiều lần | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14354074084 | 2026-07-27T12:11:15+00:00 | 1 | Bảo mật ngou như con bò | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14381104681 | 2026-08-03T03:15:17+00:00 | 1 | Ko rút tiền được, bị giam tiền | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14409630266 | 2026-08-10T07:58:38+00:00 | 1 | Tại sao lại giam tiền 2 hợp đồng, trong khi đã đóng vị thế trong cùng 1 ngày | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14414751396 | 2026-08-11T14:10:45+00:00 | 1 | App như cặc | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14418152911 | 2026-08-12T10:46:04+00:00 | 1 | Quá phiền hà | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14420925724 | 2026-08-13T02:12:57+00:00 | 2 | Giao diện kém | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14425846977 | 2026-08-14T08:14:42+00:00 | 1 | Làm ăn ko kỹ càng, cẩu thả | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14439296592 | 2026-08-17T15:52:20+00:00 | 1 | Cách xác thực sự quá ngu | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14445501649 | 2026-08-19T05:09:21+00:00 | 1 | UI UX lởm quá | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14465018475 | 2026-08-24T03:57:52+00:00 | 1 | App lỗi quá nhiều | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14465859621 | 2026-08-24T10:08:22+00:00 | 1 | Giao diện rối khó sử dụng, CSKH kém, không thể gọi được NV CSKH | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14467591535 | 2026-08-24T19:29:06+00:00 | 5 | NGUYEN VAN PHUONG | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14468902446 | 2026-08-25T04:00:51+00:00 | 1 | Nghi vấn bán dữ liệu cho lái | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14504211053 | 2026-09-03T03:32:43+00:00 | 3 | Quá chậm | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14520054584 | 2026-09-07T04:07:12+00:00 | 2 | Khá tệ | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14520064997 | 2026-09-07T04:11:54+00:00 | 1 | Tần suất bị lỗi mục tài sản quá nhiều | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |
| 14548034358 | 2026-09-14T07:44:28+00:00 | 1 | Liên tục lỗi không thể truy cập | vn\|json\|default\|page=1;vn\|json\|mostHelpful\|page=top;vn\|json\|mostrecent\|page=top;vn\|xml\|mostHelpful\|page=1;vn\|xml\|mostHelpful\|page=top |

## Possible explanation

### Evidence

- The same 66 VN RSS method combinations returned HTTP 200 for every request, but only 38 RSS responses contained review entries; 28 were parseable empty feeds.
- Different format/sort/page routes returned different overlapping slices.
- The fresh diagnostic recovered all 447 canonical IDs plus 75 additional IDs.
- Thirty-four retrievable IDs fall from 30 April 2026 VN onward, and the newest is dated 14 September 2026.
- The public HTML independently exposes three post-cutoff ProductReview objects, all also found in the RSS diagnostic.

### Interpretation

This is case A with case-C behavior: reviews after 29 April 2026 are retrievable now, so the earlier saved response set did not capture all recent reviews. The most likely mechanism is unstable/edge-cached public endpoint coverage across page, sort, and JSON/XML combinations rather than a date filter or parser cutoff in the collector.

### Unknown

- The diagnostic cannot determine whether every App Store review is exposed by these public methods.
- It cannot establish whether additional reviews after 14 September 2026 exist but were not retrievable.
- Public endpoint responses may change on another run even with identical URLs.

## Limitation

This audit does not claim that the diagnostic universe is complete and does not claim that TCInvest has no reviews outside the retrieved ranges. It only establishes what was retrievable through the public methods tested at this run.

## Recommended treatment for analysis

- Do not silently merge the 75 candidates into the canonical dataset during this diagnostic task.
- The 447-row canonical is safe to keep unchanged only if tonight’s analysis is explicitly frozen to the prior retrievable snapshot and its end date of 29 April 2026 is disclosed.
- It is not suitable for claims about App Store recency through September 2026.
- Before broader time coverage is analyzed, review the 75 candidate IDs, rerun a bounded repeatability check, then rebuild/version a new canonical dataset under an approved scope.
- If analysis must proceed tonight without a rebuild, use an App Store analysis cutoff no later than 29 April 2026 and treat Google Play separately rather than implying matched recency coverage.
