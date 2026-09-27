#!/usr/bin/env python3
"""Reuse available manual work and prepare a diverse 24-month review sample."""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_PATH = ROOT / "01_data/processed/reviews_analysis_24m.csv"
WORKBOOK_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_incomplete.xlsx"
CLEAN_PATH = ROOT / "01_data/processed/reviews_clean_full.csv"
MERGED_STANDARDIZED_PATH = ROOT / "01_data/interim/reviews_merged_standardized.csv"
RAW_GP_PATH = ROOT / "01_data/raw/google_play/2026-09-22_google_play_raw.csv"
RAW_AS_PATH = ROOT / "01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv"

SAMPLE_PATH = ROOT / "04_analysis/taxonomy/manual_review_sample_24m.csv"
OVERLAP_PATH = ROOT / "05_outputs/tables/manual_review_overlap_24m.csv"
SUMMARY_PATH = ROOT / "05_outputs/tables/manual_review_sample_24m_summary.csv"
REPORT_PATH = ROOT / "04_analysis/validation/manual_review_reuse_24m.md"

TARGET_SIZE = 100
RANDOM_SEED = 42
START = pd.Timestamp("2024-09-22T00:00:00Z")
END = pd.Timestamp("2026-09-22T23:59:59Z")
RATING_TARGET_SHARES = {"LOW": 0.60, "MID": 0.15, "HIGH": 0.25}
TIME_TARGET_SHARES = {"P1": 0.25, "P2": 0.25, "P3": 0.25, "P4": 0.25}
LENGTH_TARGET_SHARES = {"VERY_SHORT": 0.10, "NORMAL": 0.65, "LONG": 0.25}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_blank(value: object) -> bool:
    return pd.isna(value) or str(value).strip() == ""


def normalized(value: object) -> str:
    return "" if is_blank(value) else str(value).strip()


def bool_true(value: object) -> bool:
    return normalized(value).casefold() in {"true", "yes", "1"}


def largest_remainder(total: int, shares: dict[str, float]) -> dict[str, int]:
    raw = {key: total * value for key, value in shares.items()}
    result = {key: int(np.floor(value)) for key, value in raw.items()}
    remainder = total - sum(result.values())
    order = sorted(shares, key=lambda key: (-(raw[key] - result[key]), key))
    for key in order[:remainder]:
        result[key] += 1
    return result


def allocate_matrix(row_totals: dict[str, int], col_totals: dict[str, int]) -> dict[tuple[str, str], int]:
    total = sum(row_totals.values())
    if total != sum(col_totals.values()):
        raise ValueError("Row and column allocation totals differ")
    raw = {(row, col): row_total * col_totals[col] / total for row, row_total in row_totals.items() for col in col_totals}
    result = {key: int(np.floor(value)) for key, value in raw.items()}
    row_remaining = {row: row_totals[row] - sum(result[(row, col)] for col in col_totals) for row in row_totals}
    col_remaining = {col: col_totals[col] - sum(result[(row, col)] for row in row_totals) for col in col_totals}
    while sum(row_remaining.values()):
        choices = [
            (raw[(row, col)] - result[(row, col)], row, col)
            for row in row_totals for col in col_totals
            if row_remaining[row] > 0 and col_remaining[col] > 0
        ]
        _, row, col = max(choices, key=lambda item: (item[0], item[1], item[2]))
        result[(row, col)] += 1
        row_remaining[row] -= 1
        col_remaining[col] -= 1
    return result


def rating_band(series: pd.Series) -> pd.Series:
    rating = pd.to_numeric(series, errors="coerce")
    return pd.Series(np.select([rating.le(2), rating.eq(3), rating.ge(4)], ["LOW", "MID", "HIGH"], default="UNKNOWN"), index=series.index)


def time_period(series: pd.Series) -> pd.Series:
    dates = pd.to_datetime(series, utc=True, errors="coerce")
    return pd.cut(
        dates,
        bins=[
            pd.Timestamp("2024-09-22T00:00:00Z"),
            pd.Timestamp("2025-03-22T00:00:00Z"),
            pd.Timestamp("2025-09-22T00:00:00Z"),
            pd.Timestamp("2026-03-22T00:00:00Z"),
            pd.Timestamp("2026-09-23T00:00:00Z"),
        ],
        labels=["P1", "P2", "P3", "P4"],
        right=False,
    ).astype("string")


