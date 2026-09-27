# TCInvest Customer Voice Synthesis (Provisional)

**Status**: PROVISIONAL / EXPLORATORY — classification is not validated; taxonomy and journey model are not frozen.

**Date**: 2026-09-23
**Scope**: TCInvest public reviews, 24-month window (2024-09-22 to 2026-09-22)
**Evidence base**: 736 public review records, 796 atomic incidents, 15 canonical pain-point families

## Scope and Method

This synthesis draws on 736 public review records from Google Play (403) and App Store (333) over a 24-month window. Each review was semantically classified into atomic incidents using a candidate taxonomy (Phase C, 15 families) and candidate journey model (Phase D, 11 stages). Classification was PROVISIONAL and underwent self-review QA adjudication (Phase F). Measurement (Phase G) computed frequency, severity, rating, sentiment, journey, source, and trend dimensions. This synthesis (Phase H) applies a qualitative prioritization framework across seven dimensions without computing an arbitrary weighted composite score.

## Evidence Base

| Denominator | Value |
|---|---:|
| All analyzed public review records | 736 |
| Complaint-containing reviews | 613 (83.3%) |
| Google Play reviews | 403 |
| App Store reviews | 333 |
| Total incidents | 796 |
| Reviews with ≥1 incident | 646 (87.8%) |
| Canonical pain-point families | 15 |
| Journey stages | 11 |

## Main Observed Patterns

1. **Performance and UX dominate frequency**: PERFORMANCE_RELIABILITY (156 reviews, 21.2%) and UX_NAVIGATION_COMPLEXITY (150 reviews, 20.4%) are the two most frequent families, together accounting for ~41% of all analyzed reviews.

2. **Transaction-critical families dominate severity**: TRADING_ORDER_EXECUTION (75% HIGH), AUTHENTICATION_IOTP (73% HIGH), and DEPOSIT_WITHDRAWAL_TRANSFER (61% HIGH) have the highest severity shares.

3. **Source parity**: Google Play and App Store show similar within-source rates for most families (differences <2 pp). PORTFOLIO_ACCOUNT_INFORMATION shows a larger Google Play skew (+3.8 pp).

4. **April–May 2026 spike**: A concentrated review spike is observed around late April–May 2026. Possible operational causes are not independently documented within this project and are treated as hypotheses only.

5. **Sparse families**: EXCESSIVE_DATA_CONSUMPTION (1 review), SECURITY_ACCOUNT_PROTECTION (7), MARKET_RESEARCH_RECOMMENDATION_UTILITY (9) have low evidence and should not drive prioritization.

## Candidate Pain Points

Five evidence-supported candidate pain points for deeper validation:

| # | Family | Reviews | % all | HIGH % | Journey | Median rating | Trend |
|---:|---|---:|---:|---:|---|---:|---|
| 1 | PERFORMANCE_RELIABILITY | 156 | 21.2% | 62% | GENERAL_CROSS_JOURNEY | 1 | STABLE |
| 2 | TRADING_ORDER_EXECUTION | 75 | 10.2% | 75% | TRADING_ORDER_MANAGEMENT | 1 | INCREASING |
| 3 | DEPOSIT_WITHDRAWAL_TRANSFER | 56 | 7.6% | 61% | FUNDING_CASH_TRANSFER | 1 | STABLE |
| 4 | AUTHENTICATION_IOTP | 55 | 7.5% | 73% | LOGIN_AUTHENTICATION | 1 | INCREASING |
| 5 | ONBOARDING_KYC | 31 | 4.2% | 55% | ACCOUNT_OPENING_KYC | 1 | STABLE |

These are NOT "the 5 worst problems" or "the definitive Top 5 customer problems." They are five evidence-supported candidates for deeper validation by M4/M5.

## Journey Concentration

| Journey | Reviews | HIGH | Notes |
|---|---:|---:|---|
| GENERAL_CROSS_JOURNEY | 222 | 84 | App-wide issues; largest category |
| TRADING_ORDER_MANAGEMENT | 146 | 72 | Transaction-critical |
| FUNDING_CASH_TRANSFER | 57 | 37 | Transaction-critical |
| LOGIN_AUTHENTICATION | 54 | 31 | Access-critical |
| PRODUCT_DISCOVERY_MARKET_DATA | 44 | 11 | Discovery-critical |
| CUSTOMER_SUPPORT | 39 | 25 | Service-critical |
| ACCOUNT_OPENING_KYC | 27 | 16 | Onboarding-critical |
| ACCOUNT_PROFILE_MAINTENANCE | 22 | 18 | Maintenance-critical |

