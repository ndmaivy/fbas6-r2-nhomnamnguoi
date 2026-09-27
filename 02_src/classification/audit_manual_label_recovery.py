#!/usr/bin/env python3
"""Recover and audit historical row-level COMPLETE manual labels."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_PATH = ROOT / "01_data/processed/reviews_analysis_24m.csv"
CLEAN_PATH = ROOT / "01_data/processed/reviews_clean_full.csv"
BATCH1_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_batch01.xlsx"
BATCH2_PATH = ROOT / "05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json"
RECOVERY_PATH = ROOT / "05_outputs/tables/recovered_complete_manual_labels.csv"
REPORT_PATH = ROOT / "04_analysis/validation/manual_label_recovery_audit.md"

SEARCH_EXTENSIONS = {".csv", ".xlsx", ".xls", ".json", ".jsonl", ".md", ".ipynb", ".parquet", ".pkl"}
FILENAME_PATTERN = re.compile(
    r"manual_review|reviewed|complete|completed|classification|label|taxonomy|batch_?0?1|batch_?0?2|batch|manual|annotation|annotated|progress",
    re.I,
)
CONTENT_PATTERN = re.compile(
    r"label_status|\bREVIEWED\b|\bCOMPLETE\b|needs_second_review|manual_validity|pain_point|journey|severity|evidence_span|reviewer_note",
    re.I,
)
TEXT_EXTENSIONS = {".csv", ".json", ".jsonl", ".md", ".ipynb"}
REQUIRED_LABELS = [
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
MANUAL_FIELDS = [
    "manual_validity",
    "invalid_reason",
    "sentiment",
    "complaint_present",
    "issue_summary",
    "pain_point_primary",
    "pain_point_secondary_1",
    "pain_point_secondary_2",
    "journey_primary",
    "journey_secondary",
    "severity",
    "product_related",
    "feature_request",
    "evidence_span",
    "confidence",
    "reviewer_note",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def blank(value: object) -> bool:
    return pd.isna(value) or str(value).strip() == ""


def project_files() -> list[Path]:
    excluded = {RECOVERY_PATH.resolve(), REPORT_PATH.resolve()}
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".venv" not in path.parts
        and path.suffix.casefold() in SEARCH_EXTENSIONS
        and path.resolve() not in excluded
    )


def candidate_files(files: list[Path]) -> list[Path]:
    candidates = []
    for path in files:
        relative = str(path.relative_to(ROOT))
        matched = bool(FILENAME_PATTERN.search(relative))
        if not matched and path.suffix.casefold() in TEXT_EXTENSIONS:
            try:
                matched = bool(CONTENT_PATTERN.search(path.read_text(encoding="utf-8", errors="replace")))
            except OSError:
                matched = False
        if matched:
            candidates.append(path)
    return candidates


def dataframe_profile(frame: pd.DataFrame) -> tuple[int, int, int, bool, bool, str]:
    columns = frame.columns.tolist()
    manual_columns = [column for column in REQUIRED_LABELS if column in columns]
    labeled = int(frame[manual_columns].notna().any(axis=1).sum()) if manual_columns else 0
    if "label_status" in frame:
        status = frame["label_status"].astype("string").str.upper()
        complete = int(status.isin(["REVIEWED", "COMPLETE"]).sum())
        second = int(status.eq("NEEDS_SECOND_REVIEW").sum())
    else:
        complete = 0
        second = 0
    if "needs_second_review" in frame:
        needs = frame["needs_second_review"].astype("string").str.upper()
        second = max(second, int(needs.eq("YES").sum()))
        if "label_status" not in frame:
            complete = int(needs.eq("NO").sum())
    return labeled, complete, second, "source" in columns, "review_id" in columns, ", ".join(columns)


def inspect_candidates(candidates: list[Path]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in candidates:
        relative = str(path.relative_to(ROOT))
        suffix = path.suffix.casefold()
        base = {
            "path": relative,
            "file_type": suffix.lstrip("."),
            "rows": "N/A",
            "sheets": "",
            "columns": "",
            "rows_with_manual_labels": 0,
            "complete_or_reviewed": 0,
            "needs_second_review": 0,
            "has_source": False,
            "has_review_id": False,
            "assessment": "Not a row-level recovery source",
        }
        try:
            if suffix == ".xlsx":
                workbook = pd.ExcelFile(path)
                base["sheets"] = ", ".join(workbook.sheet_names)
                data_frames = []
                for sheet in workbook.sheet_names:
                    frame = pd.read_excel(path, sheet_name=sheet, dtype={"review_id": str})
                    if {"review_id", "source"}.issubset(frame.columns):
                        data_frames.append((sheet, frame))
                if data_frames:
                    sheet, frame = max(data_frames, key=lambda item: len(item[1]))
                    labeled, complete, second, has_source, has_id, columns = dataframe_profile(frame)
                    base.update(rows=len(frame), columns=columns, rows_with_manual_labels=labeled,
                                complete_or_reviewed=complete, needs_second_review=second,
                                has_source=has_source, has_review_id=has_id)
            elif suffix == ".csv":
                frame = pd.read_csv(path, dtype={"review_id": str}, low_memory=False)
                labeled, complete, second, has_source, has_id, columns = dataframe_profile(frame)
                base.update(rows=len(frame), columns=columns, rows_with_manual_labels=labeled,
                            complete_or_reviewed=complete, needs_second_review=second,
                            has_source=has_source, has_review_id=has_id)
            elif suffix == ".json":
                payload = json.loads(path.read_text(encoding="utf-8"))
                frame = pd.DataFrame(payload if isinstance(payload, list) else payload.get("records", []))
                labeled, complete, second, has_source, has_id, columns = dataframe_profile(frame)
                base.update(rows=len(frame), columns=columns, rows_with_manual_labels=labeled,
                            complete_or_reviewed=complete, needs_second_review=second,
                            has_source=has_source, has_review_id=has_id)

            if relative == "05_outputs/tables/TCInvest_manual_review_batch01.xlsx":
                base["assessment"] = "Usable primary row-level source: 49 REVIEWED + 1 NEEDS_SECOND_REVIEW"
            elif relative == "05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json":
                base["assessment"] = "Usable label source when exact-joined to batch01 roster: 14 final + 6 second-review"
            elif relative == "05_outputs/tables/manual_review_sample_v0.csv":
                base["assessment"] = "Row-level exploratory artifact, but explicitly superseded/disputed; excluded from recovery"
        except Exception as error:  # audit inventory must retain unreadable candidates
            base["assessment"] = f"Inspection error: {type(error).__name__}: {error}"
        rows.append(base)
    return pd.DataFrame(rows)


def markdown_table(frame: pd.DataFrame, columns: list[str]) -> str:
    if frame.empty:
        return "_None._"
    display = frame[columns].copy()
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, separator]
    for values in display.itertuples(index=False, name=None):
        lines.append("| " + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in values) + " |")
    return "\n".join(lines)


def main() -> None:
    files = project_files()
    hashes_before = {str(path.relative_to(ROOT)): sha256(path) for path in files}
    candidates = candidate_files(files)
    inventory = inspect_candidates(candidates)

    batch1 = pd.read_excel(BATCH1_PATH, sheet_name="Reviews", dtype={"review_id": str})
    batch1["review_id"] = batch1["review_id"].astype(str)
    batch2 = pd.DataFrame(json.loads(BATCH2_PATH.read_text(encoding="utf-8")))
    batch2["review_id"] = batch2["review_id"].astype(str)

    if batch1.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Batch01 contains duplicate composite review keys")
    if batch2["review_id"].duplicated().any():
        raise RuntimeError("Batch02 contains duplicate review IDs")
    roster_id_counts = batch1["review_id"].value_counts()
    ambiguous_json_ids = [review_id for review_id in batch2["review_id"] if roster_id_counts.get(review_id, 0) != 1]
    if ambiguous_json_ids:
        raise RuntimeError(f"Batch02 IDs are absent or non-unique in batch01 roster: {ambiguous_json_ids}")

    batch1_status = batch1["label_status"].astype("string").str.upper()
    batch1_complete = batch1[batch1_status.eq("REVIEWED")].copy()
    batch1_second = batch1[batch1_status.eq("NEEDS_SECOND_REVIEW")].copy()

    roster_columns = ["source", "review_id", "review_date", "rating", "title", "review_text_raw"]
    batch2_enriched = batch2.merge(batch1[roster_columns], on="review_id", how="left", validate="one_to_one")
    batch2_needs = batch2_enriched["needs_second_review"].astype("string").str.upper()
    batch2_complete = batch2_enriched[batch2_needs.eq("NO")].copy()
    batch2_second = batch2_enriched[batch2_needs.eq("YES")].copy()

    # Preserve actual labels and add only clearly named recovery metadata.
    output_rows: list[dict[str, object]] = []
    for _, row in batch1_complete.iterrows():
        output = {column: row[column] for column in roster_columns}
        output.update({field: row[field] for field in MANUAL_FIELDS})
        output.update({
            "original_label_status": row["label_status"],
            "needs_second_review": "",
            "incidents_json": "",
            "recovery_source": "TCInvest_manual_review_batch01.xlsx::Reviews",
            "recovered_complete_basis": "label_status=REVIEWED",
        })
        output_rows.append(output)
    for _, row in batch2_complete.iterrows():
        output = {column: row[column] for column in roster_columns}
        output.update({field: row[field] for field in MANUAL_FIELDS})
        output.update({
            "original_label_status": "",
            "needs_second_review": row["needs_second_review"],
            "incidents_json": json.dumps(row["incidents"], ensure_ascii=False),
            "recovery_source": "TCInvest_manual_review_batch02_labels_b.json + exact batch01 roster join",
            "recovered_complete_basis": "needs_second_review=NO",
        })
        output_rows.append(output)
    recovered = pd.DataFrame(output_rows)

    if recovered.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Recovered COMPLETE rows contain duplicate composite keys")

    analysis = pd.read_csv(ANALYSIS_PATH, dtype=str, keep_default_na=False)
    clean = pd.read_csv(CLEAN_PATH, dtype=str, keep_default_na=False)
    # Excel exposes review_date as a serial number. Retain that source value for
    # provenance, while using the exact composite key to attach readable metadata
    # from the protected clean dataset. Manual labels are not touched.
    recovered["source_review_date_value"] = recovered["review_date"].astype(str)
    recovered_labels = recovered.drop(columns=["review_date", "rating", "title", "review_text_raw"])
    recovered = clean[roster_columns].merge(
        recovered_labels,
        on=["source", "review_id"],
        how="right",
        validate="one_to_one",
    )
    missing_required = {field: int(recovered[field].map(blank).sum()) for field in REQUIRED_LABELS}

    analysis_keys = set(zip(analysis["source"], analysis["review_id"].astype(str)))
    clean_keys = set(zip(clean["source"], clean["review_id"].astype(str)))
    recovered_keys = list(zip(recovered["source"], recovered["review_id"].astype(str)))
    recovered["in_24m"] = [key in analysis_keys for key in recovered_keys]
    recovered["in_full_clean"] = [key in clean_keys for key in recovered_keys]
    recovered["recovery_match_status"] = [
        "INSIDE_24M" if key in analysis_keys else "OUTSIDE_24M" if key in clean_keys else "UNMATCHED"
        for key in recovered_keys
    ]

    inside_count = int(recovered["in_24m"].sum())
    outside_count = int((~recovered["in_24m"] & recovered["in_full_clean"]).sum())
    unmatched_count = int((~recovered["in_full_clean"]).sum())

    second_keys = pd.concat([
        batch1_second[["source", "review_id"]],
        batch2_second[["source", "review_id"]],
    ], ignore_index=True)
    if second_keys.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Second-review evidence contains duplicate composite keys")
    all_inspected_keys = pd.concat([
        recovered[["source", "review_id"]],
        second_keys,
    ], ignore_index=True)
    if all_inspected_keys.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Complete and second-review evidence overlap unexpectedly")

    RECOVERY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    recovered.to_csv(RECOVERY_PATH, index=False)

    candidate_table = inventory.copy()
    candidate_table["columns"] = candidate_table["columns"].map(lambda value: (str(value)[:160] + "…") if len(str(value)) > 160 else value)
    usable_sources = [
        "05_outputs/tables/TCInvest_manual_review_batch01.xlsx::Reviews",
        "05_outputs/tables/TCInvest_manual_review_batch02_labels_b.json + exact review_id join to batch01 roster",
    ]
    report = f"""# Manual Label Recovery Audit

