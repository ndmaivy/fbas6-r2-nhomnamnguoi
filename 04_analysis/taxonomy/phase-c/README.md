# Phase C — README

This directory holds the **candidate** pain-point taxonomy, codebook, and validation artifacts for Phase C. Nothing here is frozen; full-736 automated classification (Phase E) remains blocked until the verification steps below are completed.

## Files in this directory

| File | Purpose |
|---|---|
| `taxonomy_v1_candidate.csv` | 15 problem families with definition, include/exclude rule, positive/hard-negative example. |
| `subtypes_v1_candidate.csv` | 29 provisional subtypes linked to their parent family. |
| `codebook_v1_candidate.md` | Coding rules, multi-label policy, boundary cases, QA gate. |
| `phase_b_to_v1_crosswalk.csv` | Disposition of the 21 Phase B theme codes. |
| `boundary_review_v1_candidate.csv` | 21 difficult checks (10 MATCH, 5 RECODE_FAMILY, 1 RECODE_TYPE, 5 HUMAN_CHECK). |
| `targeted_review_queue.csv` | 16 UNREVIEWED reviews retrieved from outside the Phase B sample. |
| `phase_c_validation.md` | Quality controls, unresolved decisions, freeze gate. |
| `README.md` | This file — verification checklist to close Phase C. |

## What is already done

- 21 boundary cases adjudicated by the human reviewer (10 MATCH, 5 RECODE_FAMILY accepted, 1 RECODE_TYPE accepted, 5 HUMAN_CHECK resolved).
- 16 candidate reviews queued for the 8 sparse themes that had keyword hits.
- All Phase B source artifacts (100 reviews, 146 incidents, 21 themes) untouched.
- All cross-references between files validated by `python -c "..."` checks.

## What still needs verification to close Phase C

### 1. Adjudicate the targeted review queue

Open `targeted_review_queue.csv`. For each of the 16 rows, decide one of:

- `CONFIRMED_INCIDENT` — review is a real complaint of the suggested theme.
- `CONFIRMED_HARD_NEGATIVE` — keyword hit but review is praise, off-topic, or sarcasm.
- `OTHER_THEME` — real incident but belongs to a different family.
- `NO_INCIDENT` — no incident at all.
- `UNCLEAR` — insufficient evidence.

Reply in the format:

```
#<row> <source> <review_id> → <DECISION> | <correct theme if OTHER_THEME> | <one-line reason>
```

### 2. Update taxonomy status based on queue results

After adjudication, the following themes may change status in `taxonomy_v1_candidate.csv`:

- `FEE_PRICING`, `ACCOUNT_RECOVERY_PROFILE_CHANGE`, `MOBILE_TABLET_RESPONSIVENESS`, `MARKET_DATA_INFORMATION`, `AI_SUPPORT_CONTEXT_QUALITY`, `NOTIFICATION_COMMUNICATION`, `SECURITY_ACCOUNT_PROTECTION`, `DIGITAL_SIGNATURE_FLOW` — each has 2 queue candidates.
- `EXCESSIVE_DATA_CONSUMPTION` and `MARKET_RESEARCH_RECOMMENDATION_UTILITY` — no candidates retrieved; status stays `PROVISIONAL_SPARSE` with note "no extra evidence in queue".

Promotion rule: a theme stays `PROVISIONAL_SPARSE` unless the queue adds at least one confirmed incident outside the Phase B sample. Numeric count is not a promotion threshold.

### 3. Record adjudication in a new file

Create `targeted_review_queue_adjudicated.csv` with columns:

```
source,review_id,retrieval_theme,decision,correct_theme,reason
```

### 4. Update `phase_c_validation.md`

Add a section "Targeted queue adjudication" with:

- Counts per decision.
- Which themes gained confirmed incidents.
- Which themes only got hard negatives.
- Confirmation that `EXCESSIVE_DATA_CONSUMPTION` and `MARKET_RESEARCH_RECOMMENDATION_UTILITY` remain `PROVISIONAL_SPARSE` with no extra evidence.

### 5. Update `todo.md`

- Mark the queue-rà todo as completed.
- Keep Phase C status as "candidate adjudicated, not frozen" until independent human agreement is obtained.

## What is NOT required to close Phase C

- Freezing taxonomy v1 — blocked by absent second human coder.
- Running full-736 classification — blocked by unfrozen taxonomy and unfrozen journey model.
- Modifying any Phase B artifact or the 736-row analysis dataset.

## Verification commands

After steps 1–5, run from the repository root:

```powershell
python -m py_compile 02_src/classification/prepare_phase_c_review_queue.py
python -c "import pandas as pd; ..."
```

The full integrity check (15 families, 29 subtypes, 21 crosswalk, 21 boundary, 16 queue, Phase B 100/146/21) is documented in `phase_c_validation.md`.

## Phase C close criterion

Phase C is **closed at the candidate level** when:

1. `targeted_review_queue_adjudicated.csv` exists with 16 rows.
2. `taxonomy_v1_candidate.csv` `status` column reflects queue results.
3. `phase_c_validation.md` records the queue adjudication.
4. `todo.md` Phase C section is updated.

Phase C is **frozen** only when an independent human coder has validated the codebook on a held-out set and agreement is acceptable. Until then, treat all artifacts as proposals.
