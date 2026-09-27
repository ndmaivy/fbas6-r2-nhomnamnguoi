"""QA Adjudication Batch 8: flagged reviews 70-79 (10 reviews)."""
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
batch_reviews = flagged[70:80]

ADJUDICATIONS = {
    "eddf39d9-bd84-4593-8b55-0d8756ca835e": [
        {"incident_id": "Google_Play-eddf39d9-bd84-4593-8b55-0d8756ca835e-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague insult 'ap lỏ vl'; UNCLEAR appropriate."}
    ],
    "d8a64903-58c4-4159-884f-be5a0131e94f": [
        {"incident_id": "Google_Play-d8a64903-58c4-4159-884f-be5a0131e94f-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague service criticism; UNCLEAR appropriate."}
    ],
    "13867043839": [
        {"incident_id": "App_Store-13867043839-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague slow processing; OTHER acceptable."}
    ],
    "419c55b8-4ad2-4635-86f5-ae0c0f00c000": [
        {"incident_id": "Google_Play-419c55b8-4ad2-4635-86f5-ae0c0f00c000-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Too many errors; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "03428347-9975-4510-a132-6bdefbeee40f": [
        {"incident_id": "Google_Play-03428347-9975-4510-a132-6bdefbeee40f-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "IT team management poor; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "13994219702": [
        {"incident_id": "App_Store-13994219702-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Advisory/contract unclear; CUSTOMER_SUPPORT appropriate."},
        {"incident_id": "App_Store-13994219702-02",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Staff only work business hours; CUSTOMER_SUPPORT appropriate."}
    ],
    "14005255766": [
        {"incident_id": "App_Store-14005255766-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "APP_STORE_REGION_AVAILABILITY", "final_journey": "OTHER", "final_severity": "LOW",
         "new_theme_decision": "NEW_THEME_CONFIRMED", "reason": "App not available in user's App Store region; single isolated case but real distinct issue; confirm as new theme for tracking."}
    ],
    "14007820033": [],
    "14007834537": [],
    "14007842869": [
        {"incident_id": "App_Store-14007842869-01",
         "decision": "KEEP", "final_family": "TRADING_ORDER_EXECUTION", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Can't sell at peak price; TRADING_ORDER_EXECUTION appropriate; MEDIUM confidence reflects unclear root cause."}
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
prog["current_batch"] = "QA Batch 8 (flagged reviews 70-79)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:35:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 8 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
