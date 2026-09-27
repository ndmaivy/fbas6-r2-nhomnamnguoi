#!/usr/bin/env python3
"""Audit manual-label progress and export rows that are not yet final.

The source workbook and JSON label file are read-only. JSON labels are overlaid
only in the newly generated workbook so that partially completed work remains
visible without modifying either source artifact.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parents[2]
WORKBOOK_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_batch01.xlsx"
JSON_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json"
OUTPUT_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_incomplete.xlsx"

CORE_LABEL_FIELDS = [
    "manual_validity",
    "sentiment",
    "complaint_present",
    "pain_point_primary",
    "journey_primary",
    "severity",
    "product_related",
    "feature_request",
    "evidence_span",
    "confidence",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def blank(value: object) -> bool:
    return pd.isna(value) or str(value).strip() == ""


def style_workbook(path: Path) -> None:
    from openpyxl import load_workbook

    workbook = load_workbook(path)
    header_fill = PatternFill("solid", fgColor="1F4E78")
    header_font = Font(color="FFFFFF", bold=True)
    for sheet in workbook.worksheets:
        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions
        for cell in sheet[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        for column_cells in sheet.columns:
            letter = get_column_letter(column_cells[0].column)
            header = str(column_cells[0].value or "")
            if header in {"review_text_raw", "review_text_clean", "issue_summary", "evidence_span", "reviewer_note", "incomplete_reason"}:
                width = 45
            elif header in {"review_id", "raw_source_file", "exact_duplicate_group_id"}:
                width = 38
            else:
                sampled = [len(str(cell.value)) for cell in column_cells[:200] if cell.value is not None]
                width = min(max([len(header), *sampled], default=10) + 2, 24)
            sheet.column_dimensions[letter].width = width
    workbook.save(path)


def main() -> None:
    source_hashes_before = {WORKBOOK_PATH.name: sha256(WORKBOOK_PATH), JSON_PATH.name: sha256(JSON_PATH)}

    reviews = pd.read_excel(WORKBOOK_PATH, sheet_name="Reviews", dtype={"review_id": str})
    progress = pd.read_excel(WORKBOOK_PATH, sheet_name="Review Progress")
    codebook = pd.read_excel(WORKBOOK_PATH, sheet_name="Codebook")
    labels = pd.DataFrame(json.loads(JSON_PATH.read_text(encoding="utf-8")))

    if len(reviews) != 3745 or reviews["review_id"].nunique() != 3745:
        raise RuntimeError("Unexpected workbook review count or duplicate review_id")
    if labels["review_id"].duplicated().any():
        raise RuntimeError("Duplicate review_id found in JSON labels")
    if not set(labels["review_id"].astype(str)).issubset(set(reviews["review_id"].astype(str))):
        missing = sorted(set(labels["review_id"].astype(str)) - set(reviews["review_id"].astype(str)))
        raise RuntimeError(f"JSON review IDs absent from workbook: {missing}")

    work = reviews.copy()
    work["review_id"] = work["review_id"].astype(str)
    work["label_origin"] = "none"
    work.loc[~work["label_status"].eq("UNREVIEWED"), "label_origin"] = "batch01_workbook"
    work["needs_second_review"] = ""
    work["incidents_json"] = ""

    # Overlay JSON labels in-memory/new output only. Secondary fields, notes and
    # invalid_reason are intentionally allowed to be blank when not applicable.
    label_by_id = labels.set_index(labels["review_id"].astype(str), drop=False)
    common_label_fields = [
        field for field in labels.columns
        if field in work.columns and field not in {"review_id", "incidents", "needs_second_review"}
    ]
    # Empty Excel label columns may be inferred as float; object dtype is needed
    # for the string labels copied into this output-only working dataframe.
    work[common_label_fields] = work[common_label_fields].astype(object)
    for review_id, label in label_by_id.iterrows():
        row_mask = work["review_id"].eq(review_id)
        for field in common_label_fields:
            work.loc[row_mask, field] = label[field]
        needs_review = str(label["needs_second_review"]).strip().upper()
        work.loc[row_mask, "needs_second_review"] = needs_review
        work.loc[row_mask, "incidents_json"] = json.dumps(label["incidents"], ensure_ascii=False)
        work.loc[row_mask, "label_status"] = "NEEDS_SECOND_REVIEW" if needs_review == "YES" else "REVIEWED"
        work.loc[row_mask, "label_origin"] = "batch02_labels_b_json"

    missing_core = work[CORE_LABEL_FIELDS].apply(lambda row: any(blank(value) for value in row), axis=1)
    final_status = work["label_status"].eq("REVIEWED")
    final_manual_validity = work["manual_validity"].isin(["VALID", "INVALID"])
    complete = final_status & final_manual_validity & ~missing_core

    reasons: list[str] = []
    completion_status: list[str] = []
    for idx, row in work.iterrows():
        row_reasons = []
        if row["label_status"] == "UNREVIEWED":
            row_reasons.append("UNREVIEWED_NO_LABELS")
        if row["label_status"] == "NEEDS_SECOND_REVIEW" or row["needs_second_review"] == "YES":
            row_reasons.append("NEEDS_SECOND_REVIEW")
        missing_fields = [field for field in CORE_LABEL_FIELDS if blank(row[field])]
        if row["label_status"] != "UNREVIEWED" and missing_fields:
            row_reasons.append("MISSING_CORE_LABELS:" + ",".join(missing_fields))
        if row["label_status"] != "UNREVIEWED" and row["manual_validity"] not in {"VALID", "INVALID"}:
            row_reasons.append("MANUAL_VALIDITY_NOT_FINAL")
        reasons.append("; ".join(row_reasons))
        completion_status.append("COMPLETE" if complete.at[idx] else "INCOMPLETE")

    work["completion_status"] = completion_status
    work["incomplete_reason"] = reasons
    incomplete = work.loc[~complete].copy()

    workbook_reviewed = int(reviews["label_status"].eq("REVIEWED").sum())
    workbook_second = int(reviews["label_status"].eq("NEEDS_SECOND_REVIEW").sum())
    workbook_unreviewed = int(reviews["label_status"].eq("UNREVIEWED").sum())
    json_second = int(labels["needs_second_review"].astype(str).str.upper().eq("YES").sum())
    json_final = len(labels) - json_second
    summary = pd.DataFrame([
        ["Total reviews", len(reviews)],
        ["Batch01 inspected", workbook_reviewed + workbook_second],
        ["Batch01 final complete", workbook_reviewed],
        ["Batch01 needs second review", workbook_second],
        ["Batch01 unreviewed", workbook_unreviewed],
        ["Batch02 JSON label records", len(labels)],
        ["Batch02 JSON IDs matched to workbook", labels["review_id"].nunique()],
        ["Batch02 final complete", json_final],
        ["Batch02 needs second review", json_second],
        ["Final complete across both sources", int(complete.sum())],
        ["Needs second review across both sources", int(work["label_status"].eq("NEEDS_SECOND_REVIEW").sum())],
        ["Unreviewed/no labels after JSON overlay", int(work["label_status"].eq("UNREVIEWED").sum())],
        ["Rows exported as incomplete", len(incomplete)],
    ], columns=["Metric", "Value"])

    rules = pd.DataFrame([
        ["Complete", "label_status=REVIEWED; manual_validity is VALID/INVALID; all core label fields are populated."],
        ["Incomplete", "UNREVIEWED, NEEDS_SECOND_REVIEW, non-final manual_validity, or missing a core label field."],
        ["Optional fields", "invalid_reason, issue_summary, secondary labels, reviewer_note and incidents may be blank when not applicable."],
        ["JSON overlay", "JSON values are copied only into this output workbook; both source files remain unchanged."],
        ["Core fields", ", ".join(CORE_LABEL_FIELDS)],
    ], columns=["Rule", "Definition"])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        incomplete.to_excel(writer, sheet_name="Incomplete Reviews", index=False)
        summary.to_excel(writer, sheet_name="Progress Summary", index=False)
        rules.to_excel(writer, sheet_name="Completion Rules", index=False)
        progress.to_excel(writer, sheet_name="Original Progress", index=False)
        codebook.to_excel(writer, sheet_name="Codebook", index=False)
    style_workbook(OUTPUT_PATH)

    source_hashes_after = {WORKBOOK_PATH.name: sha256(WORKBOOK_PATH), JSON_PATH.name: sha256(JSON_PATH)}
    if source_hashes_before != source_hashes_after:
        raise RuntimeError("A source label file changed during filtering")

    # Re-open the output to validate the generated workbook.
    check = pd.read_excel(OUTPUT_PATH, sheet_name="Incomplete Reviews", dtype={"review_id": str})
    if len(check) != len(incomplete) or check["review_id"].duplicated().any():
        raise RuntimeError("Generated incomplete workbook failed row-count/key validation")

    print("MANUAL LABEL PROGRESS")
    print(summary.to_string(index=False))
    print(f"Output: {OUTPUT_PATH.relative_to(ROOT)}")
    print("Source files unchanged: YES")


if __name__ == "__main__":
    main()
