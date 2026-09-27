# Phase C validation and freeze gate — v1 candidate

## Work completed

- `taxonomy_v1_candidate.csv`: 15 problem families; 7 supported **in the selected Phase B sample**, 2 provisional splits of the broad product/portfolio information family, 6 sparse provisional families. Each row has a definition, include/exclude rule and keyed positive/hard-negative example.
- `subtypes_v1_candidate.csv`: 29 **provisional** subtypes linked to their parent family with a traceable example; `DIGITAL_SIGNATURE_CONTEXT` explicitly requires journey verification.
- `codebook_v1_candidate.md`: hierarchy and subtype proposals, multi-incident/multi-label rules, uncertainty and request/praise handling, explicit boundary cases with source review IDs.
- `phase_b_to_v1_crosswalk.csv`: the 21 assessed Phase B theme codes and their proposed destinations; the additional incident state `NONE` is handled separately. Ambiguous information incidents require quote-level review rather than an automatic remap.
- `boundary_review_v1_candidate.csv`: 21 difficult checks (19 real incidents plus 2 zero-incident reviews). Results: 10 `MATCH`, 5 `RECODE_FAMILY`, 1 `RECODE_TYPE`, 5 `HUMAN_CHECK`. These are **proposed** Phase C decisions, not adjudicated ground truth.
- `targeted_review_queue.csv`: 16 unique, previously unsampled reviews retrieved from the remaining 636 using documented regexes. Every row is `UNREVIEWED`; the retrieval theme is a **search hint**, never a label. Eight of the ten Phase B sparse themes have up to two candidates; no conservative keyword hit was found for `EXCESSIVE_DATA_CONSUMPTION` or `MARKET_RESEARCH_RECOMMENDATION_UTILITY`. That does not establish absence of those problems.

## Quality controls run

- All 15 family codes are unique. All positive/hard-negative examples and all 21 boundary-case keys were found in the Phase B final review table; all 19 incident IDs belong to the given `(source, review_id)` and have the stated Phase B family.
- The 21 crosswalk counts were checked against Phase B `theme_family` counts. `NONE` is an incident coding outcome outside the 21 assessed themes; don't use it as a complaint.
- The queue excludes the 100 Phase B sample keys, contains no duplicate `(source, review_id)`, retains original title/raw text and does not populate any proposed family.

## Decisions deliberately left open

1. **No independent human agreement:** all Phase B final labels say `ChatGPT (single reviewer; AI-assisted)`. A second human coder or explicit human adjudication is required before treating the candidate codebook as validated. Do not silently rename `reviewer` or claim validation.
2. **Split the 13 Phase B `PRODUCT_PORTFOLIO_INFORMATION` incidents** by evidence into market data vs portfolio/account information vs research utility. Some incidents are praise or requests and must not enter complaint counts.
3. **Check the five `HUMAN_CHECK` boundary cases**: signature flow journey, inferred deposit typo, ticker-aware AI assistant, research usefulness and validity of name-like text. Keep MEDIUM/LOW confidence where evidence cannot disambiguate.
4. **Inspect the targeted queue by reading titles and raw text.** Keyword hits can be praise, generic support requests or unrelated security accusations. Add true incidents and hard negatives separately, then reassess the 10 sparse themes. Zero hits from conservative retrieval is not zero real-world instances.
5. **Do not promote on a numeric threshold:** 7 is a Phase B sampling heuristic, not a statistical or product impact cutoff. Human reviewers must decide family boundaries and independently verify subtype rules.
6. **Customer journey is only a provisional location field here.** Freeze the journey model in Phase D after checking actual cross-channel steps; don't assume every app freeze happened during Trading.

**Phase C status:** candidate taxonomy and executable coding guidance prepared; **not frozen**. Full-736 automated classification (Phase E) remains blocked pending independent validation, adjudication, codebook acceptance and journey-model freeze. No Phase B source artifact or canonical raw review was modified for this Phase C draft.

## Targeted Queue Adjudication

### Scope

- Total candidates adjudicated: **16**
- Targeted themes assessed: **8** (2 candidates per theme)
- Non-retrieved sparse themes (no conservative extra hits): **2** — `EXCESSIVE_DATA_CONSUMPTION`, `MARKET_RESEARCH_RECOMMENDATION_UTILITY`

### Decision distribution

| Decision | Count |
|---|---:|
| CONFIRMED_INCIDENT | 11 |
| CONFIRMED_HARD_NEGATIVE | 3 |
| OTHER_THEME | 2 |
| NO_INCIDENT | 0 |
| UNCLEAR | 0 |

### Results by retrieval theme

| Retrieval theme | Confirmed | Hard negative | Other theme | No incident | Unclear |
|---|---:|---:|---:|---:|---:|
| FEE_PRICING | 1 | 1 | 0 | 0 | 0 |
| ACCOUNT_RECOVERY_PROFILE_CHANGE | 2 | 0 | 0 | 0 | 0 |
| MOBILE_TABLET_RESPONSIVENESS | 1 | 1 | 0 | 0 | 0 |
| MARKET_DATA_STALENESS_ACCURACY | 2 | 0 | 0 | 0 | 0 |
| AI_SUPPORT_CONTEXT_QUALITY | 1 | 1 | 0 | 0 | 0 |
| NOTIFICATION_COMMUNICATION | 2 | 0 | 0 | 0 | 0 |
| SECURITY_ACCOUNT_PROTECTION | 0 | 0 | 2 | 0 | 0 |
| DIGITAL_SIGNATURE_FLOW | 2 | 0 | 0 | 0 | 0 |

### Themes gaining additional support