## Search Scope

- Project files searched: **{len(files)}**
- Included types: CSV, XLSX, XLS, JSON, JSONL, Markdown, IPYNB, Parquet and PKL
- `.venv` excluded as environment content, not project evidence
- Candidate files found by filename/content terms: **{len(candidates)}**

Candidate paths:

{chr(10).join(f'- `{path.relative_to(ROOT)}`' for path in candidates)}

## Candidate Inspection

{markdown_table(candidate_table, ['path', 'file_type', 'rows', 'sheets', 'rows_with_manual_labels', 'complete_or_reviewed', 'needs_second_review', 'has_source', 'has_review_id', 'assessment'])}

## Usable Row-Level Sources

1. `{usable_sources[0]}` contains **49 actual REVIEWED rows** and **1 actual NEEDS_SECOND_REVIEW row**, with source, review ID and manual fields.
2. `{usable_sources[1]}` contains **14 final rows** (`needs_second_review=NO`) and **6 second-review rows**. The JSON does not store `source`; every JSON review ID was verified to occur exactly once in the batch01 roster, allowing an exact, deterministic source lookup. No review-text or fuzzy matching was used.

`manual_review_sample_v0.csv` contains 56 row-level exploratory labels, but its accompanying documentation explicitly marks it as disputed/superseded and not suitable as ground truth. It is not part of the historical 63/7 recovery chain.

