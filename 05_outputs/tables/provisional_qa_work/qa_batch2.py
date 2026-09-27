"""QA Adjudication Batch 2: flagged reviews 10-19 (10 reviews)."""
import csv
import json
from pathlib import Path

WORK = Path("05_outputs/tables/provisional_qa_work")

with open(WORK / "qa_progress.json") as f:
    prog = json.load(f)
with open(WORK / "qa_completed_review_keys.csv", encoding="utf-8") as f:
    completed_keys = set(l.strip() for l in f if l.strip() and "|" in l)
with open(WORK / "qa_completed_incident_ids.csv", encoding="utf-8") as f:
    completed_inc_ids = set(l.strip() for l in f if l.strip())

with open("01_data/processed/reviews_classified_24m_provisional.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))
with open("01_data/processed/review_incidents_24m_provisional.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

flagged = sorted(
    [r for r in reviews if r["needs_human_review"] == "True"],
    key=lambda x: (x["review_date"], x["source"], x["review_id"]),
)
batch_reviews = flagged[10:20]

ADJUDICATIONS = {
    "12166129599": [
        {"incident_id": "App_Store-12166129599-01",
         "decision": "KEEP", "final_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Money held after transfer is DEPOSIT_WITHDRAWAL_TRANSFER; 'lừa đảo' is user perception."}
    ],
    "12166276133": [
        {"incident_id": "App_Store-12166276133-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague insult with no specific issue; UNCLEAR appropriate."}
    ],
    "bd974c97-210a-4d21-b82a-061dcf6f9d90": [
        {"incident_id": "Google_Play-bd974c97-210a-4d21-b82a-061dcf6f9d90-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Mixed/confusing text with no clear issue; UNCLEAR appropriate."}
    ],
    "361acf1b-88b1-48b5-bddc-8ad9f98e0eca": [
        {"incident_id": "Google_Play-361acf1b-88b1-48b5-bddc-8ad9f98e0eca-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Request to revert to old version implies new version UX is worse; borderline feature_request/friction; UX_NAVIGATION_COMPLEXITY acceptable."}
    ],
    "bafa4c19-4760-4299-b62a-867de951e07e": [
        {"incident_id": "Google_Play-bafa4c19-4760-4299-b62a-867de951e07e-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague quality complaint about new version; PERFORMANCE_RELIABILITY acceptable as degradation could include performance."}
    ],
    "b688ac8c-082a-4976-8c70-99f9430abc75": [
        {"incident_id": "Google_Play-b688ac8c-082a-4976-8c70-99f9430abc75-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Single-word 'Tệ' with no specific issue; UNCLEAR appropriate."}
    ],
    "01e975f4-5aa8-4faf-b486-40c742040df8": [
        {"incident_id": "Google_Play-01e975f4-5aa8-4faf-b486-40c742040df8-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "New version slow, hard to follow; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "4b3c680c-14f7-44c1-8af3-2e40c1b2080b": [
        {"incident_id": "Google_Play-4b3c680c-14f7-44c1-8af3-2e40c1b2080b-01",
         "decision": "RECODE_JOURNEY", "final_family": "SECURITY_ACCOUNT_PROTECTION", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "'Worst security app' is a general security perception, not a login-specific issue; recode journey to GENERAL_CROSS_JOURNEY."},
        {"incident_id": "Google_Play-4b3c680c-14f7-44c1-8af3-2e40c1b2080b-02",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "UI/UX terrible with unnecessary features is UX_NAVIGATION_COMPLEXITY."}
    ],
    "12356932020": [
        {"incident_id": "App_Store-12356932020-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague warning with no specific issue; UNCLEAR appropriate."}
    ],
    "12381075336": [
        {"incident_id": "App_Store-12381075336-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "New version worse than old; UX_NAVIGATION_COMPLEXITY acceptable."}
    ],
}

ADJ_COLS = [
    "source", "review_id", "incident_id",
    "original_family", "original_subtype", "original_journey", "original_severity",
    "decision", "final_family", "final_subtype", "final_journey", "final_severity",
    "new_theme_decision", "reason",
]

adj_rows = []
batch_completed_keys = []
batch_completed_inc_ids = []

for r in batch_reviews:
    rid = r["review_id"]
    src = r["source"]
    key = f"{src}|{rid}"
    if key in completed_keys:
        continue
    incs = [i for i in incidents if i["review_id"] == rid]
    adjs = ADJUDICATIONS.get(rid, [])
    for adj in adjs:
        iid = adj["incident_id"]
        if iid in completed_inc_ids:
            continue
        orig = next((i for i in incs if i["incident_id"] == iid), None)
        if orig is None:
            print(f"MISSING INCIDENT: {iid}")
            continue
        adj_rows.append({
            "source": src, "review_id": rid, "incident_id": iid,
            "original_family": orig["pain_point_family"], "original_subtype": orig["pain_point_subtype"],
            "original_journey": orig["journey"], "original_severity": orig["severity"],
            "decision": adj["decision"], "final_family": adj["final_family"], "final_subtype": adj["final_subtype"],
            "final_journey": adj["final_journey"], "final_severity": adj["final_severity"],
            "new_theme_decision": adj["new_theme_decision"], "reason": adj["reason"],
        })
        batch_completed_inc_ids.append(iid)
    batch_completed_keys.append(key)

with open(WORK / "qa_adjudication_checkpoint.csv", "a", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ADJ_COLS)
    for row in adj_rows:
        w.writerow(row)
with open(WORK / "qa_completed_review_keys.csv", "a", encoding="utf-8") as f:
    for k in batch_completed_keys:
        f.write(k + "\n")
with open(WORK / "qa_completed_incident_ids.csv", "a", encoding="utf-8") as f:
    for iid in batch_completed_inc_ids:
        f.write(iid + "\n")

prog["completed_flagged_reviews"] += len(batch_completed_keys)
prog["completed_flagged_incidents"] += len(batch_completed_inc_ids)
prog["remaining_flagged_reviews"] = prog["flagged_reviews_total"] - prog["completed_flagged_reviews"]
prog["remaining_incidents"] = (prog["flagged_incidents_total"] + prog["additional_nonflagged_new_theme_incidents"]) - (prog["completed_flagged_incidents"] + prog["completed_additional_new_theme_incidents"])
prog["current_batch"] = "QA Batch 2 (flagged reviews 10-19)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:05:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 2 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
