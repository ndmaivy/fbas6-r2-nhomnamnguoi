# App Store Candidate Validation

## Scope

- Prior canonical: 447 unique IDs
- Candidates checked: 75
- Diagnostic raw files: 67
- Parser failures: 0

## Validation rules

- Numeric unique `review_id` not present in the old canonical
- Normal rated review entry traceable to an existing diagnostic raw response
- Parseable date, rating in 1–5, and non-empty content
- VN storefront evidence tied to TCInvest App ID `1037255487`
- No substantive content/title/rating/date/author/version conflict across JSON, XML, sort routes, or public-page copies

## Results

- VALID: 75
- AMBIGUOUS: 0
- INVALID: 0
- Valid after 29 April 2026 window: 34
- Valid before or at the cutoff: 41
- Valid inside the prior canonical exact date range: 19
- Candidate date range: 2023-04-14T03:22:33+00:00 to 2026-09-14T07:44:28+00:00
- Rating distribution: {'1': 43, '2': 6, '3': 5, '4': 1, '5': 20}

## Duplicate and conflict checks

- Duplicate candidate IDs already in old canonical: 0
- Candidate IDs sharing exact content with another ID: 4
- Candidate IDs sharing an author with another ID: 2
- Candidate IDs sharing exact content/date/rating with another ID: 0
- Candidate IDs with substantive cross-source states: 0

Exact text duplication does not invalidate a record when `review_id` differs. No candidate was removed on content similarity.

Signal details:

- Exact content `105CTOIYEUVN`: candidate IDs `11737075225`, `11767116568`, and `11777958926`; other saved IDs also use this text.
- Exact content `Tuyệt`: candidate ID `11741247423` and existing ID `11739494710`.
- Same author `tuan9a9a`: candidate IDs `14149839961` and `14381104681`. Their IDs and review records remain distinct.
- No candidate pair shared the full content/date/rating tuple under different IDs.
- None of these signals caused content-based deduplication.

## Endpoint coverage implication

19 validated candidates fall inside the prior canonical date range yet were absent from the 447-row snapshot. This directly demonstrates that the previous canonical did not capture complete public-endpoint coverage even within its own temporal range. It does not establish complete lifetime coverage for v2.

## Per-candidate status

| review_id | Date | Rating | Status | Reason |
|---|---|---:|---|---|
| 14548034358 | 2026-09-14T07:44:28+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14520064997 | 2026-09-07T04:11:54+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14520054584 | 2026-09-07T04:07:12+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14504211053 | 2026-09-03T03:32:43+00:00 | 3 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14468902446 | 2026-08-25T04:00:51+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14467591535 | 2026-08-24T19:29:06+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14465859621 | 2026-08-24T10:08:22+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14465018475 | 2026-08-24T03:57:52+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14445501649 | 2026-08-19T05:09:21+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14439296592 | 2026-08-17T15:52:20+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14425846977 | 2026-08-14T08:14:42+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14420925724 | 2026-08-13T02:12:57+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14418152911 | 2026-08-12T10:46:04+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14414751396 | 2026-08-11T14:10:45+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14409630266 | 2026-08-10T07:58:38+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14381104681 | 2026-08-03T03:15:17+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14354074084 | 2026-07-27T12:11:15+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14352635121 | 2026-07-27T02:35:18+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14352633073 | 2026-07-27T02:34:31+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14341132155 | 2026-07-24T04:57:36+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 6 raw occurrence(s); no substantive state conflict. |
| 14313162800 | 2026-07-17T06:45:43+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 6 raw occurrence(s); no substantive state conflict. |
| 14296658625 | 2026-07-13T04:19:17+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14280577109 | 2026-07-09T04:08:14+00:00 | 3 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14223394760 | 2026-06-25T05:43:41+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14162695649 | 2026-06-09T15:53:51+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14149839961 | 2026-06-06T08:12:27+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14147186413 | 2026-06-05T15:28:37+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14142865973 | 2026-06-04T13:07:36+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 6 raw occurrence(s); no substantive state conflict. |
| 14141897416 | 2026-06-04T06:40:04+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14051715882 | 2026-05-11T07:18:29+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14045600270 | 2026-05-09T15:32:29+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14040031598 | 2026-05-08T02:14:26+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14034900836 | 2026-05-06T15:43:12+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14033216115 | 2026-05-06T04:15:56+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14009628721 | 2026-04-29T15:34:18+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14008131020 | 2026-04-29T05:12:10+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007852344 | 2026-04-29T02:52:45+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007849446 | 2026-04-29T02:51:24+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007848369 | 2026-04-29T02:50:53+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007846536 | 2026-04-29T02:50:03+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007842869 | 2026-04-29T02:48:22+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007840671 | 2026-04-29T02:47:21+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007834537 | 2026-04-29T02:44:28+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 14007830108 | 2026-04-29T02:42:27+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007825034 | 2026-04-29T02:40:04+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007825045 | 2026-04-29T02:40:04+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007823992 | 2026-04-29T02:39:35+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007820033 | 2026-04-29T02:37:47+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007820003 | 2026-04-29T02:37:46+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 14007819853 | 2026-04-29T02:37:42+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12683550678 | 2025-05-22T06:02:22+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12676479614 | 2025-05-20T09:12:12+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12676449035 | 2025-05-20T08:57:57+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12660963384 | 2025-05-16T03:23:39+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12617407260 | 2025-05-04T06:47:17+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 12609904288 | 2025-05-02T08:34:11+00:00 | 2 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 2 raw occurrence(s); no substantive state conflict. |
| 11839386523 | 2024-10-16T07:35:14+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 7 raw occurrence(s); no substantive state conflict. |
| 11777958926 | 2024-09-29T14:19:44+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11767116568 | 2024-09-26T15:53:53+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11741550112 | 2024-09-19T16:10:25+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 11741247423 | 2024-09-19T14:38:14+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 5 raw occurrence(s); no substantive state conflict. |
| 11741201798 | 2024-09-19T14:24:33+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11737096946 | 2024-09-18T11:30:57+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11737083900 | 2024-09-18T11:26:09+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11737075225 | 2024-09-18T11:22:58+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11736971959 | 2024-09-18T10:42:57+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11736926631 | 2024-09-18T10:24:09+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11736923323 | 2024-09-18T10:22:45+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11736913880 | 2024-09-18T10:18:41+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 3 raw occurrence(s); no substantive state conflict. |
| 11708342893 | 2024-09-10T07:01:09+00:00 | 1 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |
| 11124085882 | 2024-04-05T12:18:45+00:00 | 3 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |
| 10383443236 | 2023-09-19T05:03:19+00:00 | 5 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |
| 10217332140 | 2023-08-04T03:54:21+00:00 | 3 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |
| 10191157286 | 2023-07-28T10:58:35+00:00 | 4 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |
| 9819441432 | 2023-04-14T03:22:33+00:00 | 3 | VALID | Valid unique review_id; parsed normal rated review; valid date/rating/content; VN evidence targets App ID 1037255487; traced to 4 raw occurrence(s); no substantive state conflict. |

## Decision

All 75 candidates passed validation, so a new versioned canonical was created. The 447-row canonical remains unchanged as provenance/history.
