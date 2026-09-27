"""QA Adjudication Batch 6: flagged reviews 50-59 (10 reviews)."""
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
batch_reviews = flagged[50:60]

ADJUDICATIONS = {
    "abd0bdab-c53b-4138-adfa-4b4f95d9a19b": [
        {"incident_id": "Google_Play-abd0bdab-c53b-4138-adfa-4b4f95d9a19b-01",
         "decision": "KEEP", "final_family": "AUTHENTICATION_IOTP", "final_subtype": "", "final_journey": "LOGIN_AUTHENTICATION", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Face verification issue; AUTHENTICATION_IOTP appropriate."}
    ],
    "e17a1244-02e2-46a7-b4e8-ef5e21919c2c": [
        {"incident_id": "Google_Play-e17a1244-02e2-46a7-b4e8-ef5e21919c2c-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Ko vào dc' is performance/access issue; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "f1abd52a-0825-4c19-98ca-a772b551d34a": [
        {"incident_id": "Google_Play-f1abd52a-0825-4c19-98ca-a772b551d34a-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Nhiều chức năng nhưng khó dùng' is UX complaint; UX_NAVIGATION_COMPLEXITY appropriate."}
    ],
    "13172558353": [
        {"incident_id": "App_Store-13172558353-01",
         "decision": "KEEP", "final_family": "AI_SUPPORT_CONTEXT_QUALITY", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "AI support unhelpful; AI_SUPPORT_CONTEXT_QUALITY appropriate."},
        {"incident_id": "App_Store-13172558353-02",
         "decision": "KEEP", "final_family": "FEE_PRICING", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Overnight fee charges perceived as fraud; FEE_PRICING appropriate; 'lừa đảo gian dối' is user perception."}
    ],
    "6d68116a-74e9-4e8e-be7c-43b6078415c3": [
        {"incident_id": "Google_Play-6d68116a-74e9-4e8e-be7c-43b6078415c3-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague criticism of app/web quality; OTHER acceptable."}
    ],
    "7a5988b3-cc5f-4f88-b009-631bee990259": [
        {"incident_id": "Google_Play-7a5988b3-cc5f-4f88-b009-631bee990259-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague error report; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "13416185136": [
        {"incident_id": "App_Store-13416185136-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague fraud warning; UNCLEAR appropriate."}
    ],
    "13476352525": [
        {"incident_id": "App_Store-13476352525-01",
         "decision": "KEEP", "final_family": "TRADING_ORDER_EXECUTION", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Can't sell when needed; TRADING_ORDER_EXECUTION appropriate."},
        {"incident_id": "App_Store-13476352525-02",
         "decision": "RECODE_FAMILY", "final_family": "FEE_PRICING", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Trừ tiền ko minh bạch' is fee transparency issue; recode from NOTIFICATION_COMMUNICATION to FEE_PRICING per codebook 'fee clarity'."},
        {"incident_id": "App_Store-13476352525-03",
         "decision": "KEEP", "final_family": "AI_SUPPORT_CONTEXT_QUALITY", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "AI support on phone and chat; AI_SUPPORT_CONTEXT_QUALITY appropriate."}
    ],
    "13572114993": [
        {"incident_id": "App_Store-13572114993-01",
         "decision": "KEEP", "final_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Deposit verification too strict; DEPOSIT_WITHDRAWAL_TRANSFER appropriate."}
    ],
    "547f969e-0676-4e7d-a158-d1c32569d075": [
        {"incident_id": "Google_Play-547f969e-0676-4e7d-a158-d1c32569d075-01",
         "decision": "KEEP", "final_family": "TRADING_ORDER_EXECUTION", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Customer lost money; TRADING_ORDER_EXECUTION reasonable; MEDIUM confidence reflects vagueness."}
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
prog["current_batch"] = "QA Batch 6 (flagged reviews 50-59)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:25:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 6 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
