# Provisional Measurement

**Status**: PROVISIONAL / EXPLORATORY — classification is not validated; taxonomy and journey model are not frozen.

**Date**: 2026-09-23
**Scope**: TCInvest public reviews, 24-month window (2024-09-22 to 2026-09-22)
**Source data**: `01_data/processed/reviews_classified_24m_provisional_adjudicated.csv` (736 reviews), `01_data/processed/review_incidents_24m_provisional_adjudicated.csv` (796 incidents)

All findings describe patterns observed in the 736 analyzed public review records. They do not describe TCInvest customers or generalizable prevalence.

## Scope

- 736 public review records (Google Play: 403, App Store: 333)
- 796 atomic incidents extracted
- 15 canonical pain-point families from Phase C candidate taxonomy
- 11 journey stages from Phase D candidate journey model
- 25 months of data (Oct 2024 – Sep 2026, inclusive of partial months)

## Denominators

| Denominator | Value |
|---|---:|
| All analyzed public review records (N) | 736 |
| Complaint-containing reviews | 613 (83.3%) |
| Google Play reviews | 403 |
| App Store reviews | 333 |
| Total incidents | 796 |
| Reviews with ≥1 incident | 646 (87.8%) |
| Reviews with 0 incidents | 90 (12.2%) |

Review count ≠ unique customers. Incident count ≠ customer prevalence.

## Pain-point Frequency

Top 5 by unique review count:

| Rank | Family | Reviews | Incidents | % all | % complaint |
|---:|---|---:|---:|---:|---:|
| 1 | PERFORMANCE_RELIABILITY | 156 | 156 | 21.2% | 25.4% |
| 2 | UX_NAVIGATION_COMPLEXITY | 150 | 155 | 20.4% | 24.5% |
| 3 | CUSTOMER_SUPPORT | 80 | 82 | 10.9% | 13.1% |
| 4 | TRADING_ORDER_EXECUTION | 75 | 76 | 10.2% | 12.2% |
| 5 | DEPOSIT_WITHDRAWAL_TRANSFER | 56 | 57 | 7.6% | 9.1% |

Full table: `05_outputs/tables/pain_point_frequency_provisional.csv`

Note: Multi-incident reviews are counted once per family for review-level frequency.

## Severity

Top 3 families by HIGH-severity share:

| Family | HIGH | MEDIUM | LOW | % HIGH |
|---|---:|---:|---:|---:|
| TRADING_ORDER_EXECUTION | 47 | 22 | 5 | 62.7% |
| AUTHENTICATION_IOTP | 31 | 17 | 6 | 56.4% |
| DEPOSIT_WITHDRAWAL_TRANSFER | 31 | 17 | 8 | 54.4% |

Trading, authentication, and money-movement incidents skew toward HIGH severity. UX/performance complaints skew toward MEDIUM.

Full table: `05_outputs/tables/pain_point_severity_provisional.csv`

## Rating and Sentiment

| Family | Median rating | 1-2 star share |
|---|---:|---:|
| DEPOSIT_WITHDRAWAL_TRANSFER | 1 | 98.2% |
| TRADING_ORDER_EXECUTION | 1 | 97.3% |
| PERFORMANCE_RELIABILITY | 1 | 95.5% |
| AUTHENTICATION_IOTP | 1 | 94.5% |
| CUSTOMER_SUPPORT | 1 | 92.5% |

Pain-point families are **associated with lower observed ratings** in this public-review sample. This is a correlation within self-selected reviewers, not a causal claim.

Sentiment is NEGATIVE-dominant across all families (typically 70-90% NEGATIVE). Some families include MIXED reviews where praise is mixed with complaint.

Full tables: `05_outputs/tables/pain_point_rating_provisional.csv`, `05_outputs/tables/pain_point_sentiment_provisional.csv`

## Journey

