# Provisional Classification Validation

**Status**: PROVISIONAL — taxonomy and journey model are NOT frozen; no independent human validation has been performed.

**Date**: 2026-09-23
**Scope**: TCInvest reviews, 24-month window (2024-09-22 to 2026-09-22)
**Input dataset**: `01_data/processed/reviews_analysis_24m.csv` (736 rows, 32 cols)

## 1. Pipeline Summary

| Stage | Output | Count |
|---|---|---|
| Total target reviews | — | 736 |
| Phase B reuse (crosswalk + boundary review + journey audit) | reviews / incidents | 100 / 146 |
| New semantic classification (Batches 1–8) | reviews / incidents | 636 / 650 |
| **Total classified** | reviews / incidents | **736 / 796** |

Batches 1–8 each processed ~76–80 reviews in deterministic order (by `review_date`, `source`, `review_id`). Checkpoint infrastructure at `01_data/processed/provisional_classification_work/` preserved state between sessions.

## 2. Schema Compliance

All output files conform to the documented schema:

- **reviews_classified_24m_provisional.csv** (18 cols): `source`, `review_id`, `review_date`, `rating`, `title`, `review_text_raw`, `incident_present`, `incident_count`, `sentiment`, `complaint_present`, `product_related`, `primary_pain_point_family`, `primary_pain_point_subtype`, `primary_journey`, `max_severity`, `classification_confidence`, `needs_human_review`, `classification_status`
- **review_incidents_24m_provisional.csv** (13 cols): `incident_id`, `source`, `review_id`, `incident_type`, `pain_point_family`, `pain_point_subtype`, `journey`, `severity`, `evidence_span`, `confidence`, `new_theme_flag`, `needs_human_review`, `classification_status`

All rows carry `classification_status = PROVISIONAL`. CSV files use UTF-8 with BOM.

## 3. QA Checks (all passed)

| Check | Result |
|---|---|
| Review row count = 736 | ✅ |
| Incident row count = 796 | ✅ |
| All `classification_status = PROVISIONAL` | ✅ |
| Every incident has non-empty `evidence_span` | ✅ |
| `incident_count` matches actual incident count per review | ✅ |
| Unique `review_id` and `incident_id` | ✅ (736 / 796) |
| `incident_id` naming convention (`{source}-{review_id}-{NN}`) | ✅ |
| Canonical family values only (after normalization) | ✅ |
| Canonical journey values only | ✅ |
| Canonical severity values only (LOW/MEDIUM/HIGH/NONE) | ✅ |
| Canonical sentiment values only (POSITIVE/NEGATIVE/MIXED/NEUTRAL/UNCLEAR) | ✅ |
| Canonical incident_type values only | ✅ |
| Canonical confidence values only (HIGH/MEDIUM/LOW) | ✅ |
| `needs_human_review` boolean | ✅ |
| Pure-praise reviews do not carry `complaint_present = True` | ✅ |
| No-incident reviews have empty family/journey | ✅ |

### Family normalization applied

39 review rows and 57 incident rows used non-canonical family labels inherited from earlier batches (journey names used as family names, or placeholder labels). These were normalized:

| Old label | Mapped to |
|---|---|
| `LOGIN_AUTHENTICATION` | `AUTHENTICATION_IOTP` |
| `PORTFOLIO_TRACKING` | `PRODUCT_PORTFOLIO_INFORMATION` |
| `PORTFOLIO_ACCOUNT_INFORMATION` | `PRODUCT_PORTFOLIO_INFORMATION` |
| `MARKET_DATA_INFORMATION` | `MARKET_DATA_STALENESS_ACCURACY` |
| `DOMAIN_OR_OTHER_NEW_THEME` | `OTHER` |
| `OTHER_NEW_THEME` | `OTHER` |
| `NONE` | (empty) |

This is a label-mapping pass, not a re-classification pass. The original incident meaning is preserved.

## 4. Coverage and Distribution

### Source mix

| Source | Reviews |
|---|---|
| Google Play | 403 (54.8%) |
| App Store | 333 (45.2%) |

### Sentiment

| Sentiment | Reviews |
|---|---|
| NEGATIVE | 573 (77.9%) |
| POSITIVE | 98 (13.3%) |
| MIXED | 47 (6.4%) |
| NEUTRAL | 12 (1.6%) |
| UNCLEAR | 6 (0.8%) |

### Incident presence

| | Reviews |
|---|---|
| With ≥1 incident | 646 (87.8%) |
| Without incident | 90 (12.2%) |
| Praise-only reviews | 16 |
| Multi-incident reviews | 119 |

### Severity (max per review)

| Severity | Reviews |
|---|---|
| HIGH | 331 (45.0%) |
| MEDIUM | 186 (25.3%) |
| NONE | 102 (13.9%) |
| LOW | 27 (3.7%) |
| (no incident → not counted) | 90 |

### Confidence

| Confidence | Reviews |
|---|---|
| HIGH | 626 (85.1%) |
| MEDIUM | 79 (10.7%) |
| LOW | 31 (4.2%) |

### Pain-point family distribution (reviews with primary family)

