# Phase B — Exploratory Discovery (final AI-assisted deliverables)

## Scope and files

Source population: `01_data/processed/reviews_analysis_24m.csv`, 736 reviews in the inclusive UTC window 2024-09-22 to 2026-09-22. Use `(source, review_id)` for joins. `review_text_raw` in the analysis dataset is authoritative; do not infer actual review language from collection locale or storefront.

This folder's **final** deliverables are:

- `phase_b_final.xlsx`: three sheets (`Reviews`, `Incidents`, `Themes`).
- `phase_b_reviews_final.csv`, `phase_b_incidents_final.csv`, `phase_b_themes_final.csv`: machine-readable exports of those sheets.
- This methodology and limitations note.

The final tables have 100 reviews (65 Google Play, 35 App Store), 146 incidents associated with 98 reviews, and 21 assessed themes. Two reviews have zero incidents. The sample combines 50 recovered Batch 01 labels, 20 recovered Batch 02 labels and 30 newly selected reviews; `sample_origin` records these origins, **not** the present completion state. Source/time/length mix was deliberately broadened: rating bands LOW/MID/HIGH = 60/15/25; four six-month periods = 16/15/15/54; VERY_SHORT/NORMAL/LONG = 10/66/24. Selection used seed 42. This is a discovery sample, **not** a representative sample or a frequency estimate for all 736 reviews.

## Final schemas and pruning

`Reviews` retains the composite key, date/rating, App Store title, original text, optional app version, sample origin, review-level labels, evidence, uncertainty, reviewer notes and review decision. `manual_validity` is retained because **one** review is `REVIEW` rather than `VALID`; `validity_note` retains the four existing validity/ambiguity notes. Blank `issue_summary` on some rows remains blank rather than inventing summaries.

`Incidents` retains its ID, parent review key, user goal/context/expected and actual outcomes/friction/consequence, verbatim evidence, incident type, specific `candidate_theme`, mapped `theme_family`, journey, confidence and notes. `Themes` retains the 21 decisions, incident counts, priority tiers and reviewer assessment.

The final tables omit empty `detected_language`/`language_detection_method`, source-specific vote counts, collector/user metadata, cleaning flags, duplicate `incidents_json`, constant `REVIEWED`/`COMPLETE`/`NO` flags, construction-only sampling columns and intermediate evidence-fix markers. These remain available through the tracked 24-month dataset and the methodology. The workbook may normalize embedded CRLF to LF; **the review CSV and the analysis dataset preserve original raw text**.

## Coding and assessment

- Read both title and raw text. A review can contain zero, one or multiple atomic incidents; each incident describes what the user tried to do, what occurred, friction and consequence. Do not infer a technical root cause or treat an accusation as proven fraud.
- Ratings do not determine sentiment or severity. Requests about improving an existing attribute can express a complaint; requests for a new capability remain feature requests. Praise is not a pain point.
- 7 theme families are `SUPPORTED_RECURRING`; `PRODUCT_PORTFOLIO_INFORMATION` needs a split; `FEATURE_REQUEST`, `OTHER` and `UNCLEAR` need reframing as request type/catch-all/uncertainty, rather than stable pain-point families.
- 10 themes remain `NEEDS_MORE_SAMPLE`: 2 near-threshold (5 incidents), 4 emerging (2 each), 4 backlog (1 each). The 7-incident reference is an **exploratory prioritization heuristic**, not a validated promotion threshold. `Themes.incident_count` includes all incident types, including praise; never treat these counts as complaint prevalence.
- One review (`07616126-4fd6-4860-a991-a0a6ea51f192`, “mong đợi”) remains `UNCLEAR_FINAL` because text alone cannot distinguish praise from unmet expectation. It has zero incidents by design. Review `13732893373` is coded as a deposit complaint based on an inferred typo in the title; its confidence remains MEDIUM. There are zero open `needs_second_review` flags in the final source.

## Integrity and limitations

Final exports were checked against the 736-row analysis dataset: 100 unique `(source, review_id)` keys, 146 unique incident IDs, incident counts per review and theme matching the source, and all review/incident `evidence_span` values exact substrings of the original title or text. Raw text, rating and date in the review CSV match the source data. Earlier work corrected 26 incident and 20 review evidence spans, including one cross-review copy error; the final files contain the corrected quotes.

All 100 rows still identify their reviewer as `ChatGPT (single reviewer; AI-assisted)`. **Final here means the Phase B AI-assisted discovery artifact is frozen for handoff; it is not independently human-validated ground truth.** No independent second reviewer or human sign-off is recorded. Public app reviews are self-selected and do not represent unique customers or all customers. Future human validation and a full codebook with definitions, include/exclude rules, hard negatives and boundary cases belong in Phase C before full-dataset classification or any claim of validated taxonomy.