def length_band(frame: pd.DataFrame) -> pd.Series:
    lengths = pd.to_numeric(frame["review_char_length"], errors="coerce")
    very_short = frame["is_very_short"].map(bool_true)
    return pd.Series(np.select([very_short, lengths.ge(200)], ["VERY_SHORT", "LONG"], default="NORMAL"), index=frame.index)


def detect_review_sheet(path: Path) -> tuple[str, list[str]]:
    workbook = pd.ExcelFile(path)
    for sheet in workbook.sheet_names:
        columns = pd.read_excel(path, sheet_name=sheet, nrows=0).columns.tolist()
        if {"source", "review_id", "label_status"}.issubset(columns):
            return sheet, workbook.sheet_names
    raise RuntimeError("No review-data sheet with source, review_id and label_status was found")


def main() -> None:
    protected = [ANALYSIS_PATH, WORKBOOK_PATH, CLEAN_PATH, MERGED_STANDARDIZED_PATH, RAW_GP_PATH, RAW_AS_PATH]
    hashes_before = {str(path.relative_to(ROOT)): sha256(path) for path in protected}

    analysis = pd.read_csv(ANALYSIS_PATH, dtype=str, keep_default_na=False)
    if len(analysis) != 736 or analysis["source"].value_counts().to_dict() != {"Google Play": 403, "App Store": 333}:
        raise RuntimeError(f"Unexpected analysis dataset: rows={len(analysis)}, sources={analysis['source'].value_counts().to_dict()}")
    if analysis.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Duplicate (source, review_id) in analysis dataset")
    analysis_dates = pd.to_datetime(analysis["review_date"], utc=True, errors="coerce")
    if analysis_dates.isna().any() or not analysis_dates.between(START, END, inclusive="both").all():
        raise RuntimeError("Analysis dataset contains invalid or out-of-window dates")

    review_sheet, sheet_names = detect_review_sheet(WORKBOOK_PATH)
    manual = pd.read_excel(WORKBOOK_PATH, sheet_name=review_sheet, dtype={"review_id": str})
    codebook_sheet = next((sheet for sheet in sheet_names if sheet.casefold() == "codebook"), None)
    codebook = pd.read_excel(WORKBOOK_PATH, sheet_name=codebook_sheet) if codebook_sheet else pd.DataFrame()
    if manual.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Duplicate (source, review_id) in manual workbook")

    pain_primary = "pain_point_primary" if "pain_point_primary" in manual.columns else "pain_point"
    journey_primary = "journey_primary" if "journey_primary" in manual.columns else "journey"
    manual_columns = [column for column in [
        "label_status", "manual_validity", "invalid_reason", "sentiment", "complaint_present",
        "issue_summary", pain_primary, "pain_point_secondary_1", "pain_point_secondary_2",
        journey_primary, "journey_secondary", "severity", "product_related", "feature_request",
        "evidence_span", "confidence", "reviewer_note", "reviewer", "reviewed_at",
        "needs_second_review", "incidents_json", "label_origin", "completion_status", "incomplete_reason",
    ] if column in manual.columns]
    required_labels = [column for column in [
        "manual_validity", "sentiment", "complaint_present", pain_primary, journey_primary,
        "severity", "product_related", "feature_request", "evidence_span", "confidence",
    ] if column in manual.columns]

    status = manual["label_status"].map(normalized).str.upper()
    second_flag = manual.get("needs_second_review", pd.Series("", index=manual.index)).map(bool_true)
    any_manual_value = manual[required_labels].apply(lambda row: any(not is_blank(value) for value in row), axis=1)
    inspected_mask = status.ne("UNREVIEWED") | any_manual_value
    second_mask = inspected_mask & (status.eq("NEEDS_SECOND_REVIEW") | second_flag)
    missing_required = manual[required_labels].apply(lambda row: any(is_blank(value) for value in row), axis=1)
    validity_final = manual["manual_validity"].map(normalized).str.upper().isin(["VALID", "INVALID"])
    complete_mask = inspected_mask & ~second_mask & status.eq("REVIEWED") & validity_final & ~missing_required
    inspected = manual.loc[inspected_mask].copy()
    inspected["manual_review_state"] = np.where(second_mask.loc[inspected.index], "NEEDS_SECOND_REVIEW", np.where(complete_mask.loc[inspected.index], "COMPLETE", "INSPECTED_INCOMPLETE"))

    analysis_keys = set(zip(analysis["source"], analysis["review_id"].astype(str)))
    clean = pd.read_csv(CLEAN_PATH, dtype=str, keep_default_na=False, usecols=["source", "review_id"])
    clean_keys = set(zip(clean["source"], clean["review_id"].astype(str)))
    inspected_keys = list(zip(inspected["source"], inspected["review_id"].astype(str)))
    inspected["in_24m"] = [key in analysis_keys for key in inspected_keys]
    inspected["in_full_clean"] = [key in clean_keys for key in inspected_keys]
    inside = inspected[inspected["in_24m"]].copy()
    outside = inspected[~inspected["in_24m"] & inspected["in_full_clean"]]
    unmatched = inspected[~inspected["in_full_clean"]]
    inside["manual_reuse_status"] = np.where(
        inside["manual_review_state"].eq("COMPLETE"),
        "REUSED_COMPLETE",
        "REUSED_NEEDS_SECOND_REVIEW",
    )

    analysis_indexed = analysis.set_index(["source", "review_id"], drop=False)
    reused_rows: list[dict[str, object]] = []
    for _, old in inside.iterrows():
        key = (old["source"], str(old["review_id"]))
        row = analysis_indexed.loc[key].to_dict()
        for column in manual_columns:
            row[column] = old[column]
        row["manual_reuse_status"] = old["manual_reuse_status"]
        reused_rows.append(row)
    reused = pd.DataFrame(reused_rows)

    new_needed = max(0, TARGET_SIZE - len(reused))
    inspected_key_set = set(inspected_keys)
    candidates = analysis[
        ~pd.Series(list(zip(analysis["source"], analysis["review_id"].astype(str))), index=analysis.index).isin(inspected_key_set)
    ].copy()
    candidates["_rating_band"] = rating_band(candidates["rating"])
    candidates["_time_period"] = time_period(candidates["review_date"])
    candidates["_length_band"] = length_band(candidates)
    rng = np.random.default_rng(RANDOM_SEED)
    candidates["_tie_breaker"] = rng.random(len(candidates))

    reused_for_targets = reused.copy()
    if len(reused_for_targets):
        reused_for_targets["_rating_band"] = rating_band(reused_for_targets["rating"])
        reused_for_targets["_time_period"] = time_period(reused_for_targets["review_date"])
        reused_for_targets["_length_band"] = length_band(reused_for_targets)

    source_shares = (analysis["source"].value_counts() / len(analysis)).to_dict()
    desired_source = largest_remainder(max(TARGET_SIZE, len(reused)), source_shares)
    desired_rating = largest_remainder(max(TARGET_SIZE, len(reused)), RATING_TARGET_SHARES)
    desired_time = largest_remainder(max(TARGET_SIZE, len(reused)), TIME_TARGET_SHARES)
    desired_length = largest_remainder(max(TARGET_SIZE, len(reused)), LENGTH_TARGET_SHARES)

    def needed_after_reuse(targets: dict[str, int], column: str) -> dict[str, int]:
        existing = reused_for_targets[column].value_counts().to_dict() if len(reused_for_targets) else {}
        return {key: max(0, value - int(existing.get(key, 0))) for key, value in targets.items()}

    source_needed = needed_after_reuse(desired_source, "source")
    rating_needed = needed_after_reuse(desired_rating, "_rating_band")
    time_needed = needed_after_reuse(desired_time, "_time_period")
    length_needed = needed_after_reuse(desired_length, "_length_band")
    if sum(source_needed.values()) != new_needed or sum(rating_needed.values()) != new_needed:
        raise RuntimeError("Existing reviewed distribution exceeds a source/rating target; allocation requires review")

    joint_allocation = allocate_matrix(source_needed, rating_needed) if new_needed else {}
    slots = [key for key, count in joint_allocation.items() for _ in range(count)]
    rng.shuffle(slots)
    selected_indices: list[int] = []
    selected_time = {key: 0 for key in time_needed}
    selected_length = {key: 0 for key in length_needed}
    for source_name, band in slots:
        pool = candidates[
            candidates["source"].eq(source_name)
            & candidates["_rating_band"].eq(band)
            & ~candidates.index.isin(selected_indices)
        ].copy()
        if pool.empty:
            raise RuntimeError(f"Insufficient candidates for source={source_name}, rating_band={band}")
        pool["_score"] = (
            pool["_time_period"].map(lambda value: max(time_needed.get(value, 0) - selected_time.get(value, 0), 0) / max(time_needed.get(value, 1), 1)) * 4
            + pool["_length_band"].map(lambda value: max(length_needed.get(value, 0) - selected_length.get(value, 0), 0) / max(length_needed.get(value, 1), 1)) * 3
            + pool["_tie_breaker"] * 1e-6
        )
        chosen_index = int(pool["_score"].idxmax())
        selected_indices.append(chosen_index)
        chosen = candidates.loc[chosen_index]
        selected_time[chosen["_time_period"]] = selected_time.get(chosen["_time_period"], 0) + 1
        selected_length[chosen["_length_band"]] = selected_length.get(chosen["_length_band"], 0) + 1

    sampled = candidates.loc[selected_indices, analysis.columns].copy()
    for column in manual_columns:
        sampled[column] = ""
    sampled["label_status"] = "UNREVIEWED"
    sampled["manual_reuse_status"] = "NEW_SAMPLE_UNREVIEWED"

    final_sample = pd.concat([reused, sampled], ignore_index=True, sort=False)
    final_sample["rating_band"] = rating_band(final_sample["rating"])
    final_sample["time_period_24m"] = time_period(final_sample["review_date"])
    final_sample["text_length_band"] = length_band(final_sample)
    final_sample["sampling_seed"] = RANDOM_SEED

    # Stable, human-friendly ordering: reused work first, then new rows by time/source/key.
    reuse_order = {"REUSED_COMPLETE": 0, "REUSED_NEEDS_SECOND_REVIEW": 1, "NEW_SAMPLE_UNREVIEWED": 2}
    final_sample["_reuse_order"] = final_sample["manual_reuse_status"].map(reuse_order)
    final_sample = final_sample.sort_values(["_reuse_order", "review_date", "source", "review_id"]).drop(columns="_reuse_order").reset_index(drop=True)

    # Overlap audit contains every actually inspected row from the supplied workbook.
    overlap = inspected.copy()
    overlap["old_label_status"] = overlap["label_status"]
    overlap["manual_reuse_status"] = ""
    overlap.loc[overlap["in_24m"] & overlap["manual_review_state"].eq("COMPLETE"), "manual_reuse_status"] = "REUSED_COMPLETE"
    overlap.loc[overlap["in_24m"] & ~overlap["manual_review_state"].eq("COMPLETE"), "manual_reuse_status"] = "REUSED_NEEDS_SECOND_REVIEW"
    preferred_overlap = [
        "source", "review_id", "review_date", "rating", "review_text_raw", "old_label_status",
        "needs_second_review", "in_24m", "manual_reuse_status", "manual_review_state",
    ]
    overlap_columns = preferred_overlap + [column for column in manual_columns if column not in preferred_overlap and column != "label_status"]
    overlap = overlap[overlap_columns]

    # Taxonomy coverage uses COMPLETE records inside the 24-month window only.
    complete_inside = inside[inside["manual_review_state"].eq("COMPLETE")].copy()
    pain_values = sorted({normalized(value) for value in complete_inside.get(pain_primary, pd.Series(dtype=object)) if normalized(value)})
    journey_values = sorted({normalized(value) for value in complete_inside.get(journey_primary, pd.Series(dtype=object)) if normalized(value)})
    codebook_pain = []
    codebook_journey = []
    if not codebook.empty:
        pain_col = next((column for column in codebook.columns if "pain point" in str(column).casefold()), None)
        journey_col = next((column for column in codebook.columns if "journey" in str(column).casefold()), None)
        if pain_col:
            codebook_pain = [normalized(value) for value in codebook[pain_col] if normalized(value)]
        if journey_col:
            codebook_journey = [normalized(value) for value in codebook[journey_col] if normalized(value)]
    zero_pain = [value for value in codebook_pain if value not in pain_values]
    zero_journey = [value for value in codebook_journey if value not in journey_values]

    secondary_columns = [column for column in ["pain_point_secondary_1", "pain_point_secondary_2"] if column in complete_inside.columns]
    secondary_count = int(complete_inside[secondary_columns].apply(
        lambda row: any(normalized(value) not in {"", "NONE"} for value in row), axis=1
    ).sum()) if secondary_columns and len(complete_inside) else 0
    unclear_fields = [column for column in [pain_primary, journey_primary, *secondary_columns] if column in complete_inside.columns]
    unclear_count = int(complete_inside[unclear_fields].apply(
        lambda row: any(normalized(value) == "UNCLEAR" for value in row), axis=1
    ).sum()) if unclear_fields and len(complete_inside) else 0
    none_count = int(complete_inside[pain_primary].map(normalized).eq("NONE").sum()) if pain_primary in complete_inside else 0
    feature_request_count = int(complete_inside["feature_request"].map(normalized).str.upper().eq("YES").sum()) if "feature_request" in complete_inside else 0

    # Validation: keys, membership, labels, second-review retention, and diversity.
    final_keys = list(zip(final_sample["source"], final_sample["review_id"].astype(str)))
    if final_sample.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Duplicate key in final manual sample")
    if not set(final_keys).issubset(analysis_keys):
        raise RuntimeError("Final sample contains a key outside the analysis dataset")
    final_dates = pd.to_datetime(final_sample["review_date"], utc=True, errors="coerce")
    if final_dates.isna().any() or not final_dates.between(START, END, inclusive="both").all():
        raise RuntimeError("Final sample contains an invalid or out-of-window date")
    new_rows = final_sample["manual_reuse_status"].eq("NEW_SAMPLE_UNREVIEWED")
    blank_fields = [column for column in manual_columns if column != "label_status"]
    new_labels_blank = final_sample.loc[new_rows, blank_fields].apply(lambda col: col.map(is_blank)).all().all()
    new_status_ok = final_sample.loc[new_rows, "label_status"].eq("UNREVIEWED").all()
    if not (new_labels_blank and new_status_ok):
        raise RuntimeError("A new sample row contains a nonblank manual label")

    old_labels_preserved = True
    for _, old in inside.iterrows():
        result = final_sample[
            final_sample["source"].eq(old["source"]) & final_sample["review_id"].astype(str).eq(str(old["review_id"]))
        ].iloc[0]
        for column in manual_columns:
            if normalized(result[column]) != normalized(old[column]):
                old_labels_preserved = False
                break
    if not old_labels_preserved:
        raise RuntimeError("A reused manual label changed")
    reused_second_keys = set(zip(inside.loc[inside["manual_review_state"].eq("NEEDS_SECOND_REVIEW"), "source"], inside.loc[inside["manual_review_state"].eq("NEEDS_SECOND_REVIEW"), "review_id"].astype(str)))
    second_preserved = reused_second_keys.issubset(set(final_keys))
    if not second_preserved:
        raise RuntimeError("A reusable second-review case is absent from the final sample")
    if final_sample["source"].nunique() < 2 or final_sample["rating_band"].nunique() < 3 or final_sample["time_period_24m"].nunique() < 4 or final_sample["text_length_band"].nunique() < 3:
        raise RuntimeError("Final sample does not meet minimum diversity coverage")

    # Summary is deliberately descriptive, not a population estimate.
    summary_rows: list[dict[str, object]] = []
    dimensions = {
        "source": final_sample["source"],
        "rating_band": final_sample["rating_band"],
        "reused_vs_new": final_sample["manual_reuse_status"].map(lambda value: "NEW" if value == "NEW_SAMPLE_UNREVIEWED" else "REUSED"),
        "manual_reuse_status": final_sample["manual_reuse_status"],
        "review_status": final_sample["label_status"],
        "very_short_status": final_sample["is_very_short"].map(lambda value: "VERY_SHORT" if bool_true(value) else "NOT_VERY_SHORT"),
        "time_period_24m": final_sample["time_period_24m"],
        "text_length_band": final_sample["text_length_band"],
    }
    for dimension, values in dimensions.items():
        for category, count in values.value_counts(dropna=False).items():
            summary_rows.append({
                "dimension": dimension,
                "category": category,
                "count": int(count),
                "percentage": round(100 * int(count) / len(final_sample), 2),
            })
    summary = pd.DataFrame(summary_rows)

    SAMPLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    OVERLAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    final_sample.to_csv(SAMPLE_PATH, index=False)
    overlap.to_csv(OVERLAP_PATH, index=False)
    summary.to_csv(SUMMARY_PATH, index=False)

    pain_counts = complete_inside[pain_primary].map(normalized).value_counts().rename_axis("category").reset_index(name="count") if len(complete_inside) else pd.DataFrame(columns=["category", "count"])
    journey_counts = complete_inside[journey_primary].map(normalized).value_counts().rename_axis("category").reset_index(name="count") if len(complete_inside) else pd.DataFrame(columns=["category", "count"])
    severity_counts = complete_inside["severity"].map(normalized).value_counts().rename_axis("severity").reset_index(name="count") if len(complete_inside) else pd.DataFrame(columns=["severity", "count"])
    sentiment_counts = complete_inside["sentiment"].map(normalized).value_counts().rename_axis("sentiment").reset_index(name="count") if len(complete_inside) else pd.DataFrame(columns=["sentiment", "count"])
    complaint_counts = complete_inside["complaint_present"].map(normalized).value_counts().rename_axis("complaint_present").reset_index(name="count") if len(complete_inside) else pd.DataFrame(columns=["complaint_present", "count"])

    def bullet(values: list[str]) -> str:
        return ", ".join(values) if values else "None in the supplied workbook."

    def compact_counts(frame: pd.DataFrame) -> str:
        return ", ".join(f"{row[0]}={row[1]}" for row in frame.itertuples(index=False, name=None)) if len(frame) else "None"

    report = f"""# Manual Review Reuse — 24-Month Analysis Window

## Purpose

Prepare a taxonomy-development/validation sample from the finalized 24-month dataset. This artifact is not a population estimate and is not used to identify top pain points, complaints, journeys, business problems, or customer behavior.

## Inputs

- Analysis dataset: `01_data/processed/reviews_analysis_24m.csv` ({len(analysis):,} rows)
- Manual workbook: `05_outputs/tables/TCInvest_manual_review_incomplete.xlsx`
- Review-data sheet: `{review_sheet}`
- Workbook sheets: {', '.join(sheet_names)}
- Matching key: `(source, review_id)` only

## Manual Work Found in the Supplied Workbook

- Inspected rows: **{len(inspected):,}**
- Complete rows: **{int(complete_mask.sum()):,}**
- Needs-second-review rows: **{int(second_mask.sum()):,}**
- Inspected inside 24 months: **{len(inside):,}**
- Inspected outside 24 months: **{len(outside):,}**
- Unmatched against the full clean dataset: **{len(unmatched):,}**

Important: the supplied workbook is an **incomplete-row export**. Its review sheet contains no COMPLETE rows; the previously reported 63 COMPLETE labels are absent from this input and therefore cannot be reused or counted for taxonomy coverage in this task. No labels were reconstructed from other files.

## Reuse Logic

Records were matched only by `(source, review_id)`. Every available manual-label value for reusable rows was copied unchanged. NEEDS_SECOND_REVIEW records remain unresolved and are marked `REUSED_NEEDS_SECOND_REVIEW`. New records are marked `NEW_SAMPLE_UNREVIEWED`, have `label_status=UNREVIEWED`, and all other manual fields are blank.

## New Sampling Rule

- Seed: **{RANDOM_SEED}**
- Target size: **{TARGET_SIZE}**
- Existing in-scope inspected rows retained: **{len(reused)}**
- New rows selected: **{len(sampled)}**
- Source target follows the analysis dataset approximately (Google Play 54.76%, App Store 45.24%).
- Intentional rating-band targets for taxonomy coverage: LOW 60%, MID 15%, HIGH 25%. This keeps complaints dominant without allowing the natural 1-star skew to crowd out mixed/high-rating evidence.
- Time target: approximately equal representation across four consecutive six-month periods.
- Text-length target: VERY_SHORT 10%, NORMAL 65%, LONG 25%; LONG is defined as at least 200 cleaned characters.
- A deterministic greedy selection within source/rating allocations prioritizes remaining time and length deficits, with seed-based tie-breaking.

## Final Sample Validation

- Rows: **{len(final_sample):,}**
- Duplicate `(source, review_id)` keys: **{int(final_sample.duplicated(['source', 'review_id'], keep=False).sum())}**
- All rows belong to the 736-row analysis dataset: **Yes**
- All rows fall inside the agreed UTC window: **Yes**
- Old manual labels preserved exactly: **{'Yes' if old_labels_preserved else 'No'}**
- New manual fields blank: **{'Yes' if new_labels_blank and new_status_ok else 'No'}**
- Second-review cases retained: **{'Yes' if second_preserved else 'No'}**
- Sources: {compact_counts(final_sample['source'].value_counts().rename_axis('source').reset_index(name='count'))}
- Rating bands: {compact_counts(final_sample['rating_band'].value_counts().rename_axis('band').reset_index(name='count'))}
- Time periods: {compact_counts(final_sample['time_period_24m'].value_counts().sort_index().rename_axis('period').reset_index(name='count'))}
- Text-length bands: {compact_counts(final_sample['text_length_band'].value_counts().rename_axis('band').reset_index(name='count'))}

## Taxonomy Coverage from COMPLETE In-Scope Labels

Only COMPLETE labels in the supplied workbook are eligible for this section.

- Pain-point counts: {compact_counts(pain_counts)}
- Journey counts: {compact_counts(journey_counts)}
- Severity distribution: {compact_counts(severity_counts)}
- Sentiment distribution: {compact_counts(sentiment_counts)}
- Complaint-present distribution: {compact_counts(complaint_counts)}
- Reviews with secondary pain points: **{secondary_count}**
- Reviews containing UNCLEAR in primary/secondary pain-point or journey fields: **{unclear_count}**
- Reviews with primary pain point NONE: **{none_count}**
- Feature-request reviews: **{feature_request_count}**

Categories with manual evidence:

- Pain point: {bullet(pain_values)}
- Journey: {bullet(journey_values)}

Codebook categories with zero COMPLETE manual evidence in this workbook:

- Pain point: {bullet(zero_pain)}
- Journey: {bullet(zero_journey)}

Absence of evidence here is not evidence that a category should be removed. The Codebook was not modified.

## Limitations

- The designated workbook omits completed manual-review rows, limiting label reuse and taxonomy-coverage auditing.
- New sampling is intentionally diversity-oriented and must not be used to estimate population prevalence.
- No new labels were inferred, no second-review ambiguity was resolved, and no taxonomy or Codebook value was changed.
"""
    REPORT_PATH.write_text(report, encoding="utf-8")

    # Re-read CSV outputs and repeat essential invariants.
    sample_check = pd.read_csv(SAMPLE_PATH, dtype=str, keep_default_na=False)
    if len(sample_check) != len(final_sample) or sample_check.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Written sample failed row/key validation")
    hashes_after = {str(path.relative_to(ROOT)): sha256(path) for path in protected}
    if hashes_before != hashes_after:
        raise RuntimeError("A protected source file changed")

    print("MANUAL REVIEW 24M REUSE RESULT")
    print(f"Workbook: {WORKBOOK_PATH.relative_to(ROOT)}")
    print(f"Sheets: {sheet_names}")
    print(f"Existing inspected/complete/second: {len(inspected)}/{int(complete_mask.sum())}/{int(second_mask.sum())}")
    print(f"Inside/complete inside/second inside/outside/unmatched: {len(inside)}/{int(inside['manual_review_state'].eq('COMPLETE').sum())}/{int(inside['manual_review_state'].eq('NEEDS_SECOND_REVIEW').sum())}/{len(outside)}/{len(unmatched)}")
    print(f"New sampled/final: {len(sampled)}/{len(final_sample)}")
    print(f"Sources: {final_sample['source'].value_counts().to_dict()}")
    print(f"Rating bands: {final_sample['rating_band'].value_counts().to_dict()}")
    print(f"Very short: {int(final_sample['is_very_short'].map(bool_true).sum())}")
    print(f"Time periods: {final_sample['time_period_24m'].value_counts().sort_index().to_dict()}")
    print(f"Length bands: {final_sample['text_length_band'].value_counts().to_dict()}")
    print(f"Taxonomy represented pain/journey: {pain_values}/{journey_values}")
    print(f"Zero-evidence pain/journey: {zero_pain}/{zero_journey}")
    print(f"Secondary/UNCLEAR/NONE/feature request: {secondary_count}/{unclear_count}/{none_count}/{feature_request_count}")
    print(f"New labels blank: {'YES' if new_labels_blank and new_status_ok else 'NO'}")
    print(f"Old labels preserved: {'YES' if old_labels_preserved else 'NO'}")
    print(f"Second-review retained: {'YES' if second_preserved else 'NO'}")
    print("Source files unchanged: YES")


if __name__ == "__main__":
    main()
