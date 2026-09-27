# Phase C — pain-point codebook v1 (candidate; not frozen)

## Scope and status

This is a **coding proposal**, derived from the 100 AI-assisted reviews and 146 atomic incidents in `../phase-b/`. `taxonomy_v1_candidate.csv` lists 15 proposed problem families; `subtypes_v1_candidate.csv` lists 29 proposed subtypes keyed to those families. Seven families retain Phase B's `SUPPORTED_RECURRING` status **within this deliberately selected sample**; the remainder and all subtypes are provisional. Neither these counts nor the label names establish prevalence among the 736 reviews or all TCInvest customers. No independent human coder has validated the labels. Do not use this as a frozen prompt for full-dataset classification yet.

## What is being coded

A pain point is an **experience problem**, not a broad journey/topic: _user goal + context + observed obstacle + consequence + supporting quote_. An incident can be a failure, friction, confusion, unmet need, feature request, praise, other or unclear. Keep `incident_type` distinct from `pain_point_family`: a positive mention of low fees is **not** a pricing complaint. Code incident-by-incident, then derive review-level multi-labels from **distinct** incidents; one review may have zero incidents. Use `(source, review_id)` as the key and copy `evidence_span` verbatim from title or raw text.

For each specific incident choose at most **one primary family** and optionally one secondary family only if the quoted text also describes an independently observable second problem. Do not infer an underlying cause (lag → server fault), financial loss, intent, spam or customer identity. Preserve `NONE` (only praise/no problem), `UNCLEAR` (insufficient evidence) and `OTHER_NEW_THEME` (specific problem not covered) as **coding outcomes**, never as counted pain-point families. A feature request belongs in `incident_type=feature_request`, with the requested task domain as family when identifiable; if none is identifiable, route to `OTHER_NEW_THEME` and request codebook review.

`confidence=HIGH` means the quoted obstacle and task are explicit; `MEDIUM` means a plausible interpretation is required; `LOW` means alternatives remain. Rating is never a shortcut for sentiment, family or severity. The existing Phase B review `13732893373` (“Nạo tiền không và tài khoản” / “Bad”) is an **inferred** deposit complaint and remains MEDIUM confidence; it is not proof of a financial incident. Mark `manual_validity=REVIEW` (review `14467591535`) separately from pain-point coding. Keep `07616126` (“mong đợi”) as `UNCLEAR_FINAL` with zero incidents; do not manufacture a positive or negative theme.

### Hierarchy and boundaries

| Family | Candidate subtypes / placement | Status |
|---|---|---|
| `PERFORMANCE_RELIABILITY` | Lag/freezing; crash/launch/black screen | Supported in sample |
| `UX_NAVIGATION_COMPLEXITY` | Clutter/navigation; screen state; `MOBILE_TABLET_RESPONSIVENESS` candidate subtype | Supported in sample |
| `ONBOARDING_KYC` | Registration; initial identity/biometric verification; `DIGITAL_SIGNATURE_FLOW` candidate subtype **only with evidence of task context** | Supported in sample |
| `AUTHENTICATION_IOTP` | Login/session; iOTP/biometric authentication | Supported in sample |
| `TRADING_ORDER_EXECUTION` | Submit/modify/cancel/status; order-entry price/quantity context | Supported in sample |
| `DEPOSIT_WITHDRAWAL_TRANSFER` | Deposit/credit; withdrawal/transfer; bank linking and fund availability | Supported in sample |
| `CUSTOMER_SUPPORT` | Reachability/delay; answer/AI quality (`AI_SUPPORT_CONTEXT_QUALITY` candidate subtype) | Supported in sample |
| `MARKET_DATA_INFORMATION` | Price-board completeness; `MARKET_DATA_STALENESS_ACCURACY` candidate subtype | Provisional split from v0 `PRODUCT_PORTFOLIO_INFORMATION` |
| `PORTFOLIO_ACCOUNT_INFORMATION` | Balances/holdings; P&L; chart settings/persistence | Provisional split from v0 `PRODUCT_PORTFOLIO_INFORMATION` |
| `FEE_PRICING` | Transaction cost; margin/loan rates | Provisional sparse |
| `ACCOUNT_RECOVERY_PROFILE_CHANGE` | Lost-phone recovery; existing-account contact/identity changes | Provisional sparse |
| `SECURITY_ACCOUNT_PROTECTION` | Explicit protection policy/upsell concern | Provisional sparse |
| `NOTIFICATION_COMMUNICATION` | Transaction-email delivery/timing | Provisional sparse |
| `MARKET_RESEARCH_RECOMMENDATION_UTILITY` | Research usefulness/clarity | Provisional sparse |
| `EXCESSIVE_DATA_CONSUMPTION` | Concrete data use on launch/session | Provisional sparse |

