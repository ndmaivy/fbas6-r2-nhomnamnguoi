"""QA Adjudication Batch 1: flagged reviews 0-9 (10 reviews)."""
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
batch_reviews = flagged[0:10]

ADJUDICATIONS = {
    "11801692398": [
        {"incident_id": "App_Store-11801692398-01",
         "decision": "KEEP", "final_family": "", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "NONE",
         "new_theme_decision": "N/A", "reason": "Single-word praise; insufficient evidence for journey location; LOW confidence appropriate."}
    ],
    "a6034dee-e8e0-402f-ac3b-e4cebefc1248": [
        {"incident_id": "Google_Play-a6034dee-e8e0-402f-ac3b-e4cebefc1248-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Review/referral program non-payment is a support interaction; 'lừa đảo' is user perception not verified fraud."}
    ],
    "11836640608": [
        {"incident_id": "App_Store-11836640608-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Same review/referral program non-payment pattern; CUSTOMER_SUPPORT appropriate."}
    ],
    "cbbc87cf-77ee-4fec-931e-ea3e9a56ba2a": [
        {"incident_id": "Google_Play-cbbc87cf-77ee-4fec-931e-ea3e9a56ba2a-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Single-word 'Tệ' with no specific issue; UNCLEAR/OTHER/UNKNOWN is correct."}
    ],
    "e3f5cf46-2491-45ef-9268-c516fff48ea3": [
        {"incident_id": "Google_Play-e3f5cf46-2491-45ef-9268-c516fff48ea3-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Review/referral program non-payment; CUSTOMER_SUPPORT appropriate."}
    ],
    "4277ac82-b4c7-48b8-a1c3-18f4164e9ff0": [
        {"incident_id": "Google_Play-4277ac82-b4c7-48b8-a1c3-18f4164e9ff0-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "iChat locked without reason is a support access issue; HIGH severity appropriate for account access block."}
    ],
    "20eca2ba-c0a0-449e-ba64-0e62611515ff": [
        {"incident_id": "Google_Play-20eca2ba-c0a0-449e-ba64-0e62611515ff-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague policy complaint; CUSTOMER_SUPPORT is reasonable; LOW confidence reflects vagueness."}
    ],
    "de1bacde-5a2d-4fa0-a39c-2f1c03f716cd": [
        {"incident_id": "Google_Play-de1bacde-5a2d-4fa0-a39c-2f1c03f716cd-01",
         "decision": "RECODE_JOURNEY", "final_family": "NOTIFICATION_COMMUNICATION", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Unwanted phone calls are a communication issue, not a support interaction; recode journey to GENERAL_CROSS_JOURNEY."}
    ],
    "6025ead0-ff94-4e25-a54e-954e4535bed5": [
        {"incident_id": "Google_Play-6025ead0-ff94-4e25-a54e-954e4535bed5-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague performance complaint; PERFORMANCE_RELIABILITY/GENERAL_CROSS_JOURNEY appropriate."}
    ],
    "12004038909": [
        {"incident_id": "App_Store-12004038909-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague performance complaint; PERFORMANCE_RELIABILITY/GENERAL_CROSS_JOURNEY appropriate."}
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
            "source": src,
            "review_id": rid,
            "incident_id": iid,
            "original_family": orig["pain_point_family"],
            "original_subtype": orig["pain_point_subtype"],
            "original_journey": orig["journey"],
            "original_severity": orig["severity"],
            "decision": adj["decision"],
            "final_family": adj["final_family"],
            "final_subtype": adj["final_subtype"],
            "final_journey": adj["final_journey"],
            "final_severity": adj["final_severity"],
            "new_theme_decision": adj["new_theme_decision"],
            "reason": adj["reason"],
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
prog["current_batch"] = "QA Batch 1 (flagged reviews 0-9)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:00:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 1 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
