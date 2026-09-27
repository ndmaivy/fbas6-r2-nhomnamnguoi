# Phase D — Journey Codebook v1 (candidate; not frozen)

## Scope and status

This is a **coding proposal** for the customer journey model, derived from the 146 Phase B incidents in `../phase-b/`. The journey model answers **WHERE** in the user experience the issue occurred. The pain-point family (Phase C) answers **WHAT** problem occurred. Journey and pain-point family are independent dimensions.

The candidate model has **11 journey stages**: 8 specific stages, 1 cross-journey stage, 1 catch-all, and 1 unknown. One stage (`ACCOUNT_PROFILE_MAINTENANCE`) is newly added based on Phase B evidence. No stages were merged or removed.

This draft changes no Phase B artifact or 736-row dataset. No independent human coder has validated the journey model. Do not use this as a frozen prompt for full-dataset classification yet.

## Journey stages

### ACCOUNT_OPENING_KYC

**Definition:** First-time account creation and initial identity verification for a new user.

**Typical user goals:** Open a new TCInvest account and complete identity verification.

**Include when:**
- Creating a new account
- Initial face/biometric/video verification
- Initial digital signature for account activation
- Initial CCCD submission for a new account

**Exclude when:**
- Updating an existing account profile (phone, CCCD) → ACCOUNT_PROFILE_MAINTENANCE
- Recovering access after lockout → ACCOUNT_PROFILE_MAINTENANCE
- Routine login after account exists → LOGIN_AUTHENTICATION

**Common confusion with:**
- ACCOUNT_PROFILE_MAINTENANCE — first-time setup vs. existing-account update
- LOGIN_AUTHENTICATION — initial biometric registration vs. routine login

**Decision rule:** If the account does not yet exist or is being created for the first time, use ACCOUNT_OPENING_KYC. If the account exists and the user is updating information or recovering access, use ACCOUNT_PROFILE_MAINTENANCE.

**Representative incident examples:**
- `Google_Play-0965c4ed-df13-48d6-b0f0-8f5c739800da-01`: "không xác nhận được sinh trắc học"
- `Google_Play-e7a9cf27-0878-42f7-8972-3a2542c2af3f-01`: "xác minh khuôn mặt cả nghìn lần không được"
- `App_Store-12795601247-01`: "Xét duyệt mở tk chậm chạp"

---

### ACCOUNT_PROFILE_MAINTENANCE

**Definition:** Updating or maintaining an existing account profile, including contact information changes, identity document updates, account recovery after lockout, and preference settings.

**Typical user goals:** Update personal information or recover access to an existing account.

**Include when:**
- Changing phone number on existing account
- Updating CCCD on existing account
- Recovering access after losing phone or being locked out
- Saving widget/preference settings
- Post-registration digital signature tasks

**Exclude when:**
- Initial account creation → ACCOUNT_OPENING_KYC
- Routine login → LOGIN_AUTHENTICATION

**Common confusion with:**
- ACCOUNT_OPENING_KYC — existing-account update vs. first-time setup
- LOGIN_AUTHENTICATION — recovery after lockout vs. routine login failure

**Decision rule:** If the account already exists and the user is updating information, changing settings, or recovering access, use ACCOUNT_PROFILE_MAINTENANCE. The key distinction from ACCOUNT_OPENING_KYC is that the account is already active.

**Representative incident examples:**
- `Google_Play-1b8d554a-8ac2-466c-9a62-48d2ceb8f9dc-01`: "đổi sdt thông tin khách hàng ... 3 tuần không xong"
- `App_Store-13177936096-01`: "Popup yêu cầu thay đổi hiện lên liên tục"
- `App_Store-13628052342-01`: "KHÔNG CÓ up hình thông tin cccd cũ"
- `Google_Play-f93f9a8e-c094-4ceb-8268-f4ba73dbb18c-01`: "bắt làm chữ ký số mà cứ chụp ảnh xong là đơ" (recoded from OTHER)

---

### LOGIN_AUTHENTICATION

**Definition:** Routine access to an existing account via password, OTP, iOTP, biometric, or device authorization.

**Typical user goals:** Log in to an existing TCInvest account.

**Include when:**
- Failed login
- Missing iOTP
- Biometric login failure
- Device authorization failure
- Session management issues for existing account