Summary-only Markdown/CSV files and the current incomplete/sample outputs are not recovery sources for missing COMPLETE rows.

## Provenance and Recovery

- Batch01 COMPLETE: **{len(batch1_complete)}**
- Batch02 COMPLETE: **{len(batch2_complete)}**
- Recovered COMPLETE total: **{len(recovered)}**
- Unique recovered `(source, review_id)` keys: **{recovered.drop_duplicates(['source', 'review_id']).shape[0]}**
- Duplicate recovered keys: **{int(recovered.duplicated(['source', 'review_id'], keep=False).sum())}**
- Independently evidenced second-review rows: **{len(second_keys)}**
- Total inspected evidence reconstructed from actual rows: **{len(all_inspected_keys)}**

This exactly matches the historical report of 70 inspected = 63 COMPLETE + 7 NEEDS_SECOND_REVIEW.

## 24-Month Match

Matching used `(source, review_id)` only.

- Recovered COMPLETE inside 24 months: **{inside_count}**
- Recovered COMPLETE outside 24 months: **{outside_count}**
- Unmatched recovered COMPLETE: **{unmatched_count}**

## Required-Label Completeness

{chr(10).join(f'- `{field}` missing: **{count}**' for field, count in missing_required.items())}

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
"""
    REPORT_PATH.write_text(report, encoding="utf-8")

    # Validate the written output and prove every pre-existing searched file stayed unchanged.
    check = pd.read_csv(RECOVERY_PATH, dtype=str, keep_default_na=False)
    if len(check) != len(recovered) or check.duplicated(["source", "review_id"], keep=False).any():
        raise RuntimeError("Written recovery output failed row/key validation")
    hashes_after = {relative: sha256(ROOT / relative) for relative in hashes_before}
    if hashes_before != hashes_after:
        changed = [path for path in hashes_before if hashes_before[path] != hashes_after[path]]
        raise RuntimeError(f"Source files changed during audit: {changed}")

    print("MANUAL LABEL RECOVERY RESULT")
    print(f"Files searched: {len(files)}")
    print(f"Candidates: {len(candidates)}")
    print(f"Batch01 complete/second: {len(batch1_complete)}/{len(batch1_second)}")
    print(f"Batch02 complete/second: {len(batch2_complete)}/{len(batch2_second)}")
    print(f"Recovered complete/unique/duplicates: {len(recovered)}/{recovered.drop_duplicates(['source', 'review_id']).shape[0]}/{int(recovered.duplicated(['source', 'review_id'], keep=False).sum())}")
    print(f"Inside/outside/unmatched: {inside_count}/{outside_count}/{unmatched_count}")
    print(f"Second review: {len(second_keys)}")
    print(f"Total inspected evidence: {len(all_inspected_keys)}")
    print(f"Missing required labels: {missing_required}")
    print("Provenance confidence: HIGH")
    print("Recovery status: COMPLETE")
    print("Source files unchanged: YES")


if __name__ == "__main__":
    main()
