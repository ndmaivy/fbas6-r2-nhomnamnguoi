# Manual Review Reuse — 24-Month Final Sample

## Recovery Status

- COMPLETE labels recovered: **63**
- NEEDS_SECOND_REVIEW labels retained: **7**
- Unique inspected evidence: **70**
- Inspected keys already present in the pre-recovery sample: **18**
- Inspected keys absent from the pre-recovery sample: **52**

All inspected evidence was matched by `(source, review_id)` and retained. COMPLETE labels came only from `recovered_complete_manual_labels.csv`; second-review labels came from `TCInvest_manual_review_incomplete.xlsx`. No label was inferred or resolved.

## Rebuild and Sampling Method

- Final target: **100 unique reviews**
- New reviews required and selected: **30**
- New rows reused from the pre-recovery sample: **18**
- Additional new rows drawn from the analysis dataset: **12**
- Random seed: **42**

The 70 inspected rows were retained regardless of imbalance. Their starting distribution was Google Play/App Store = {'Google Play': 65, 'App Store': 5}, rating bands = {'LOW': 43, 'HIGH': 19, 'MID': 8}, time periods = {'P1': 7, 'P2': 4, 'P3': 5, 'P4': 54}, and text-length bands = {'NORMAL': 56, 'LONG': 7, 'VERY_SHORT': 7}.

New selection used dynamically calculated deficits against these diversity targets:

- Source: approximate 24-month dataset mix where feasible
- Rating: LOW 60%, MID 15%, HIGH 25%
- Time: four equal six-month periods
- Length: VERY_SHORT 10%, NORMAL 65%, LONG 25% (`LONG >= 200` characters)

Because existing evidence was heavily Google Play/P4, source and time targets were not achievable without dropping inspected rows. New rows therefore prioritize App Store and earlier periods. Previously sampled unreviewed rows receive a deterministic preference when they also fill diversity deficits.

## Final Sample Validation

- Rows and unique keys: **100 / 100**
- COMPLETE: **63**
- NEEDS_SECOND_REVIEW: **7**
- NEW_SAMPLE_UNREVIEWED: **30**
- Sources: {'Google Play': 65, 'App Store': 35}
- Rating bands: {'LOW': 60, 'HIGH': 25, 'MID': 15}
- Time periods: {'P1': 16, 'P2': 15, 'P3': 15, 'P4': 54}
- Text-length bands: {'NORMAL': 66, 'LONG': 24, 'VERY_SHORT': 10}
- All keys belong to the 736-row dataset: **Yes**
- COMPLETE labels preserved exactly: **Yes**
- Second-review labels preserved: **Yes**
- New manual fields blank: **Yes**

## Taxonomy Coverage from 63 COMPLETE Labels

- Pain-point primary: {'PERFORMANCE_RELIABILITY': 16, 'UX_NAVIGATION_COMPLEXITY': 9, 'NONE': 7, 'AUTHENTICATION_IOTP': 7, 'DEPOSIT_WITHDRAWAL_TRANSFER': 5, 'ONBOARDING_KYC': 5, 'TRADING_ORDER_EXECUTION': 4, 'FEATURE_REQUEST': 3, 'CUSTOMER_SUPPORT': 3, 'PRODUCT_PORTFOLIO_INFORMATION': 2, 'FEE_PRICING': 1, 'OTHER': 1}
- Journey primary: {'GENERAL_CROSS_JOURNEY': 27, 'TRADING_ORDER_MANAGEMENT': 7, 'LOGIN_AUTHENTICATION': 7, 'FUNDING_CASH_TRANSFER': 6, 'ACCOUNT_OPENING_KYC': 5, 'CUSTOMER_SUPPORT': 4, 'PRODUCT_DISCOVERY_MARKET_DATA': 3, 'ACCOUNT_PROFILE_MAINTENANCE': 1, 'PORTFOLIO_TRACKING': 1, 'OTHER': 1, 'UNCLEAR': 1}
- Severity: {'MEDIUM': 24, 'HIGH': 18, 'LOW': 14, 'NONE': 7}
- Sentiment: {'NEGATIVE': 51, 'POSITIVE': 8, 'MIXED': 3, 'NEUTRAL': 1}
- Complaint present: {'YES': 55, 'NO': 8}
- Product related: {'YES': 63}
- Feature request: {'NO': 56, 'YES': 7}
- Reviews with secondary pain points: **20**
- Multi-pain-point reviews: **20**
- Reviews containing UNCLEAR: **10**
- Primary pain point NONE: **7**
- Primary pain point or journey OTHER: **2**
- Feature-request reviews: **7**

Represented pain-point categories: ['NONE', 'PERFORMANCE_RELIABILITY', 'UX_NAVIGATION_COMPLEXITY', 'ONBOARDING_KYC', 'AUTHENTICATION_IOTP', 'TRADING_ORDER_EXECUTION', 'DEPOSIT_WITHDRAWAL_TRANSFER', 'CUSTOMER_SUPPORT', 'FEE_PRICING', 'PRODUCT_PORTFOLIO_INFORMATION', 'FEATURE_REQUEST', 'OTHER']

Pain-point categories with zero evidence: ['COMMUNITY_MODERATION', 'NOTIFICATION_COMMUNICATION', 'LOCALIZATION_LANGUAGE', 'SECURITY_ACCOUNT_PROTECTION', 'UNCLEAR']

Represented journey categories: ['GENERAL_CROSS_JOURNEY', 'ACCOUNT_OPENING_KYC', 'LOGIN_AUTHENTICATION', 'PRODUCT_DISCOVERY_MARKET_DATA', 'TRADING_ORDER_MANAGEMENT', 'PORTFOLIO_TRACKING', 'FUNDING_CASH_TRANSFER', 'CUSTOMER_SUPPORT', 'ACCOUNT_PROFILE_MAINTENANCE', 'OTHER', 'UNCLEAR']

Journey categories with zero evidence: ['COMMUNITY_SOCIAL']

Zero evidence does not imply that a Codebook category should be removed.

## Human Review Workload

- COMPLETE — no action: **63**
- NEEDS_SECOND_REVIEW — human resolution: **7**
- NEW_SAMPLE_UNREVIEWED — human labeling: **30**

## Limitations

- The sample is intentionally optimized for taxonomy discovery/validation, not prevalence estimation.
- The 70 historical inspected rows are source/time imbalanced and were not dropped.
- No taxonomy refinement, classification, second-review resolution, pain-point ranking or business inference was performed.