The Phase B family label `PRODUCT_PORTFOLIO_INFORMATION` **must be recoded** into market data, portfolio/account information, or research utility using the incident's exact quote; do not map all 13 occurrences mechanically. `DIGITAL_SIGNATURE_FLOW`, `MOBILE_TABLET_RESPONSIVENESS`, `AI_SUPPORT_CONTEXT_QUALITY` and `MARKET_DATA_STALENESS_ACCURACY` are currently **subtype proposals**, not stable top-level families. `FEATURE_REQUEST`, `OTHER`, `UNCLEAR` and v0 `Positive / General Satisfaction` are not pain-point families.

## Family rules, hard negatives and boundary examples

All IDs below identify **Phase B** reviews; use `(source, review_id)` to locate the quoted source. Positive examples illustrate coding, not real-world frequency. Hard negatives show when a nearby label must **not** be used.

### 1. `PERFORMANCE_RELIABILITY`

- **Include:** the app lags, freezes, exits, fails to launch or goes black. Example Google Play `e24f9216-51cf-4eb1-86b7-ed37ea9d208d`: “đang dùng bt tự nhiên bị out ra, h xóa đi cài lại vẫn vậy. bó tay”.
- **Exclude / hard negative:** a phone-number update delayed for three weeks (`1b8d554a-8ac2-466c-9a62-48d2ceb8f9dc`) is account-maintenance friction, not measured app latency.
- **Boundary:** a KYC video stalls (`0965c4ed-df13-48d6-b0f0-8f5c739800da`): primary `ONBOARDING_KYC` because registration is blocked; add performance only if a distinct app-wide failure is also stated. A price board whose figures stop updating may instead be `MARKET_DATA_INFORMATION`; don't invent a backend cause.

### 2. `UX_NAVIGATION_COMPLEXITY`

- **Include:** crowded layout, unintuitive navigation, too many steps, poor sizing; example App Store `13216345199` (“rất nhiều tính năng nhưng đa số không hữu dụng…”).
- **Exclude / hard negative:** Google Play `2d0a8c38-c9a5-4339-ae6c-a5bdad354b60` (“treo đơ liên tục”) describes a freeze, not layout.
- **Boundary:** when order-entry UI hides the price and causes wrong input (`e3383658-6e3a-42cd-9016-5563a4a31347`), use `TRADING_ORDER_EXECUTION` for the order-specific harm; UX is secondary only if separate layout friction is explicit. Tablet landscape/undersized controls are a provisional UX subtype, not a new family by default.

### 3. `ONBOARDING_KYC`

- **Include:** new account registration, initial identity/face/video verification; example Google Play `0965c4ed-df13-48d6-b0f0-8f5c739800da` (“không đăng ký được”).
- **Exclude / hard negative:** App Store `13177936096` concerns updating an **existing** CCCD record, not initial onboarding.
- **Boundary:** “chụp ảnh chữ ký số … đơ” (`f93f9a8e-c094-4ceb-8268-f4ba73dbb18c`) is `DIGITAL_SIGNATURE_FLOW` candidate; its account-opening stage is **not stated**, so leave journey `OTHER/UNCLEAR` until verified rather than forcing onboarding.

### 4. `AUTHENTICATION_IOTP`

