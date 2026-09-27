# Data Cleaning Log

## Input Dataset

- File: `01_data/interim/reviews_merged_standardized.csv`
- Rows: 3,745
- Google Play: 3,223
- App Store: 522
- Duplicate `(source, review_id)` keys: 0

## Cleaning Rules

A record is rejected only when at least one reproducible core validity rule fails:

1. `review_id` is missing or whitespace-only.
2. `review_date` is missing or cannot be parsed as a datetime.
3. `rating` cannot be parsed or is not one of 1, 2, 3, 4, or 5.
4. `review_text_raw` is missing, empty, or whitespace-only.
5. A deterministic rule confirms invalid/spam content. No such rule was justified or applied in this run.

Duplicate keys cause the script to stop rather than choose a record automatically. No time-range filter is applied. Ratings, dates, app versions, collection locales, language fields, and review polarity are not used to remove otherwise valid records.

## Records Removed

- Missing review ID: 0
- Invalid/missing date: 0
- Invalid/missing rating: 0
- Empty/whitespace-only text: 0
- Confirmed invalid/spam: 0
- Total rejected: 0

## Records Retained Intentionally

- Very short reviews (`review_char_length <= 10`): 533
- Exact duplicate-text records with distinct review keys: 417 records across 69 groups
- Missing `app_version`: 459
- Missing `detected_language`: 3,745

These records remain valid. Short or identical wording does not establish that a review or user is duplicated.

## Text Cleaning

`review_text_raw` is preserved unchanged. `review_text_clean` is produced only by:

1. converting CRLF/CR line endings to LF;
2. trimming leading and trailing whitespace;
3. collapsing consecutive whitespace, including line breaks, to one ordinary space.

Vietnamese diacritics, emoji, punctuation, spelling, casing, and wording are preserved. No translation, stemming, lemmatization, stopword removal, or paraphrasing is performed.

## Quality Flags

- `review_char_length`: Unicode character count of `review_text_clean`.
- `review_word_count`: count of non-whitespace token-like sequences.
- `is_very_short`: `True` when cleaned text contains at most 10 characters.
- `is_exact_duplicate_text`: `True` when the exact `review_text_raw` occurs more than once across the full dataset.
- `exact_duplicate_group_id`: stable SHA-256-derived identifier for the exact raw text; null/empty for non-duplicates.
- `missing_app_version`: `True` when `app_version` is empty.
- `suspected_spam`: defaults to `False`; no deterministic suspicion rule was applied.
- `is_valid_for_analysis`: `True` only when all core validity rules pass.
- `removal_reason`: semicolon-separated failed rules; null/empty for retained records.

## Output Dataset

- Clean file: `01_data/processed/reviews_clean_full.csv`
- Rejected file: `01_data/processed/reviews_rejected.csv`
- Clean rows: 3,745
- Google Play: 3,223
- App Store: 522
- Date range: 2015-08-13T11:10:30+00:00 to 2026-09-21T12:13:27+00:00
- Timezone validation: All retained dates parse consistently to UTC.
- Rating distribution:
- 1 star: 2,016
- 2 star: 236
- 3 star: 175
- 4 star: 151
- 5 star: 1,167

## Limitations

- Duplicate content does not imply a duplicate person or review; distinct `(source, review_id)` keys are retained.
- Very short reviews can be valid but may provide insufficient context for later pain-point classification.
- Missing app versions are retained and not imputed.
- Actual review language has not been detected; `collection_locale` is not substituted for `detected_language`.
- `suspected_spam=False` means no deterministic flag rule fired, not that content was manually verified as non-spam.
- This is the full available history and does not represent a selected analysis time range.
