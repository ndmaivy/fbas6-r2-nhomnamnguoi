"""QA Adjudication Batch 4: flagged reviews 30-39 (10 reviews)."""
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
batch_reviews = flagged[30:40]

ADJUDICATIONS = {
    "12530510462": [
        {"incident_id": "App_Store-12530510462-01",
         "decision": "KEEP", "final_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Money arrival slow; DEPOSIT_WITHDRAWAL_TRANSFER appropriate."},
        {"incident_id": "App_Store-12530510462-02",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "UI should learn from SSI; UX_NAVIGATION_COMPLEXITY appropriate."}
    ],
    "12545090227": [
        {"incident_id": "App_Store-12545090227-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Frequent errors; PERFORMANCE_RELIABILITY appropriate."},
        {"incident_id": "App_Store-12545090227-02",
         "decision": "KEEP", "final_family": "AI_SUPPORT_CONTEXT_QUALITY", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "Phone only reaches robot, Zalo/Mess unanswered; AI_SUPPORT_CONTEXT_QUALITY appropriate."},
        {"incident_id": "App_Store-12545090227-03",
         "decision": "RECODE_FAMILY", "final_family": "PORTFOLIO_ACCOUNT_INFORMATION", "final_subtype": "", "final_journey": "PORTFOLIO_TRACKING", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "'Số dư tài khoản mất' is account balance display issue; recode from broad PRODUCT_PORTFOLIO_INFORMATION to canonical PORTFOLIO_ACCOUNT_INFORMATION per codebook."}
    ],
    "12617407260": [
        {"incident_id": "App_Store-12617407260-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague insult 'app ngôn lù'; UNCLEAR appropriate."}
    ],
    "12683550678": [
        {"incident_id": "App_Store-12683550678-01",
         "decision": "KEEP", "final_family": "ONBOARDING_KYC", "final_subtype": "", "final_journey": "ACCOUNT_OPENING_KYC", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "CCCD verification app errors; ONBOARDING_KYC appropriate."},
        {"incident_id": "App_Store-12683550678-02",
         "decision": "KEEP", "final_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "final_subtype": "", "final_journey": "FUNDING_CASH_TRANSFER", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Withdrawal mentioned; DEPOSIT_WITHDRAWAL_TRANSFER appropriate despite ambiguous phrasing."},
        {"incident_id": "App_Store-12683550678-03",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'App rất rối' is UX complaint; UX_NAVIGATION_COMPLEXITY appropriate."}
    ],
    "39b03a78-64a0-478d-b52f-6a5272d179c3": [
        {"incident_id": "Google_Play-39b03a78-64a0-478d-b52f-6a5272d179c3-01",
         "decision": "KEEP", "final_family": "OTHER", "final_subtype": "", "final_journey": "UNKNOWN", "final_severity": "LOW",
         "new_theme_decision": "N/A", "reason": "Vague 'lỗi 23/5/25' with no specific issue; UNCLEAR appropriate."}
    ],
    "c61b6588-4baa-4af9-aab9-46fb38bcaa87": [
        {"incident_id": "Google_Play-c61b6588-4baa-4af9-aab9-46fb38bcaa87-01",
         "decision": "RECODE_JOURNEY", "final_family": "SECURITY_ACCOUNT_PROTECTION", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Data leak concern causing unsolicited calls is not a support interaction; recode journey to GENERAL_CROSS_JOURNEY."}
    ],
    "46fa6425-0a0f-4955-adfb-882bf8b4a5b5": [
        {"incident_id": "Google_Play-46fa6425-0a0f-4955-adfb-882bf8b4a5b5-01",
         "decision": "KEEP", "final_family": "AUTHENTICATION_IOTP", "final_subtype": "", "final_journey": "LOGIN_AUTHENTICATION", "final_severity": "HIGH",
         "new_theme_decision": "N/A", "reason": "OTP issue on app reinstall; AUTHENTICATION_IOTP appropriate."}
    ],
    "12850138790": [
        {"incident_id": "App_Store-12850138790-01",
         "decision": "KEEP", "final_family": "CUSTOMER_SUPPORT", "final_subtype": "", "final_journey": "CUSTOMER_SUPPORT", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Support slow issue handling; CUSTOMER_SUPPORT appropriate."}
    ],
    "12889467768": [
        {"incident_id": "App_Store-12889467768-01",
         "decision": "KEEP", "final_family": "PERFORMANCE_RELIABILITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "Vague 'Hay bị lỗi'; PERFORMANCE_RELIABILITY appropriate."}
    ],
    "12917524601": [
        {"incident_id": "App_Store-12917524601-01",
         "decision": "KEEP", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
         "new_theme_decision": "N/A", "reason": "'Khó dùng' is UX complaint; UX_NAVIGATION_COMPLEXITY appropriate."}
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
prog["current_batch"] = "QA Batch 4 (flagged reviews 30-39)"
prog["last_completed_review_key"] = batch_completed_keys[-1] if batch_completed_keys else prog["last_completed_review_key"]
prog["updated_at"] = "2026-09-23T07:15:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 4 done: {len(batch_completed_keys)} reviews, {len(batch_completed_inc_ids)} incidents adjudicated")
print(f"Progress: {prog['completed_flagged_reviews']}/{prog['flagged_reviews_total']} flagged reviews, {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents")
print(f"Remaining: {prog['remaining_flagged_reviews']} flagged reviews, {prog['remaining_incidents']} total incidents")