- **ACCOUNT_RECOVERY_PROFILE_CHANGE** — 2 confirmed incidents outside Phase B sample (phone number change delayed one week; CCCD update failing repeatedly). Evidence is consistent with the existing definition. Status remains `PROVISIONAL_SPARSE`; the existing status vocabulary does not contain a stronger state, and 2 confirmed incidents is not sufficient for automatic promotion.
- **NOTIFICATION_COMMUNICATION** — 2 confirmed incidents outside Phase B sample (excessive referral notifications; persistent undismissable "no internet" notification). Evidence is consistent with the existing definition. Status remains `PROVISIONAL_SPARSE` for the same reason.
- **MARKET_DATA_STALENESS_ACCURACY** (subtype of `MARKET_DATA_INFORMATION`) — 2 confirmed incidents outside Phase B sample (missing percentage change on price board; widget lagging behind market price board). Parent family `MARKET_DATA_INFORMATION` retains `PROVISIONAL_SPLIT`.
- **DIGITAL_SIGNATURE_FLOW** (subtype of `ONBOARDING_KYC`) — 2 confirmed incidents outside Phase B sample (forced FPT digital signature registration with no exit; forced digital signature when other apps do not require it). Parent family `ONBOARDING_KYC` retains `SUPPORTED_IN_SAMPLE`.
- **MOBILE_TABLET_RESPONSIVENESS** (subtype of `UX_NAVIGATION_COMPLEXITY`) — 1 confirmed incident outside Phase B sample (app cannot open on iPad Pro M4). Parent family `UX_NAVIGATION_COMPLEXITY` retains `SUPPORTED_IN_SAMPLE`.
- **AI_SUPPORT_CONTEXT_QUALITY** (subtype of `CUSTOMER_SUPPORT`) — 1 confirmed incident outside Phase B sample (AI support described as terrible). Parent family `CUSTOMER_SUPPORT` retains `SUPPORTED_IN_SAMPLE`.
- **FEE_PRICING** — 1 confirmed incident outside Phase B sample (custody fee interest accruing at high rate, not auto-deducted). Status remains `PROVISIONAL_SPARSE`; 1 confirmed incident is not sufficient for promotion.

### Themes remaining sparse

- **FEE_PRICING** — 1 confirmed + 1 hard negative. Remains `PROVISIONAL_SPARSE`.
- **SECURITY_ACCOUNT_PROTECTION** — 0 confirmed; 2 other-theme recodes (both to `DEPOSIT_WITHDRAWAL_TRANSFER`). Remains `PROVISIONAL_SPARSE`. The keyword hits ("lừa đảo", "an toàn kém") reflect user perception of fraud or theft, not a security-design concern as defined by the family. Per codebook rule, treat such wording as user perception, not verified fraud.
- **EXCESSIVE_DATA_CONSUMPTION** — no candidates retrieved. Remains `PROVISIONAL_SPARSE`. No conservative extra hits is insufficient additional evidence, not evidence of absence.
- **MARKET_RESEARCH_RECOMMENDATION_UTILITY** — no candidates retrieved. Remains `PROVISIONAL_SPARSE`. Same reasoning.

### Hard negatives (useful boundary evidence)

- **FEE_PRICING** — `cebce133-8708-41d3-9a75-e7da72962539`: keyword "miễn phí giao dịch" matched but review is praise about free trading. Confirms the codebook rule that low-fee praise is not a fee complaint.
- **MOBILE_TABLET_RESPONSIVENESS** — `12956820659`: keyword "font" matched but review is a feature request for a font size option; current state described as "quá tốt". Confirms that font-size requests are feature requests, not responsiveness failures.
- **AI_SUPPORT_CONTEXT_QUALITY** — `13388783260`: keyword "chatbot" matched but review is praise about chatbot convenience. Confirms that chatbot praise is not an AI quality complaint.

### Other-theme recodes

- **SECURITY_ACCOUNT_PROTECTION → DEPOSIT_WITHDRAWAL_TRANSFER** — `12166129599`: "Lừa đảo giam tiền của người dùng sau khi nhận chuyển khoản". Per codebook rule, "lừa đảo" is user perception, not verified fraud. The actual issue described is funds being held after transfer, which maps to `DEPOSIT_WITHDRAWAL_TRANSFER`.
- **SECURITY_ACCOUNT_PROTECTION → DEPOSIT_WITHDRAWAL_TRANSFER** — `1fbfc074-a707-4bea-bc45-78e494045b90`: "An toàn kém. Bán cp xong tiền mất 2,5% k bit đi đâu. Ăn cắp tài sản". Per codebook rule, "an toàn kém" and "ăn cắp" are user perception, not verified security breach. The actual issue described is unexplained 2.5% balance loss after selling stocks, which maps to `DEPOSIT_WITHDRAWAL_TRANSFER`.

### Unresolved cases

- None. All 16 candidates received a definitive decision.

### Taxonomy status changes

- **No status changes applied.** All themes retain their current status values. The existing status vocabulary (`SUPPORTED_IN_SAMPLE`, `PROVISIONAL_SPLIT`, `PROVISIONAL_SPARSE`) does not contain a stronger state for the themes that gained additional confirmed incidents. Per the rules, no new status values were invented. Additional evidence is documented above.

### Limitation wording

The targeted review queue is a **purposive validation sample**, not a representative sample. Keyword retrieval is used to find possible evidence, not to estimate prevalence. Counts in this queue must **NOT** be extrapolated to:

- the 736-review analysis dataset
- the full review population
- TCInvest customers generally

**Phase C status after this task:** Candidate adjudicated — not frozen. Taxonomy freeze remains blocked until an independent human coder validates the candidate codebook on a held-out review set with acceptable agreement and disagreements are adjudicated.