**Exclude when:**
- Initial KYC face verification for registration → ACCOUNT_OPENING_KYC
- Account recovery after lockout → ACCOUNT_PROFILE_MAINTENANCE

**Common confusion with:**
- ACCOUNT_OPENING_KYC — routine login vs. initial biometric registration
- ACCOUNT_PROFILE_MAINTENANCE — routine login vs. recovery after lockout

**Decision rule:** If the account exists and the user is attempting routine access (not recovering from lockout), use LOGIN_AUTHENTICATION.

**Representative incident examples:**
- `Google_Play-ade96f2c-c95d-4eb1-86b7-ed37ea9d208d-01`: "bị lỗi out khi đăng nhập"
- `Google_Play-b431f770-1878-4782-99ba-23a4eadeb8a8-01`: "có mỗi iotp mà nửa ngày không thấy gửi"
- `App_Store-12387003343-01`: "Lỗi đăng nhập"

---

### FUNDING_CASH_TRANSFER

**Definition:** Moving funds into or out of the TCInvest account, including deposits, withdrawals, bank linking, and fund availability.

**Typical user goals:** Deposit, withdraw, or transfer funds.

**Include when:**
- Uncredited deposit
- Blocked withdrawal
- Failed bank linking
- Delayed fund availability
- Fund validation issues

**Exclude when:**
- Display-only balance issue without confirmed movement failure → PORTFOLIO_TRACKING
- Fee complaint without movement failure → not a journey-specific incident

**Common confusion with:**
- PORTFOLIO_TRACKING — confirmed movement failure vs. display-only balance issue
- FEE_PRICING — fee complaints are not journey-specific unless tied to a movement failure

**Decision rule:** If the user reports a confirmed or strongly implied failure to move funds (deposit not credited, withdrawal blocked, transfer failed), use FUNDING_CASH_TRANSFER. If the issue is only about displaying balances, use PORTFOLIO_TRACKING.

**Note:** The strawman proposed splitting FUNDING and WITHDRAWAL as separate stages. Phase B evidence does not support this split — the 16 incidents are evenly distributed across deposit and withdrawal issues. Combined here pending further evidence.

**Representative incident examples:**
- `Google_Play-c06ce68c-7cf1-42e5-b2f7-5deb78d724b4-01`: "giờ thì ko rút tiền được luôn"
- `Google_Play-89c58827-2128-479a-bdfa-12cb8375f846-01`: "chuyển tiền buổi tối khi cần thiết không cho chuyển"
- `App_Store-13013318242-02`: "tiền bắn vào TK ... tới cả tuần tiền TK vẫn bằng 0"

---

### TRADING_ORDER_MANAGEMENT

**Definition:** Placing, modifying, cancelling, confirming, or executing an order, including order-entry context and order status.

**Typical user goals:** Place or manage a stock order.

**Include when:**
- Inability to place/sell/cancel/modify an order
- Wrong order input
- Missing order-entry price/quantity context
- Order status issues

**Exclude when:**
- Generic app freeze without stated order impact → GENERAL_CROSS_JOURNEY
- Viewing holdings without order placement → PORTFOLIO_TRACKING

**Common confusion with:**
- PORTFOLIO_TRACKING — order placement vs. viewing holdings
- PRODUCT_DISCOVERY_MARKET_DATA — researching before trading vs. placing an order
- GENERAL_CROSS_JOURNEY — app-wide performance vs. order-specific failure

**Decision rule:** If the user is in the order flow (placing, modifying, cancelling, or checking status of an order), use TRADING_ORDER_MANAGEMENT. If the user is viewing their portfolio without order intent, use PORTFOLIO_TRACKING.

**Representative incident examples:**
- `Google_Play-ab2dfff3-3256-4426-bcff-90608588dd94-01`: "không khớp được lệnh"
- `App_Store-12092046546-01`: "đặt giá xong mở ra xem giá tt đã thay đổi"
- `App_Store-13630920900-01`: "không đặt huỷ lệnh được"

---

### PORTFOLIO_TRACKING

**Definition:** Viewing own holdings, balances, profit/loss, or chart state for the user portfolio.

**Typical user goals:** View and analyze own portfolio.

**Include when:**
- Missing portfolio P&L
- Missing balance display
- Unsaved chart settings
- Display-only balance issues without confirmed movement failure