| Journey | Reviews | Incidents | HIGH | Families |
|---|---:|---:|---:|---:|
| GENERAL_CROSS_JOURNEY | 222 | 222 | 84 | 11 |
| TRADING_ORDER_MANAGEMENT | 146 | 146 | 72 | 7 |
| FUNDING_CASH_TRANSFER | 57 | 59 | 37 | 6 |
| LOGIN_AUTHENTICATION | 54 | 56 | 31 | 3 |
| PRODUCT_DISCOVERY_MARKET_DATA | 44 | 44 | 11 | 4 |
| CUSTOMER_SUPPORT | 39 | 40 | 25 | 3 |
| ACCOUNT_OPENING_KYC | 27 | 27 | 16 | 2 |
| ACCOUNT_PROFILE_MAINTENANCE | 22 | 24 | 18 | 3 |
| UNKNOWN | 23 | 23 | 0 | 2 |
| PORTFOLIO_TRACKING | 15 | 15 | 4 | 3 |
| OTHER | 1 | 1 | 1 | 1 |

GENERAL_CROSS_JOURNEY is the largest category (app-wide issues). Among specific journeys, TRADING_ORDER_MANAGEMENT has the most incidents and the most HIGH-severity incidents.

Full table: `05_outputs/tables/journey_pain_point_provisional.csv`
Matrix: `05_outputs/tables/pain_point_journey_matrix_provisional.csv`

## Source Comparison

Largest within-source rate differences (Google Play − App Store, percentage points):

| Family | GP rate | AS rate | Diff (pp) |
|---|---:|---:|---:|
| PORTFOLIO_ACCOUNT_INFORMATION | 5.0% | 1.2% | +3.8 |
| ACCOUNT_RECOVERY_PROFILE_CHANGE | 4.5% | 2.4% | +2.1 |
| PERFORMANCE_RELIABILITY | 21.6% | 21.0% | +0.6 |
| UX_NAVIGATION_COMPLEXITY | 20.3% | 20.7% | −0.4 |
| AUTHENTICATION_IOTP | 7.4% | 7.8% | −0.4 |
| TRADING_ORDER_EXECUTION | 10.4% | 10.5% | −0.1 |

Most families show small differences (<2 pp). PORTFOLIO_ACCOUNT_INFORMATION shows a larger Google Play skew. These differences could reflect reviewer mix, platform differences, product-version differences, or App Store coverage limitations — not necessarily behavioral differences.

**Note on source comparison totals**: The source comparison table sums family-source pairs across all 15 families. Because multi-family reviews are counted once per family, the summed Google Play total (412) exceeds the canonical Google Play denominator (403), and the summed App Store total (322) is less than the canonical App Store denominator (333). The difference reflects reviews that appear in multiple families (GP) or that have no canonical-family incident (AS). The within-source rate column uses the correct canonical denominators (GP=403, AS=333).

Full table: `05_outputs/tables/pain_point_source_comparison_provisional.csv`

## Trend

Monthly review rates over 25 months for top 5 families show:

- **PERFORMANCE_RELIABILITY** and **UX_NAVIGATION_COMPLEXITY** have visible spikes in April-May 2026. A concentrated review spike is observed around late April–May 2026. Possible operational causes are not independently documented within this project and are treated as hypotheses only.
- **CUSTOMER_SUPPORT** rates are relatively stable across the window.
- **TRADING_ORDER_EXECUTION** and **DEPOSIT_WITHDRAWAL_TRANSFER** show moderate fluctuation without clear directional trend.

Trend signal summary (first half vs second half of window):

| Family | Trend |
|---|---|
| TRADING_ORDER_EXECUTION | INCREASING |
| AUTHENTICATION_IOTP | INCREASING |
| CUSTOMER_SUPPORT | INCREASING |
| PERFORMANCE_RELIABILITY | STABLE |
| UX_NAVIGATION_COMPLEXITY | STABLE |
| Most others | INSUFFICIENT_DATA or STABLE |

Trend signals are conservative and do not imply causality. The April–May 2026 spike may reflect a transient event-driven cluster; persistent recurrence (observed across multiple months) is what supports prioritization, not single-month spikes.

Full table: `05_outputs/tables/pain_point_monthly_trend_provisional.csv`

## New Themes

Confirmed new themes from QA:

| Subtype | Incidents | Reviews | Recurring? |
|---|---:|---:|---|
| EXCESSIVE_ADS (NOTIFICATION_COMMUNICATION) | 1 | 1 | No — single case |
| DATA_SELLING_SUSPICION (SECURITY_ACCOUNT_PROTECTION) | 1 | 1 | No — single case |
| APP_STORE_REGION_AVAILABILITY (OTHER) | 1 | 1 | No — single case |