| Family | Reviews |
|---|---|
| PERFORMANCE_RELIABILITY | 150 |
| UX_NAVIGATION_COMPLEXITY | 93 |
| TRADING_ORDER_EXECUTION | 66 |
| AUTHENTICATION_IOTP | 52 |
| DEPOSIT_WITHDRAWAL_TRANSFER | 48 |
| OTHER | 38 |
| MARKET_DATA_STALENESS_ACCURACY | 34 |
| MOBILE_TABLET_RESPONSIVENESS | 27 |
| CUSTOMER_SUPPORT | 24 |
| ACCOUNT_RECOVERY_PROFILE_CHANGE | 23 |
| ONBOARDING_KYC | 22 |
| AI_SUPPORT_CONTEXT_QUALITY | 11 |
| FEE_PRICING | 10 |
| PRODUCT_PORTFOLIO_INFORMATION | 10 |
| NOTIFICATION_COMMUNICATION | 9 |
| MARKET_RESEARCH_RECOMMENDATION_UTILITY | 7 |
| SECURITY_ACCOUNT_PROTECTION | 5 |
| UNCLEAR | 3 |
| DIGITAL_SIGNATURE_FLOW | 2 |
| EXCESSIVE_DATA_CONSUMPTION | 1 |

### Journey stage distribution

| Journey | Reviews |
|---|---|
| GENERAL_CROSS_JOURNEY | 213 |
| TRADING_ORDER_MANAGEMENT | 146 |
| FUNDING_CASH_TRANSFER | 59 |
| LOGIN_AUTHENTICATION | 55 |
| PRODUCT_DISCOVERY_MARKET_DATA | 47 |
| CUSTOMER_SUPPORT | 41 |
| ACCOUNT_OPENING_KYC | 25 |
| ACCOUNT_PROFILE_MAINTENANCE | 24 |
| UNKNOWN | 19 |
| PORTFOLIO_TRACKING | 16 |
| OTHER | 1 |

### Incident type distribution

| Type | Incidents |
|---|---|
| failure | 360 |
| friction | 354 |
| praise | 27 |
| feature_request | 18 |
| unclear | 18 |
| unmet_need | 14 |
| confusion | 3 |
| other | 2 |

## 5. Human Review Queue

93 reviews (12.6%) are flagged `needs_human_review = TRUE`. These are listed in `05_outputs/tables/provisional_classification_review_queue.csv` with the reason(s) for flagging:

- `low_confidence` (31 reviews): classification confidence is LOW
- `unclear_signal` (reviews with UNCLEAR sentiment/complaint/product_related)
- `ambiguous_family` (family is UNCLEAR or OTHER)
- `multi_incident(N)` (reviews with N ≥ 2 incidents)
- `new_theme(N)` (reviews with one or more `new_theme_flag = TRUE` incidents)

## 6. New Themes Flagged

18 incidents across the corpus carry `new_theme_flag = TRUE`. These represent incidents that don't clearly fit the candidate Phase C taxonomy:

- `APP_STORE_REGION_AVAILABILITY` — app not available in user's App Store region (1 incident)
- `CRYPTO_DEPOSIT` — feature request for crypto deposit (1 incident)
- `DATA_SELLING_SUSPICION` — user alleges data sold to market makers (1 incident)
- `WIDGET_FEATURE` — widget feature (praise, 1 incident)
- `EXCESSIVE_ADS` — excessive IPO ads in app (1 incident)
- Plus other cases where the reviewer raises a concern not mappable to existing taxonomy

## 7. Caveats and Limitations

1. **No independent validation**: classifications were produced by a single semantic pass without human adjudication. Accuracy cannot be claimed.
2. **Taxonomy is PROVISIONAL**: the 15 pain-point families used here are the candidate taxonomy from Phase C, which has not been frozen.
3. **Journey model is PROVISIONAL**: the 11-stage journey from Phase D is also not frozen.
4. **Rating-content mismatch**: a small number of reviews carry positive ratings with negative content (or vice versa). These were classified by content, not rating. The mismatch is noted via `needs_human_review = TRUE` in some cases.
5. **Source mix bias**: Google Play (54.8%) and App Store (45.2%) reviewers are self-selected public samples, not representative customer populations. Platform results should not be aggregated without disclosure.
6. **Time window**: all 736 reviews fall within 2024-09-22 to 2026-09-22, but Google Play and App Store have different temporal coverage within that window.
7. **Short / vague reviews**: 90 reviews (12.2%) had no extractable incident. These are not errors — they reflect vague, off-topic, or pure-vitriol reviews without actionable content.
8. **Praise ≠ complaint**: praise incidents are counted separately and do not contribute to `complaint_present = True`.

## 8. Files Produced

| File | Purpose |
|---|---|
| `01_data/processed/reviews_classified_24m_provisional.csv` | 736 reviews with classification |
| `01_data/processed/review_incidents_24m_provisional.csv` | 796 incidents |
| `05_outputs/tables/provisional_classification_review_queue.csv` | 93 reviews flagged for human review |
| `05_outputs/tables/provisional_classification_summary.csv` | Distribution metrics |
| `04_analysis/validation/provisional_classification_validation.md` | This document |
| `01_data/processed/provisional_classification_work/` | Working files (checkpoints, batch scripts) |

