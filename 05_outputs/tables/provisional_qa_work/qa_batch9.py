"""QA Adjudication Batch 9: flagged reviews 80-92 (13 reviews, last batch)."""
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
batch_reviews = flagged[80:93]

ADJUDICATIONS = {
    "eb3e3875-2bc9-4ce9-9808-9f937dd15a69": [
        {"incident_id": "Google_Play-eb3e3875-2bc9-4ce9-9808-9f937dd15a69-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "'App hãy lỗi' (typo for 'hay lỗi'); PERFORMANCE_RELIABILITY appropriate."}
    ],
    "b5161b29-c1a7-41da-b77f-d8fd16a97d00": [
        {"incident_id": "Google_Play-b5161b29-c1a7-41da-b77f-d8fd16a97d00-01",
         "decision": "KEEP", "final_family": "UNCLEAR", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "NONE",
         "new_theme_decision": "N/A", "reason": "Vague holiday reference; UNCLEAR appropriate."}
    ],
    "92b45d0c-73a1-46bf-9bb5-6218ab82e507": [
        {"incident_id": "Google_Play-92b45d0c-73a1-46bf-9bb5-6218ab82e507-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "App hard to use; UX_NAVIGATION_COMPLEXITY appropriate."},
        {"incident_id": "Google_Play-92b45d0c-73a1-46bf-9bb5-6218ab82e507-02",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Service delay too long; CUSTOMER_SUPPORT appropriate."}
    ],
    "14045600270": [
        {"incident_id": "App_Store-14045600270-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "'Lỗi 2 ngày rồi'; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "1dbfd40c-06ac-4217-a552-6b7b70e93f14": [
        {"incident_id": "Google_Play-1dbfd40c-06ac-4217-a552-6b7b70e93f14-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "NONE",
         "new_theme_decision": "N/A", "reason": "Vague praise; OTHER acceptable for general positive."}
    ],
    "8d63919e-1d1f-4fec-bd8b-be215087e6b5": [
        {"incident_id": "Google_Play-8d63919e-1d1f-4fec-bd8b-be215087e6b5-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "UX extremely bad; UX_NAVIGATION_COMPLEXITY appropriate."}
    ],
    "14142865973": [],
    "14280577109": [
        {"incident_id": "App_Store-14280577109-01",
         "decision": "RECODE_FAMILY", "final_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "LOW",
         "new_theme_decision": "RECLASSIFIED_TO_EXISTING", "reason": "Feature request for crypto deposit fits DEPOSIT_WITHDRAWAL_TRANSFER (deposit feature); recode from MARKET_RESEARCH_RECOMMENDATION_UTILITY to canonical family."}
    ],
    "14352633073": [
        {"incident_id": "App_Store-14352633073-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "No support staff, poor service; CUSTOMER_SUPPORT appropriate."}
    ],
    "14465018475": [],
    "14467591535": [],
    "14468902446": [
        {"incident_id": "App_Store-14468902446-01",
         "decision": "KEEP", "final_family": "SECURITY_ACCOUNT_PROTECTION", "final_subtype": "DATA_SELLING_SUSPICION", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "HIGH",
         "new_theme_decision": "NEW_THEME_CONFIRMED", "reason": "Data selling suspicion is a new theme subtype within existing SECURITY_ACCOUNT_PROTECTION family; keep family, confirm new subtype."}
    ],
    "14504211053": [
        {"incident_id": "App_Store-14504211053-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Trading app very slow; PERFORMANCE_RELIABILITY appropriate."}
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
prog["current_batch"] = "QA Batch 9 (flagged reviews 80-92, last)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:40:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 9 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