5 additional new-theme cases were reclassified to existing families or marked UNCLEAR (cosmetic icon color, removed feature, community feature, child account, font size).

These are NOT promoted into main taxonomy families. They are tracked separately for future evidence collection.

Full table: `05_outputs/tables/new_theme_summary_provisional.csv`

## Key Observed Patterns

1. **Performance and UX dominate**: PERFORMANCE_RELIABILITY (156 reviews) and UX_NAVIGATION_COMPLEXITY (150 reviews) are the two most frequent families, together accounting for ~41% of all analyzed reviews.

2. **Money-movement and trading are HIGH-severity**: TRADING_ORDER_EXECUTION (62.7% HIGH), AUTHENTICATION_IOTP (56.4% HIGH), and DEPOSIT_WITHDRAWAL_TRANSFER (54.4% HIGH) have the highest severity shares.

3. **April–May 2026 spike**: A concentrated review spike is observed around late April–May 2026. Possible operational causes are not independently documented within this project and are treated as hypotheses only.

4. **Source parity**: Google Play and App Store show similar within-source rates for most families (differences <2 pp). PORTFOLIO_ACCOUNT_INFORMATION shows a Google Play skew.

5. **Support interaction quality**: CUSTOMER_SUPPORT reviews (80) include AI/bot frustration themes and hotline inaccessibility.

6. **Sparse families**: EXCESSIVE_DATA_CONSUMPTION (1 review), SECURITY_ACCOUNT_PROTECTION (7), MARKET_RESEARCH_RECOMMENDATION_UTILITY (9) have low evidence and should not be over-interpreted.

## Limitations

1. **Self-selected public reviewers**: Google Play and App Store reviewers are not representative of all TCInvest customers.
2. **PROVISIONAL classification**: No independent human validation has been performed. QA adjudication was self-review.
3. **Taxonomy and journey not frozen**: Family boundaries and journey stages may change before finalization.
4. **Single-reviewer coding**: All classifications and QA were performed by a single coder (AI-assisted).
5. **Small sample for sparse families**: Families with <10 reviews should not drive prioritization.
6. **No causality claims**: Rating associations, source differences, and trend signals are observational, not causal.
7. **No prevalence claims**: "X% of reviews mention Y" is not "X% of customers experience Y."
8. **App Store coverage**: 522-row App Store canonical is the broadest validated union, not a complete lifetime population.
9. **No unverified event attribution**: The April–May 2026 review spike is reported as an observed pattern. Any specific operational cause is a hypothesis, not an established fact within this project.

## Files Produced

| File | Purpose |
|---|---|
| `05_outputs/tables/pain_point_frequency_provisional.csv` | Family-level frequency |
| `05_outputs/tables/pain_point_severity_provisional.csv` | Family-level severity distribution |
| `05_outputs/tables/pain_point_rating_provisional.csv` | Family-level rating distribution |
| `05_outputs/tables/pain_point_sentiment_provisional.csv` | Family-level sentiment distribution |
| `05_outputs/tables/journey_pain_point_provisional.csv` | Journey-level aggregation |
| `05_outputs/tables/pain_point_journey_matrix_provisional.csv` | Family × journey matrix |
| `05_outputs/tables/pain_point_source_comparison_provisional.csv` | Google Play vs App Store |
| `05_outputs/tables/pain_point_monthly_trend_provisional.csv` | Monthly rates |
| `05_outputs/tables/pain_point_representative_evidence_provisional.csv` | 2-3 examples per family |
| `05_outputs/tables/new_theme_summary_provisional.csv` | Confirmed new themes |
| `05_outputs/tables/pain_point_summary_provisional.csv` | Master summary (one row per family) |
| `05_outputs/tables/pain_point_prioritization_inputs_provisional.csv` | Phase H inputs |
| `05_outputs/charts/pain_point_review_frequency_provisional.png` | Frequency chart |
| `05_outputs/charts/pain_point_severity_distribution_provisional.png` | Severity chart |
| `05_outputs/charts/pain_point_by_journey_provisional.png` | Journey matrix chart |
| `05_outputs/charts/pain_point_source_comparison_provisional.png` | Source comparison chart |
| `05_outputs/charts/pain_point_monthly_trend_provisional.png` | Monthly trend chart |
| `04_analysis/provisional_measurement.md` | This document |
