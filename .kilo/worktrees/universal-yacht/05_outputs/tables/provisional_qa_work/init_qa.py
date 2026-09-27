"""Initialize QA adjudication checkpoint infrastructure."""
import csv
import json
from pathlib import Path

WORK = Path("05_outputs/tables/provisional_qa_work")
WORK.mkdir(parents=True, exist_ok=True)

with open("01_data/processed/reviews_classified_24m_provisional.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))
with open("01_data/processed/review_incidents_24m_provisional.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

flagged = sorted(
    [r for r in reviews if r["needs_human_review"] == "True"],
    key=lambda x: (x["review_date"], x["source"], x["review_id"]),
)
flagged_rids = set(r["review_id"] for r in flagged)
flagged_incidents = [i for i in incidents if i["review_id"] in flagged_rids]
new_theme_all = [i for i in incidents if i["new_theme_flag"] == "True"]
new_theme_outside = [i for i in new_theme_all if i["review_id"] not in flagged_rids]

progress = {
    "flagged_reviews_total": len(flagged),
    "flagged_incidents_total": len(flagged_incidents),
    "new_theme_incidents_total": len(new_theme_all),
    "additional_nonflagged_new_theme_incidents": len(new_theme_outside),
    "completed_flagged_reviews": 0,
    "completed_flagged_incidents": 0,
    "completed_additional_new_theme_incidents": 0,
    "remaining_flagged_reviews": len(flagged),
    "remaining_incidents": len(flagged_incidents) + len(new_theme_outside),
    "current_batch": None,
    "last_completed_review_key": None,
    "updated_at": None,
}

with open(WORK / "qa_progress.json", "w") as f:
    json.dump(progress, f, indent=2)

with open(WORK / "qa_completed_review_keys.csv", "w", encoding="utf-8") as f:
    f.write("source|review_id\n")
with open(WORK / "qa_completed_incident_ids.csv", "w", encoding="utf-8") as f:
    f.write("incident_id\n")

ADJ_COLS = [
    "source", "review_id", "incident_id",
    "original_family", "original_subtype", "original_journey", "original_severity",
    "decision", "final_family", "final_subtype", "final_journey", "final_severity",
    "new_theme_decision", "reason",
]
with open(WORK / "qa_adjudication_checkpoint.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ADJ_COLS)
    w.writeheader()

print(f"Initialized QA work directory at {WORK}")
print(f"Flagged reviews: {len(flagged)}")
print(f"Flagged incidents: {len(flagged_incidents)}")
print(f"New theme outside flagged: {len(new_theme_outside)}")
print(f"Total adjudication target: {len(flagged_incidents) + len(new_theme_outside)}")