**Exclude when:**
- Confirmed deposit/withdrawal failure → FUNDING_CASH_TRANSFER
- Price-board quote freshness → PRODUCT_DISCOVERY_MARKET_DATA

**Common confusion with:**
- FUNDING_CASH_TRANSFER — display-only issue vs. confirmed movement failure
- PRODUCT_DISCOVERY_MARKET_DATA — own holdings vs. market data

**Decision rule:** If the issue is about displaying the user's own portfolio data (holdings, P&L, balances) without a confirmed fund movement failure, use PORTFOLIO_TRACKING. Do not infer failed transfers from display issues.

**Representative incident examples:**
- `App_Store-11750539058-01`: "không hiện thị thông số tiền trong 2 TK ngân hàng"
- `Google_Play-8a6e6c41-9bfb-4a15-bbae-c2f83ead1bda-02`: "quản lý lời lỗ phải nhờ excel"
- `Google_Play-1eb01879-8d2e-41ce-a4b4-1dfd9c6ffd53-03`: "số dư thì hiện chập chờn"

---

### PRODUCT_DISCOVERY_MARKET_DATA

**Definition:** Finding, researching, or monitoring stocks, market data, price boards, and investment research content.

**Typical user goals:** Discover and research investment opportunities.

**Include when:**
- Missing or stale price board data
- Stock screening/search issues
- Chart indicator issues
- Research content quality

**Exclude when:**
- Viewing own holdings → PORTFOLIO_TRACKING
- Placing an order → TRADING_ORDER_MANAGEMENT

**Common confusion with:**
- PORTFOLIO_TRACKING — market data vs. own holdings
- TRADING_ORDER_MANAGEMENT — researching vs. placing an order

**Decision rule:** If the issue is about market-level data (price boards, quotes, research) rather than the user's own portfolio, use PRODUCT_DISCOVERY_MARKET_DATA.

**Representative incident examples:**
- `Google_Play-44d2d1dd-47b3-4af1-89c4-476dd62e4079-01`: "số liệu trên bảng điện không dịch chuyển"
- `App_Store-12901670031-04`: "giá thị trường cập nhật chậm, thiếu chính xác"
- `App_Store-13446154783-03`: "Đội ngũ phân tích thị trường khá tệ"

---

### CUSTOMER_SUPPORT

**Definition:** The incident is about the support interaction itself: reachability, response time, answer quality, or AI assistant behavior.

**Typical user goals:** Obtain timely, useful help from support.

**Include when:**
- Inability to reach support
- Slow or scripted responses
- Irrelevant answers
- AI assistant quality issues

**Exclude when:**
- Underlying product failure with support only mentioned as context → preserve the underlying product journey as primary

**Common confusion with:**
- Any underlying product journey (FUNDING, TRADING, etc.) when support is mentioned but the failure is elsewhere

**Decision rule:** CUSTOMER_SUPPORT is a journey location only when the incident is about the support interaction itself. If the review says "nạp tiền không vào, gọi support mãi không xử lý", this contains two potential incidents: (1) funding failure → FUNDING_CASH_TRANSFER, (2) poor support interaction → CUSTOMER_SUPPORT. Do not collapse them automatically.

**Representative incident examples:**
- `Google_Play-028fcd26-9ed7-4edb-a256-5d54363dfa43-01`: "DV CSKH tệ"
- `App_Store-12387003343-02`: "Hỗ trợ kém"
- `App_Store-13013318242-03`: "AI hỗ trợ nói luyên thuyên chả đâu vào đâu"

---

### GENERAL_CROSS_JOURNEY

**Definition:** The issue genuinely affects multiple journey stages or the whole app, such as app-wide performance, overall UI complexity, or device-level issues.

**Typical user goals:** Use the app generally across multiple tasks.

**Include when:**
- App-wide lag/freeze/crash
- Overall UI complexity that affects multiple tasks
- Device-specific issues (tablet, mobile data)
- General praise/feature requests not tied to a specific journey

**Exclude when:**
- The incident can be located in a specific journey stage
- The evidence is insufficient to determine journey → UNKNOWN

**Common confusion with:**
- UNKNOWN — app-wide but locatable vs. insufficient evidence
- Specific journey stages when the failure is actually localized

