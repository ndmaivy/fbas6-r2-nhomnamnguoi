"""QA Adjudication Batch 10: 12 non-flagged new_theme incidents."""
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

flagged_rids = set(r["review_id"] for r in reviews if r["needs_human_review"] == "True")
new_theme_all = [i for i in incidents if i["new_theme_flag"] == "True"]
new_theme_outside = [i for i in new_theme_all if i["review_id"] not in flagged_rids]

ADJUDICATIONS = {
    "Google_Play-f93f9a8e-c094-4ceb-8268-f4ba73dbb18c-01": {
        "review_id": "f93f9a8e-c094-4ceb-8268-f4ba73dbb18c",
        "source": "Google Play",
        "decision": "RECODE_FAMILY", "final_family": "ONBOARDING_KYC", "final_subtype": "DIGITAL_SIGNATURE_CONTEXT", "final_journey": "ACCOUNT_OPENING_KYC", "final_severity": "HIGH",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Digital signature flow failure per codebook is ONBOARDING_KYC candidate subtype; recode from OTHER to canonical family."
    },
    "Google_Play-033b8a01-f565-4002-a7dc-d7432622c677-01": {
        "review_id": "033b8a01-f565-4002-a7dc-d7432622c677",
        "source": "Google Play",
        "decision": "UNCLEAR", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "UNCLEAR",
        "reason": "Cosmetic icon color request for feng shui; single isolated case, insufficient evidence for recurring theme."
    },
    "App_Store-12472251645-01": {
        "review_id": "12472251645",
        "source": "App Store",
        "decision": "RECODE_FAMILY", "final_family": "TRADING_ORDER_EXECUTION", "final_subtype": "", "final_journey": "TRADING_ORDER_MANAGEMENT", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Feature request for margin/leverage from unrealized gains fits TRADING_ORDER_EXECUTION (trading feature domain)."
    },
    "App_Store-12741234952-01": {
        "review_id": "12741234952",
        "source": "App Store",
        "decision": "RECODE_FAMILY", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "App naming/search confusion is UX/brand issue; recode from OTHER to UX_NAVIGATION_COMPLEXITY."
    },
    "Google_Play-a922e373-6084-42f3-913c-8ce9ee95dcc4-01": {
        "review_id": "a922e373-6084-42f3-913c-8ce9ee95dcc4",
        "source": "Google Play",
        "decision": "RECODE_FAMILY", "final_family": "PRODUCT_DISCOVERY_MARKET_DATA", "final_subtype": "", "final_journey": "PRODUCT_DISCOVERY_MARKET_DATA", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Feature request for more fund listings is product discovery; recode from OTHER to PRODUCT_DISCOVERY_MARKET_DATA."
    },
    "App_Store-12956820659-01": {
        "review_id": "12956820659",
        "source": "App Store",
        "decision": "RECODE_FAMILY", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "MOBILE_TABLET_LAYOUT", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Font size accessibility is UI sizing issue; recode from OTHER to UX_NAVIGATION_COMPLEXITY with MOBILE_TABLET_LAYOUT candidate subtype."
    },
    "App_Store-12967217625-01": {
        "review_id": "12967217625",
        "source": "App Store",
        "decision": "UNCLEAR", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "UNCLEAR",
        "reason": "Feature request for a removed feature but no description of which feature; insufficient evidence."
    },
    "App_Store-13711043247-01": {
        "review_id": "13711043247",
        "source": "App Store",
        "decision": "UNCLEAR", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "UNCLEAR",
        "reason": "Community feature complaint is vague; insufficient evidence about what community feature or specific issue."
    },
    "Google_Play-26405e29-6e00-44eb-8547-08c38fa7beca-01": {
        "review_id": "26405e29-6e00-44eb-8547-08c38fa7beca",
        "source": "Google Play",
        "decision": "UNCLEAR", "final_family": "OTHER", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "UNCLEAR",
        "reason": "Feature request for child account with fund purchase is vague; insufficient evidence about specific capability gap."
    },
    "App_Store-13857042814-01": {
        "review_id": "13857042814",
        "source": "App Store",
        "decision": "RECODE_FAMILY", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Localization/internationalization issue is UX concern; recode from OTHER to UX_NAVIGATION_COMPLEXITY."
    },
    "Google_Play-8c8bebe4-06ea-4546-9533-66d3e4d79109-01": {
        "review_id": "8c8bebe4-06ea-4546-9533-66d3e4d79109",
        "source": "Google Play",
        "decision": "RECODE_FAMILY", "final_family": "UX_NAVIGATION_COMPLEXITY", "final_subtype": "MOBILE_TABLET_LAYOUT", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "LOW",
        "new_theme_decision": "RECLASSIFIED_TO_EXISTING",
        "reason": "Tablet landscape optimization is mobile/tablet layout issue; recode from OTHER to UX_NAVIGATION_COMPLEXITY with MOBILE_TABLET_LAYOUT subtype."
    },
    "App_Store-14548034358-03": {
        "review_id": "14548034358",
        "source": "App Store",
        "decision": "KEEP", "final_family": "NOTIFICATION_COMMUNICATION", "final_subtype": "EXCESSIVE_ADS", "final_journey": "GENERAL_CROSS_JOURNEY", "final_severity": "MEDIUM",
        "new_theme_decision": "NEW_THEME_CONFIRMED",
        "reason": "Excessive IPO ads is a new theme subtype within existing NOTIFICATION_COMMUNICATION family; keep family, confirm new subtype."
    },
}