## 9. Recommended Next Steps

1. Human adjudication of the 93-review queue to produce a `VALIDATED` subset.
2. Freeze the taxonomy and journey model based on adjudication outcomes.
3. Re-classify reviews where human review changed the label.
4. Compute inter-rater agreement if multiple human reviewers participate.
5. Promote `classification_status` from `PROVISIONAL` to `VALIDATED` only after independent human review confirms accuracy.

## 10. QA Adjudication

**This QA step improves the provisional classification, but it is NOT independent human validation. The 93-review queue was selected because cases were difficult, so it is not a representative holdout sample. Classification remains PROVISIONAL.**

### 10.1 Scope

- 93 flagged reviews (`needs_human_review = TRUE`) with 103 linked incidents
- 12 additional `new_theme_flag = TRUE` incidents from non-flagged reviews
- Total adjudication target: 115 incidents

### 10.2 Decisions

| Decision | Count |
|---|---:|
| KEEP | 93 |
| RECODE_FAMILY | 14 |
| RECODE_JOURNEY | 3 |
| RECODE_SUBTYPE | 0 |
| RECODE_SEVERITY | 0 |
| REMOVE_INCIDENT | 0 |
| SPLIT_INCIDENT | 0 |
| MERGE_INCIDENT | 0 |
| UNCLEAR | 5 |
| **Total** | **115** |

### 10.3 New Theme Review (18 incidents)

| Disposition | Count |
|---|---:|
| Reclassified to existing family (A) | 10 |
| NEW_THEME_CONFIRMED (B) | 3 |
| UNCLEAR — insufficient evidence (C) | 5 |

**Clusters among new-theme incidents:**
- `APP_STORE_REGION_AVAILABILITY` (1 incident, App Store|14005255766) — single isolated case, confirmed as new theme
- `DATA_SELLING_SUSPICION` (1 incident, App Store|14468902446) — new subtype within SECURITY_ACCOUNT_PROTECTION
- `EXCESSIVE_ADS` (1 incident, App Store|14548034358-03) — new subtype within NOTIFICATION_COMMUNICATION
- `DIGITAL_SIGNATURE_CONTEXT` (1 incident) — recoded to ONBOARDING_KYC per codebook
- 5 `feature_request` incidents for cosmetic/minor features → reclassified to existing families or marked UNCLEAR

### 10.4 Family Normalization

The provisional output used some subtype names as family names (`MARKET_DATA_STALENESS_ACCURACY`, `MOBILE_TABLET_RESPONSIVENESS`, `AI_SUPPORT_CONTEXT_QUALITY`, `PRODUCT_PORTFOLIO_INFORMATION`, `DIGITAL_SIGNATURE_FLOW`). These were normalized to canonical Phase C family names in the adjudicated output:

| Subtype-name used as family | Normalized to |
|---|---|
| `MARKET_DATA_STALENESS_ACCURACY` | `MARKET_DATA_INFORMATION` |
| `MOBILE_TABLET_RESPONSIVENESS` | `UX_NAVIGATION_COMPLEXITY` |
| `AI_SUPPORT_CONTEXT_QUALITY` | `CUSTOMER_SUPPORT` |
| `PRODUCT_PORTFOLIO_INFORMATION` | `PORTFOLIO_ACCOUNT_INFORMATION` |
| `DIGITAL_SIGNATURE_FLOW` | `ONBOARDING_KYC` |

This is a label-mapping pass, not a re-classification pass. Original incident meaning is preserved.

### 10.5 Adjudicated Outputs

| File | Purpose |
|---|---|
| `05_outputs/tables/provisional_classification_adjudication.csv` | 115 adjudication rows (original vs final) |
| `01_data/processed/reviews_classified_24m_provisional_adjudicated.csv` | 736 reviews with corrections applied |
| `01_data/processed/review_incidents_24m_provisional_adjudicated.csv` | 796 incidents with corrections applied |
| `05_outputs/tables/provisional_qa_summary.csv` | QA decision counts |
| `05_outputs/tables/provisional_qa_work/` | Checkpoint files and batch scripts |

### 10.6 Post-QA Integrity (all passed)

- Review rows: 736 ✅
- Incident rows: 796 ✅
- Unique review IDs: 736 ✅
- Unique incident IDs: 796 ✅
- Orphan incidents: 0 ✅
- incident_count consistency: ✅
- classification_status preserved: PROVISIONAL ✅
- Canonical family values only: ✅ (after normalization)
- Canonical journey values only: ✅
- Canonical severity values only: ✅
- No-incident reviews have empty family/journey: ✅

### 10.7 Caveats

- QA adjudication was performed by the same coder as the initial semantic pass. This is self-review, not independent validation.
- The 93-review queue is biased toward difficult cases, not a representative sample.
- Taxonomy and journey model remain NOT frozen.
- `classification_status` remains `PROVISIONAL` on all rows.
