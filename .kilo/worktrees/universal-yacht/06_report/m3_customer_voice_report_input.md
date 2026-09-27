# M3 Customer Voice Report Input (Provisional)

**Status**: PROVISIONAL / EXPLORATORY

## 1. Research Question

What experience problems do public reviewers of TCInvest (Google Play and App Store) repeatedly report, and which pain-point candidates are most evidence-supported for deeper business validation?

## 2. Method

- 736 public review records collected (Google Play: 403, App Store: 333) over 24-month window (2024-09-22 to 2026-09-22).
- Each review semantically classified into atomic incidents using candidate Phase C taxonomy (15 pain-point families) and Phase D journey model (11 stages).
- PROVISIONAL classification with self-review QA adjudication (Phase F).
- Measurement (Phase G) across frequency, severity, rating, sentiment, journey, source, trend.
- Qualitative prioritization (Phase H) across 7 dimensions without weighted composite score.

## 3. Evidence Base

| Metric | Value |
|---|---:|
| Reviews analyzed | 736 |
| Complaint-containing reviews | 613 (83.3%) |
| Incidents extracted | 796 |
| Pain-point families | 15 |
| Journey stages | 11 |

## 4. Key Findings

### Finding 1: Performance and UX dominate frequency
**Evidence**: 156 reviews (21.2%) mention PERFORMANCE_RELIABILITY; 150 reviews (20.4%) mention UX_NAVIGATION_COMPLEXITY. Together ~41% of all analyzed reviews.
**Interpretation**: These are the most recurrent issues in the public-review sample.
**Hypothesis**: App-wide reliability and navigation complexity affect multiple journeys.
**Limitation**: Public reviewers are self-selected; this does not estimate prevalence across TCInvest customers.

### Finding 2: Transaction-critical families carry highest severity
**Evidence**: TRADING_ORDER_EXECUTION 75% HIGH severity; AUTHENTICATION_IOTP 73% HIGH; DEPOSIT_WITHDRAWAL_TRANSFER 61% HIGH.
**Interpretation**: When these issues occur, reviewers consistently rate them as high-impact.
**Hypothesis**: Failures in trading, authentication, or money movement directly block financial tasks.
**Limitation**: Severity is based on review text interpretation, not independent impact measurement.

### Finding 3: Five candidate pain points show strong cross-dimensional evidence
**Evidence**: PERFORMANCE_RELIABILITY (156 reviews, 62% HIGH, both platforms), TRADING_ORDER_EXECUTION (75, 75% HIGH, INCREASING), DEPOSIT_WITHDRAWAL_TRANSFER (56, 61% HIGH, both), AUTHENTICATION_IOTP (55, 73% HIGH, INCREASING), ONBOARDING_KYC (31, 55% HIGH, both).
**Interpretation**: These five families combine high frequency or high severity with transaction-critical journey location and both-platform coverage.
**Hypothesis**: Each represents a distinct, reproducible product issue worth deeper investigation.
**Limitation**: Classification is PROVISIONAL; taxonomy not frozen; single-coder.

### Finding 4: Source parity across platforms
**Evidence**: Most families show <2 pp within-source rate difference between Google Play and App Store. PORTFOLIO_ACCOUNT_INFORMATION shows +3.8 pp Google Play skew.
**Interpretation**: Pain-point patterns are broadly consistent across platforms.
**Hypothesis**: The issues are product-level, not platform-specific.
**Limitation**: App Store coverage is a 522-row validated union, not a complete lifetime population.

### Finding 5: April–May 2026 review spike
**Evidence**: A concentrated spike in PERFORMANCE_RELIABILITY and UX_NAVIGATION_COMPLEXITY reviews around late April–May 2026.
**Interpretation**: This may reflect a transient event-driven cluster.
**Hypothesis**: Possible operational causes (not independently documented within this project).
**Limitation**: No independent evidence of a specific operational event within this project's data.

### Finding 6: Sparse families should not drive prioritization
**Evidence**: EXCESSIVE_DATA_CONSUMPTION (1 review), SECURITY_ACCOUNT_PROTECTION (7), MARKET_RESEARCH_RECOMMENDATION_UTILITY (9).
**Interpretation**: These families have insufficient evidence for prioritization despite potentially high severity.
**Hypothesis**: May become relevant with more data.
**Limitation**: Current sample size limits confidence in these families.

### Finding 7: Three single-case new themes tracked separately
**Evidence**: APP_STORE_REGION_AVAILABILITY (1), DATA_SELLING_SUSPICION (1), EXCESSIVE_ADS (1).
**Interpretation**: These are emerging signals but not yet recurring themes.
**Hypothesis**: May indicate niche issues worth monitoring.
**Limitation**: Single-incident evidence is insufficient for taxonomy promotion.

## 5. Candidate Pain-Point Table