ADJ_COLS = [
    "source", "review_id", "incident_id",
    "original_family", "original_subtype", "original_journey", "original_severity",
    "decision", "final_family", "final_subtype", "final_journey", "final_severity",
    "new_theme_decision", "reason",
]

adj_rows = []
new_completed_review_keys = set()

for iid, adj in ADJUDICATIONS.items():
    if iid in completed_inc_ids:
        continue
    orig = next((i for i in incidents if i["incident_id"] == iid), None)
    if orig is None:
        print(f"MISSING INCIDENT: {iid}")
        continue
    adj_rows.append({
        "source": adj["source"], "review_id": adj["review_id"], "incident_id": iid,
        "original_family": orig["pain_point_family"], "original_subtype": orig["pain_point_subtype"],
        "original_journey": orig["journey"], "original_severity": orig["severity"],
        "decision": adj["decision"], "final_family": adj["final_family"], "final_subtype": adj["final_subtype"],
        "final_journey": adj["final_journey"], "final_severity": adj["final_severity"],
        "new_theme_decision": adj["new_theme_decision"], "reason": adj["reason"],
    })
    new_completed_review_keys.add(f"{adj['source']}|{adj['review_id']}")

with open(WORK / "qa_adjudication_checkpoint.csv", "a", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ADJ_COLS)
    for row in adj_rows:
        w.writerow(row)
with open(WORK / "qa_completed_incident_ids.csv", "a", encoding="utf-8") as f:
    for iid in [a["incident_id"] for a in adj_rows]:
        f.write(iid + "\n")

prog["completed_additional_new_theme_incidents"] += len(adj_rows)
prog["remaining_incidents"] = (prog["flagged_incidents_total"] + prog["additional_nonflagged_new_theme_incidents"]) - (prog["completed_flagged_incidents"] + prog["completed_additional_new_theme_incidents"])
prog["current_batch"] = "QA Batch 10 (12 non-flagged new_theme incidents)"
prog["updated_at"] = "2026-09-23T07:45:00"
with open(WORK / "qa_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"QA Batch 10 done: {len(adj_rows)} non-flagged new_theme incidents adjudicated")
print(f"Progress: {prog['completed_flagged_incidents']}/{prog['flagged_incidents_total']} flagged incidents, {prog['completed_additional_new_theme_incidents']}/{prog['additional_nonflagged_new_theme_incidents']} additional new_theme incidents")
print(f"Remaining: {prog['remaining_incidents']} total incidents")