- **Include:** failed login, missing iOTP, biometric/device authentication for an existing account; example Google Play `b431f770-1878-4782-99ba-23a4eadeb8a8`: “có mỗi iotp mà nửa ngày không thấy gửi”.
- **Exclude / hard negative:** face video during first registration (`0965c4ed-df13-48d6-b0f0-8f5c739800da`) belongs to KYC.
- **Boundary:** a crash *during login* (`ade96f2c-c95d-4486-8c9b-17394d3bd7e7`) can be authentication primary and reliability secondary only with two separately described symptoms; a generic “không chạy nổi” is performance, not inferred login failure.

### 5. `TRADING_ORDER_EXECUTION`

- **Include:** cannot place/sell/cancel/modify/confirm an order; wrong order input/status/price context; example Google Play `ab2dfff3-3256-4426-bcff-90608588dd94` reports a non-matching order.
- **Exclude / hard negative:** a generic freeze (`2d0a8c38-c9a5-4339-ae6c-a5bdad354b60`) does not prove an order failure.
- **Boundary:** App Store `12092046546` lacks up-to-date price/holding context *inside order entry*: trade-flow primary; distinct price-feed staleness outside the order form belongs to `MARKET_DATA_INFORMATION`. A requested 24/7 order workflow is `feature_request` and its task domain is trading, not evidence of an executed failed order.

### 6. `DEPOSIT_WITHDRAWAL_TRANSFER`

- **Include:** uncredited deposit, unavailable funds, blocked transfer/withdrawal, failed bank linking; example Google Play `c06ce68c-7cf1-42e5-b2f7-5deb78d724b4`: “giờ thì ko rút tiền được luôn”.
- **Exclude / hard negative:** App Store `11750539058` says balances are **not displayed**; do not claim money has disappeared. Use `PORTFOLIO_ACCOUNT_INFORMATION`.
- **Boundary:** `13732893373` is inferred from a typo'd title; MEDIUM confidence and no claim of verified lost money. “Tiền TK vẫn bằng 0” after transfer (`13013318242`) supports deposit/credit friction as a user report, not confirmed bank-ledger loss.

### 7. `CUSTOMER_SUPPORT`

- **Include:** contact attempts receive no answer, delayed resolution, generic or irrelevant scripted answers; App Store `12387003343`: “Lỗi đăng nhập - gọi hỗ trợ chỉ có tổng đài tự động”.
- **Exclude / hard negative:** missing iOTP (`b431f770-1878-4782-99ba-23a4eadeb8a8`) without any reported support attempt.
- **Boundary:** same review may have a login failure and a separate unresolved support interaction (`12387003343`): two incidents, authentication and support. AI-chat that ignores selected ticker (`13691875675`) is a candidate support/context subtype only if the use is assistance; if it is research advice, flag for adjudication.

### 8. `MARKET_DATA_INFORMATION` — provisional split

- **Include:** quote/price-board information missing or stale; App Store `12901670031`: “giá thị trường cập nhật chậm, thiếu chính xác, hay cần phải làm mới”.
- **Exclude / hard negative:** missing bank balances in the “all accounts” view (`11750539058`) concern account information.
- **Boundary:** a *frozen UI* showing unchanged prices may be performance, market-data freshness, or both; record the user's observed effect (“số liệu ... không dịch chuyển”), not a feed root cause. Missing price steps in an order form can be trading context, with market data secondary only when independently stated.

### 9. `PORTFOLIO_ACCOUNT_INFORMATION` — provisional split

- **Include:** portfolio P&L, holdings/account balances or chart indicators not shown or not retained; App Store `11750539058` (“không hiện thị thông số tiền trong 2 TK ngân hàng”).
- **Exclude / hard negative:** App Store `12901670031` describing intraday quote freshness is market data, not P&L.
- **Boundary:** “số dư hiện chập chờn” (`1eb01879-8d2e-41ce-a4b4-1dfd9c6ffd53`) is a display issue; do not infer failed transfers. If the record explicitly says a deposit did not credit, use money movement.

### 10. `FEE_PRICING` — provisional sparse

- **Include:** fee/margin rate causes dissatisfaction or an unmet need; Google Play `646b0a5b-3f6c-4f89-9ce4-9f174e440c38`: “Giảm thêm lãi suất vay thì tốt hơn nữa”.
- **Exclude / hard negative:** Google Play `8a6e6c41-9bfb-4a15-bbae-c2f83ead1bda` says “phí rẻ nên xài” but complains about information/portfolio tools, not the fee.
- **Boundary:** a request to reduce an existing rate can be pricing friction; a request for a brand-new capability is `feature_request`. Do not promote pricing based on five incidents: some are praise.