## Severity and Rating Signals

All five candidate families have median rating = 1 and 1-2 star share ≥ 90%. This means reviews mentioning these families are associated with the lowest observed ratings in the public-review sample. This is a correlation within self-selected reviewers, not a causal claim.

## Trend Signals

- TRADING_ORDER_EXECUTION: INCREASING (first half vs second half of window)
- AUTHENTICATION_IOTP: INCREASING
- Others: STABLE

INCREASING signals are conservative and do not imply causality. They reflect more mentions in the second half of the 24-month window.

## Emerging Themes

Three single-case new themes confirmed during QA, kept separate from the main candidate set:

| Theme | Family | Incidents | Status |
|---|---|---:|---|
| APP_STORE_REGION_AVAILABILITY | OTHER | 1 | Emerging / monitor-only |
| DATA_SELLING_SUSPICION | SECURITY_ACCOUNT_PROTECTION | 1 | Emerging / monitor-only |
| EXCESSIVE_ADS | NOTIFICATION_COMMUNICATION | 1 | Emerging / monitor-only |

These are NOT promoted into the main candidate set because each has only a single incident. They are tracked for future evidence collection.

## Candidate Business Problems

### CAND-01: App reliability failures during general use
Public reviewers repeatedly report app lag, freezing, and crashes during general use, which is associated with inability to complete tasks and visible frustration across multiple journeys. 156 reviews (21.2% of analyzed sample), 62% HIGH severity, both platforms represented.

### CAND-02: Order execution failures
Public reviewers repeatedly report inability to place, modify, or cancel stock orders, which is associated with missed trading opportunities and explicit financial-loss claims. 75 reviews (10.2%), 75% HIGH severity, INCREASING trend.

### CAND-03: Deposit/withdrawal/transfer delays or failures
Public reviewers repeatedly report delays or failures in depositing, withdrawing, or transferring funds, which is associated with inability to access money and high-severity financial impact. 56 reviews (7.6%), 61% HIGH severity.

### CAND-04: Authentication and login failures
Public reviewers repeatedly report login failures, missing iOTP, and biometric authentication issues, which is associated with inability to access the account and downstream task blockage. 55 reviews (7.5%), 73% HIGH severity, INCREASING trend.

### CAND-05: Onboarding and KYC friction
Public reviewers repeatedly report difficulty completing new-account registration and identity verification, which is associated with blocked customer acquisition. 31 reviews (4.2%), 55% HIGH severity.

## M4/M5 Validation Handoff

For each candidate, M4 should inspect the actual product flow and attempt to reproduce the reported friction/failure. M5 should assess business impact, operational impact, and strategic relevance. Neither M4 nor M5 should assume the review claim is true without independent verification.

Full handoff: `05_outputs/tables/m4_m5_validation_handoff.csv`

## Limitations

1. **Self-selected public reviewers**: Google Play and App Store reviewers are not representative of all TCInvest customers.
2. **PROVISIONAL classification**: No independent human validation has been performed. QA adjudication was self-review.
3. **Taxonomy and journey not frozen**: Family boundaries and journey stages may change before finalization.
4. **Single-reviewer coding**: All classifications and QA were performed by a single coder (AI-assisted).
5. **Small sample for sparse families**: Families with <10 reviews should not drive prioritization.
6. **No causality claims**: Rating associations, source differences, and trend signals are observational, not causal.
7. **No prevalence claims**: "X% of reviews mention Y" is not "X% of customers experience Y."
8. **No unverified event attribution**: The April–May 2026 review spike is reported as an observed pattern. Any specific operational cause is a hypothesis, not an established fact within this project.

## What Can and Cannot Be Concluded

**Can be concluded** (within the analyzed public-review sample):
- Five pain-point families show strong evidence across frequency, severity, journey criticality, rating association, and source coverage.
- These families are associated with the lowest observed ratings and highest severity in the sample.
- Transaction-critical journeys (trading, funding, authentication) carry the highest severity.

**Cannot be concluded**:
- Prevalence of these issues across all TCInvest customers.
- Causality between pain points and low ratings.
- Whether the April–May 2026 spike reflects a specific operational event.
- Whether the taxonomy and journey model are correct in their current form.
- Whether the five candidates are the "most important" problems for the business.

These candidates require triangulation with product-flow audit (M4), support data, analytics, telemetry, and customer interviews before any business prioritization decision.