**Decision rule:** Use GENERAL_CROSS_JOURNEY only when the issue genuinely spans multiple journey stages or affects the whole app. Do not use it merely because a review is vague — if the evidence is insufficient, use UNKNOWN instead.

**Representative incident examples:**
- `Google_Play-e24f9216-51cf-4eb1-86b7-ed37ea9d208d-01`: "đang dùng bt tự nhiên bị out ra"
- `Google_Play-2d0a8c38-c9a5-4339-ae6c-a5bdad354b60-01`: "treo đơ liên tục"
- `Google_Play-6638c299-2864-4386-837e-41064b75be48-01`: "sao cứ cứng đơ" (recoded from UNCLEAR)

---

### OTHER

**Definition:** A clear journey exists conceptually but does not fit any current model stage.

**Include when:**
- The incident describes a real experience problem that cannot be located in any defined journey stage but the journey is conceptually identifiable

**Exclude when:**
- The incident can be located in a defined journey stage
- The evidence is insufficient → UNKNOWN

**Common confusion with:**
- UNKNOWN — journey exists but unmodeled vs. insufficient evidence
- GENERAL_CROSS_JOURNEY — app-wide issues

**Decision rule:** Use OTHER as a safety valve when a journey is conceptually identifiable but does not fit any defined stage. This is distinct from UNKNOWN (insufficient evidence).

**Note:** No Phase B incidents remain in this category after recoding. Retained for future evidence.

---

### UNKNOWN

**Definition:** Review evidence is insufficient to locate the incident in any journey stage.

**Include when:**
- The incident has insufficient evidence to determine a journey location
- The review text is too vague or short to classify

**Exclude when:**
- The incident can be located in a defined journey stage, even if the pain-point family is unclear

**Common confusion with:**
- OTHER — journey exists but unmodeled
- GENERAL_CROSS_JOURNEY — app-wide but locatable

**Decision rule:** Use UNKNOWN only when the evidence is genuinely insufficient to determine a journey location. Do not use it for vague reviews that can still be located in a specific stage.

**Representative incident examples:**
- `Google_Play-01c61fdf-61e9-4a21-9167-382c2205e006-01`: "App quá tệ" (recoded from GENERAL_CROSS_JOURNEY)
- `Google_Play-b5161b29-c1a7-41da-b77f-d8fd16a97d00-01`: "tcbs năm nay nghỉ lễ sớm à" (recoded from GENERAL_CROSS_JOURNEY)
- `App_Store-12004106819-01`: "Lỗi app" (recoded from GENERAL_CROSS_JOURNEY)
- `App_Store-11801692398-01`: "Oke" (recoded from UNCLEAR)

---

## Cross-journey rules

### CUSTOMER_SUPPORT vs underlying product journey

CUSTOMER_SUPPORT is a journey location only when the incident is about the support interaction itself. If support is mentioned while the actual failure occurs elsewhere, preserve the underlying product journey as primary. A single review may contain multiple incidents at different journey locations.

### CROSS_JOURNEY vs UNKNOWN

CROSS_JOURNEY: the issue genuinely affects multiple journey stages or the whole app. UNKNOWN: the evidence is insufficient to locate the incident. Do not use CROSS_JOURNEY merely because a review is vague.

### OTHER vs UNKNOWN

OTHER: a clear journey exists conceptually but does not fit the current model. UNKNOWN: the evidence is insufficient. Use OTHER only when the journey is conceptually identifiable but unmodeled.

## QA gate before journey freeze

1. **Adjudicate against independent human labels** on a subset not used to draft these rules; record coder ID, date, disagreements and reconciled rule. Single-reviewer AI-assisted sample is not independent agreement.
2. For each journey: validate the include/exclude rules yield the expected decision on the Phase B incidents. Keep separate incident types for praise/unmet needs/requests.
3. Review the boundary cases: REGISTRATION_KYC vs ACCOUNT_PROFILE_MAINTENANCE, LOGIN_AUTHENTICATION vs ACCOUNT_RECOVERY, FUNDING vs WITHDRAWAL, TRADING vs PORTFOLIO_MONITORING, DISCOVERY_RESEARCH vs PORTFOLIO_MONITORING, CUSTOMER_SUPPORT vs underlying product journey.
4. Freeze journey model together with taxonomy v1 only after adjudications are accepted. Until then write `candidate` in version metadata and do not scale automated classification to all 736 reviews.