### 11. `ACCOUNT_RECOVERY_PROFILE_CHANGE` — provisional sparse

- **Include:** recovery after lost phone; changing phone number or CCCD on an existing account; Google Play `1b8d554a-8ac2-466c-9a62-48d2ceb8f9dc`: “đổi sdt thông tin khách hàng ... 3 tuần không xong”.
- **Exclude / hard negative:** initial biometric registration (`0965c4ed-df13-48d6-b0f0-8f5c739800da`) is KYC.
- **Boundary:** account lockout after losing a phone (`11764988478`) may be both account recovery and subsequent login/support incidents; distinguish goals rather than duplicating the same obstacle three times. CCCD update `13628052342` may have been placed under v0 KYC; re-evaluate from its existing-account context.

### 12. `SECURITY_ACCOUNT_PROTECTION` — provisional sparse

- **Include:** an explicit concern about protection policy or security-package pricing; Google Play `c6eae58a-de68-4a0d-add8-231850981783` questions a paid security prompt.
- **Exclude / hard negative:** delayed iOTP (`b431f770-1878-4782-99ba-23a4eadeb8a8`) is authentication reliability, not proof of insecure design.
- **Boundary:** keep the security-package concern as a **perception**; no evidence here proves baseline protection is absent. Zero evidence of an actual security breach.

### 13. `NOTIFICATION_COMMUNICATION` — provisional sparse

- **Include:** missing or late transaction message; App Store `12388866897`: “Thông báo dao dịch trong ngày về mail chậm. Hơn 10h chưa thấy đâu.”
- **Exclude / hard negative:** Google Play `5d89ab13-4007-48a8-8e02-6279e531d636` merely describes receipt of a daily summary, not a delay complaint.
- **Boundary:** a price board refreshing slowly belongs to market data, not email delivery. Phase B's two notification incidents include **one praise**, so this is not evidence of two independent delays.

### 14. `MARKET_RESEARCH_RECOMMENDATION_UTILITY` — provisional sparse

- **Include:** user says market analysis/recommendations are unhelpful; App Store `13446154783`: “Đội ngũ phân tích thị trường khá tệ.”
- **Exclude / hard negative:** intraday price staleness (`12901670031`) is quote data, not research quality.
- **Boundary:** a subsequent market move opposite a recommendation is **not** proof the analysis was objectively wrong. The review expresses dissatisfaction; investigate separately.

### 15. `EXCESSIVE_DATA_CONSUMPTION` — provisional sparse

- **Include:** concrete reported data consumed per app launch; App Store `12492849736`: “Mỗi mở app tốn hơn 30MB data, xài ko để ý là hết dung lượng 4g”.
- **Exclude / hard negative:** a lag/freezing report (`ab61f02f-ef5c-4420-988e-1df2def70c5f`) with no data-use figure is performance.
- **Boundary:** do not assume the amount is measured, representative or a technical cause. One incident cannot establish recurrence.

## QA gate before taxonomy freeze

1. **Adjudicate against independent human labels** on a subset not used to draft these rules; record coder ID, date, disagreements and reconciled rule. Single-reviewer AI-assisted sample is not independent agreement.
2. For each family: validate the cited positive and hard-negative review in context; include/exclude rules must yield the expected decision. Keep separate incident types for praise/unmet needs/requests.
3. Review the 10 `NEEDS_MORE_SAMPLE` themes by **complaint evidence**, not incident count alone. The Phase B 7-incident reference is a sampling heuristic, **not** a threshold for automatic promotion. Additional examples must be genuinely independent reviews and represent both platforms/time spans where feasible.
4. Resolve the broad information split and the account-maintenance/KYC and trade-context/UX boundaries. Recode the Phase B incidents that change family; retain the original Phase B tables as evidence, never overwrite them silently.
5. Freeze taxonomy and journey rules only after adjudications are accepted. Until then write `candidate` in version metadata and do not scale automated classification to all 736 reviews.