| Candidate | Family | Reviews | % all | HIGH % | Journey | Median rating |
|---|---|---:|---:|---:|---|---:|
| CAND-01 | PERFORMANCE_RELIABILITY | 156 | 21.2% | 62% | GENERAL_CROSS_JOURNEY | 1 |
| CAND-02 | TRADING_ORDER_EXECUTION | 75 | 10.2% | 75% | TRADING_ORDER_MANAGEMENT | 1 |
| CAND-03 | DEPOSIT_WITHDRAWAL_TRANSFER | 56 | 7.6% | 61% | FUNDING_CASH_TRANSFER | 1 |
| CAND-04 | AUTHENTICATION_IOTP | 55 | 7.5% | 73% | LOGIN_AUTHENTICATION | 1 |
| CAND-05 | ONBOARDING_KYC | 31 | 4.2% | 55% | ACCOUNT_OPENING_KYC | 1 |

## 6. Representative Evidence

### CAND-01: PERFORMANCE_RELIABILITY
- "App cập nhật dữ liệu lúc thị trường mở cửa, không giao dịch được" (App Store, 2026-04-29, rating 1)
- "App lỗi tê liệt ngay đầu phiên giao dịch. Bảng điện không cập nhật, không mua bán được" (App Store, 2026-04-29, rating 1)
- "app siêu tệ ,phí thời gian ,tiền bạc" (Google Play, 2026-02-10, rating 1)

### CAND-02: TRADING_ORDER_EXECUTION
- "khi nào cần bán là nó đơ và k vào đc app" (App Store, 2025-12-05, rating 2)
- "không đặt lệnh hủy lệnh dc" (Google Play, 2026-01-14, rating 1)
- "Mất tiền nhiều quá ko bán dc giá đỉnh" (App Store, 2026-04-29, rating 1)

### CAND-03: DEPOSIT_WITHDRAWAL_TRANSFER
- "Lúc cần rút tiền thì tính năng ipower bị biến mất không rút tiền được" (App Store, 2026-06-06, rating 1)
- "App này chuyên giam Tiền cổ tức đợi cuối ngày hết giao dịch mới nhả Tiền ra" (App Store, 2026-07-17, rating 1)
- "tính năng chuyển tiền ra ngoài bị lỗi" (Google Play, 2026-05-17, rating 1)

### CAND-04: AUTHENTICATION_IOTP
- "cái hệ thống quét khuôn mặt nguuu lôl, ko có báo động là quét dc hay chưa" (Google Play, 2026-04-25, rating 1)
- "Rất thường gặp lỗi đăng nhập" (App Store, 2026-07-13, rating 1)
- "Cứ 24 tiếng lại phải chạy vô app lấy cái OTP bằng tay xong đi cập nhật biến môi trường" (App Store, 2026-08-14, rating 1)

### CAND-05: ONBOARDING_KYC
- "bắt xác thực cccd nhưng app lỗi load 7749 lần mãi k đc" (App Store, 2025-05-22, rating 1)
- "Dăng ký ol mà lâu vl" (Google Play, 2026-02-25, rating 2)
- "không đăng ký được" (Phase B reference, Google Play, rating 1)

## 7. Customer Journey Implications

- **GENERAL_CROSS_JOURNEY** (222 reviews) dominates, indicating app-wide reliability and UX issues affect multiple journeys simultaneously.
- **TRADING_ORDER_MANAGEMENT** (146 reviews) is the largest specific journey with the most HIGH-severity incidents.
- **FUNDING_CASH_TRANSFER** and **LOGIN_AUTHENTICATION** are transaction-critical and access-critical journeys with high severity.
- **ACCOUNT_OPENING_KYC** affects new customer acquisition.

## 8. Candidate Business Problems

The five candidates represent potential business problems for deeper investigation. Each requires M4 (product flow audit) and M5 (business impact assessment) validation before any business prioritization decision.

See `05_outputs/tables/candidate_problem_cards_provisional.csv` for full problem cards with root-cause hypotheses and validation requirements.

## 9. Limitations

- 736 public review records ≠ 736 unique customers.
- Public reviewers are self-selected and not representative of all TCInvest customers.
- Classification is PROVISIONAL; no independent human validation.
- Taxonomy and journey model are not frozen.
- All findings are observational; no causality claims.
- No prevalence estimates across the customer base.
- April–May 2026 spike causes are hypotheses only.

## 10. Recommended Validation Questions for M4/M5

### For M4 (Product Flow Audit):
1. **CAND-01**: Can app freeze/lag be reproduced on representative devices during peak market hours? What are the latency profiles at key API endpoints?
2. **CAND-02**: Can order placement/cancellation failures be reproduced? What is the order-state synchronization architecture?
3. **CAND-03**: What is the end-to-end deposit/withdrawal flow? Where are the failure points?
4. **CAND-04**: Can login failures be reproduced across devices? What is the iOTP delivery infrastructure?
5. **CAND-05**: What is the current onboarding/KYC completion rate? Where do users drop off?

### For M5 (Business Impact Assessment):
1. **CAND-01**: What is the impact on trading volume and customer retention?
2. **CAND-02**: What is the financial impact of failed orders? What is the customer compensation history?
3. **CAND-03**: What is the financial impact and regulatory/compliance constraints?
4. **CAND-04**: What is the impact on customer acquisition and retention?
5. **CAND-05**: What is the impact on new-customer conversion and onboarding cost?

M4 and M5 should NOT assume the review claims are true without independent verification. They should treat the review evidence as a signal for where to look, not as proof of what they will find.
