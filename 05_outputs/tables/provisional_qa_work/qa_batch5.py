"""QA Adjudication Batch 5: flagged reviews 40-49 (10 reviews)."""
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
batch_reviews = flagged[40:50]

ADJUDICATIONS = {
    "9711f697-5d2f-4fcd-9813-75b1260ae8ce": [
        {"incident_id": "Google_Play-9711f697-5d2f-4fcd-9813-75b1260ae8ce-01",
         "decision": "RECODE_FAMILY", "final_family": "MARKET_DATA_INFORMATION", "final_subtype": "", "final_journey": "PRODUCT_DISCOVERY_MARKET_DATA", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Thông tin sai lệch' is market data staleness/accuracy; recode from subtype-name MARKET_DATA_STALENESS_ACCURACY to canonical MARKET_DATA_INFORMATION family per codebook."},
        {"incident_id": "Google_Play-9711f697-5d2f-4fcd-9813-75b1260ae8ce-02",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Support unreachable; CUSTOMER_SUPPORT appropriate."}
    ],
    "b8566b33-1451-4fbc-8976-a687b982c667": [
        {"incident_id": "Google_Play-b8566b33-1451-4fbc-8976-a687b982c667-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Toàn lỗi' is performance complaint; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "cd1b84a1-3d05-4f5c-953e-a15f48882c84": [
        {"incident_id": "Google_Play-cd1b84a1-3d05-4f5c-953e-a15f48882c84-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Frequent serious errors; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "12957364236": [
        {"incident_id": "App_Store-12957364236-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'App nhiều lỗi'; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "12964759767": [
        {"incident_id": "App_Store-12964759767-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'App gì mà lag lộn lên'; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "83ed0e5c-2150-41dc-b3fd-c90abf0cb2b5": [
        {"incident_id": "Google_Play-83ed0e5c-2150-41dc-b3fd-c90abf0cb2b5-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague 'app quá tệ' with no specific issue; OTHER acceptable for general negative."}
    ],
    "50a1fcce-0d4d-4327-a298-5625037db0c6": [
        {"incident_id": "Google_Play-50a1fcce-0d4d-4327-a298-5625037db0c6-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "UI and staff behavior both criticized; UX captures UI, staff behavior is secondary context."}
    ],
    "13030216864": [
        {"incident_id": "App_Store-13030216864-01",
         "decision": "UNCLEAR", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
         "new_theme_decision": "UNCLEAR", "reason": "Feature request to disable 'Cá mập thông thái' is unclear; insufficient evidence about what this feature is or its impact."}
    ],
    "28fbcc6b-2251-4028-bdb3-09111f7c0258": [
        {"incident_id": "Google_Play-28fbcc6b-2251-4028-bdb3-09111f7c0258-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "App loads nothing; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "13112614932": [
        {"incident_id": "App_Store-13112614932-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Không thể hiểu dc cách sử dụng app'; UX_NAVIGATION_COMPLEXITY appropriate."}
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
prog["current_batch"] = "QA Batch 5 (flagged reviews 40-49)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:20:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 5 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
