# Manual Label Recovery Audit

## Search Scope

- Project files searched: **208**
- Included types: CSV, XLSX, XLS, JSON, JSONL, Markdown, IPYNB, Parquet and PKL
- `.venv` excluded as environment content, not project evidence
- Candidate files found by filename/content terms: **24**

Candidate paths:

- `00_docs/methodology/analysis_scope.md`
- `00_docs/methodology/data_collection_log.md`
- `01_data/interim/google_play_standardized.csv`
- `01_data/interim/reviews_merged_standardized.csv`
- `01_data/processed/reviews_clean_full.csv`
- `01_data/raw/google_play/2026-09-22_google_play_raw.csv`
- `04_analysis/taxonomy/manual_review_sample_24m.csv`
- `04_analysis/taxonomy/manual_review_sample_v0.md`
- `04_analysis/taxonomy/taxonomy_v0.md`
- `04_analysis/validation/app_store_candidate_validation.md`
- `04_analysis/validation/app_store_recency_gap_audit.md`
- `04_analysis/validation/data_quality_audit.md`
- `04_analysis/validation/manual_review_reuse_24m.md`
- `05_outputs/tables/TCInvest_manual_review_batch01.xlsx`
- `05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json`
- `05_outputs/tables/TCInvest_manual_review_incomplete.xlsx`
- `05_outputs/tables/data_quality_issues.csv`
- `05_outputs/tables/data_quality_summary.csv`
- `05_outputs/tables/manual_review_overlap_24m.csv`
- `05_outputs/tables/manual_review_sample_24m_summary.csv`
- `05_outputs/tables/manual_review_sample_v0.csv`
- `AGENTS.md`
- `README.md`
- `todo.md`

## Candidate Inspection

| path | file_type | rows | sheets | rows_with_manual_labels | complete_or_reviewed | needs_second_review | has_source | has_review_id | assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00_docs/methodology/analysis_scope.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 00_docs/methodology/data_collection_log.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 01_data/interim/google_play_standardized.csv | csv | 3223 |  | 0 | 0 | 0 | True | True | Not a row-level recovery source |
| 01_data/interim/reviews_merged_standardized.csv | csv | 3745 |  | 0 | 0 | 0 | True | True | Not a row-level recovery source |
| 01_data/processed/reviews_clean_full.csv | csv | 3745 |  | 0 | 0 | 0 | True | True | Not a row-level recovery source |
| 01_data/raw/google_play/2026-09-22_google_play_raw.csv | csv | 3223 |  | 0 | 0 | 0 | True | False | Not a row-level recovery source |
| 04_analysis/taxonomy/manual_review_sample_24m.csv | csv | 100 |  | 7 | 0 | 7 | True | True | Not a row-level recovery source |
| 04_analysis/taxonomy/manual_review_sample_v0.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 04_analysis/taxonomy/taxonomy_v0.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 04_analysis/validation/app_store_candidate_validation.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 04_analysis/validation/app_store_recency_gap_audit.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 04_analysis/validation/data_quality_audit.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 04_analysis/validation/manual_review_reuse_24m.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 05_outputs/tables/TCInvest_manual_review_batch01.xlsx | xlsx | 3745 | Reviews, Review Progress, Codebook | 50 | 49 | 1 | True | True | Usable primary row-level source: 49 REVIEWED + 1 NEEDS_SECOND_REVIEW |
| 05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json | json | 20 |  | 20 | 14 | 6 | False | True | Usable label source when exact-joined to batch01 roster: 14 final + 6 second-review |
| 05_outputs/tables/TCInvest_manual_review_incomplete.xlsx | xlsx | 3682 | Incomplete Reviews, Progress Summary, Completion Rules, Original Progress, Codebook | 7 | 0 | 7 | True | True | Not a row-level recovery source |
| 05_outputs/tables/data_quality_issues.csv | csv | 10 |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 05_outputs/tables/data_quality_summary.csv | csv | 45 |  | 0 | 0 | 0 | True | False | Not a row-level recovery source |
| 05_outputs/tables/manual_review_overlap_24m.csv | csv | 7 |  | 7 | 0 | 6 | True | True | Not a row-level recovery source |
| 05_outputs/tables/manual_review_sample_24m_summary.csv | csv | 20 |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| 05_outputs/tables/manual_review_sample_v0.csv | csv | 56 |  | 56 | 0 | 0 | True | True | Row-level exploratory artifact, but explicitly superseded/disputed; excluded from recovery |
| AGENTS.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| README.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |
| todo.md | md | N/A |  | 0 | 0 | 0 | False | False | Not a row-level recovery source |

## Usable Row-Level Sources

1. `05_outputs/tables/TCInvest_manual_review_batch01.xlsx::Reviews` contains **49 actual REVIEWED rows** and **1 actual NEEDS_SECOND_REVIEW row**, with source, review ID and manual fields.
2. `05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json + exact review_id join to batch01 roster` contains **14 final rows** (`needs_second_review=NO`) and **6 second-review rows**. The JSON does not store `source`; every JSON review ID was verified to occur exactly once in the batch01 roster, allowing an exact, deterministic source lookup. No review-text or fuzzy matching was used.

`manual_review_sample_v0.csv` contains 56 row-level exploratory labels, but its accompanying documentation explicitly marks it as disputed/superseded and not suitable as ground truth. It is not part of the historical 63/7 recovery chain.

Summary-only Markdown/CSV files and the current incomplete/sample outputs are not recovery sources for missing COMPLETE rows.

## Provenance and Recovery

- Batch01 COMPLETE: **49**
- Batch02 COMPLETE: **14**
- Recovered COMPLETE total: **63**
- Unique recovered `(source, review_id)` keys: **63**
- Duplicate recovered keys: **0**
- Independently evidenced second-review rows: **7**
- Total inspected evidence reconstructed from actual rows: **70**

This exactly matches the historical report of 70 inspected = 63 COMPLETE + 7 NEEDS_SECOND_REVIEW.

## 24-Month Match

Matching used `(source, review_id)` only.

- Recovered COMPLETE inside 24 months: **63**
- Recovered COMPLETE outside 24 months: **0**
- Unmatched recovered COMPLETE: **0**

## Required-Label Completeness

- `manual_validity` missing: **0**
- `sentiment` missing: **0**
- `complaint_present` missing: **0**
- `pain_point_primary` missing: **0**
- `journey_primary` missing: **0**
- `severity` missing: **0**
- `product_related` missing: **0**
- `feature_request` missing: **0**
- `evidence_span` missing: **0**
- `confidence` missing: **0**

No missing label was filled or inferred.

## Recovery Assessment

- Provenance confidence: **High**
- Recovery status: **Complete** relative to the historical 63 COMPLETE / 7 second-review report
- Recovery output: `05_outputs/tables/recovered_complete_manual_labels.csv`

## Limitations

- Batch02 source metadata require an exact roster join because the JSON did not record `source`; uniqueness was explicitly verified before the join.
- `REVIEWED` and `needs_second_review=NO` are treated as the historical workflow's completion evidence. No label meaning was changed.
- This audit does not modify the current 100-review manual sample. Recovered rows should be incorporated only in a separate follow-up task.
- No taxonomy, classification, pain-point frequency or business insight was produced.
