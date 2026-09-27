"""QA Adjudication Batch 7: flagged reviews 60-69 (10 reviews)."""
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
batch_reviews = flagged[60:70]

ADJUDICATIONS = {
    "29e01899-efa2-4546-8421-6b2abf4bf775": [
        {"incident_id": "Google_Play-29e01899-efa2-4546-8421-6b2abf4bf775-01",
         "decision": "KEEP", "final_family": "TRADING_ORDER_EXECUTION", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Can't place/cancel orders; TRADING_ORDER_EXECUTION appropriate."},
        {"incident_id": "Google_Play-29e01899-efa2-4546-8421-6b2abf4bf775-02",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "No support for error handling; CUSTOMER_SUPPORT appropriate."},
        {"incident_id": "Google_Play-29e01899-efa2-4546-8421-6b2abf4bf775-03",
         "decision": "KEEP", "final_family": "FEE_PRICING", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "High margin rate; FEE_PRICING appropriate."}
    ],
    "6e30c2fa-02e6-43ad-818c-1dae839ff8d8": [
        {"incident_id": "Google_Play-6e30c2fa-02e6-43ad-818c-1dae839ff8d8-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Single-word 'Tệ'; UNCLEAR appropriate."}
    ],
    "a8c833fb-d991-4ed4-8ec3-eac4602bb61f": [
        {"incident_id": "Google_Play-a8c833fb-d991-4ed4-8ec3-eac4602bb61f-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague staff criticism; UNCLEAR appropriate."}
    ],
    "13703439891": [
        {"incident_id": "App_Store-13703439891-01",
         "decision": "KEEP", "final_family": "ONBOARDING_KYC", "final_subtype": "", "final_journey": "ACCOUNT_OPENING_KYC", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Verification time too long; ONBOARDING_KYC appropriate."}
    ],
    "13729660566": [
        {"incident_id": "App_Store-13729660566-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague negative experience; OTHER acceptable."}
    ],
    "13732547803": [
        {"incident_id": "App_Store-13732547803-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Trading UI design bad; UX_NAVIGATION_COMPLEXITY with TRADING journey appropriate."}
    ],
    "62c0e271-0108-42d1-b984-d8d269e8da8c": [
        {"incident_id": "Google_Play-62c0e271-0108-42d1-b984-d8d269e8da8c-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague 'app siêu tệ'; OTHER acceptable."}
    ],
    "13785950483": [
        {"incident_id": "App_Store-13785950483-01",
         "decision": "RECODE_FAMILY", "final_family": "ONBOARDING_KYC", "final_subtype": "", "final_journey": "ACCOUNT_OPENING_KYC", "final_severity": "MEDIUM",
         "new_theme_decision": "RECLASSIFIED_TO_EXISTING", "reason": "Forced account linking during onboarding fits ONBOARDING_KYC; recode from OTHER to canonical family."}
    ],
    "13e0c0e6-6e6c-4bdb-b12e-8fedf3068801": [
        {"incident_id": "Google_Play-13e0c0e6-6e6c-4bdb-b12e-8fedf3068801-01",
         "decision": "KEEP", "final_family": "ONBOARDING_KYC", "final_subtype": "", "final_journey": "ACCOUNT_OPENING_KYC", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Registration slow; ONBOARDING_KYC appropriate."}
    ],
    "13790529670": [
        {"incident_id": "App_Store-13790529670-01",
         "decision": "RECODE_FAMILY", "final_family": "NOTIFICATION_COMMUNICATION", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "RECLASSIFIED_TO_EXISTING", "reason": "Gamification/promotion with 26 lucky bags of greetings is excessive promotional content; recode from OTHER to NOTIFICATION_COMMUNICATION."}
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
prog["current_batch"] = "QA Batch 7 (flagged reviews 60-69)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:30:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 7 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
