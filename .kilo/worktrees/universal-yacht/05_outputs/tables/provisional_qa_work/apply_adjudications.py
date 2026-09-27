"""Apply QA adjudications to create corrected outputs and final artifacts."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(".")
WORK = ROOT / "05_outputs/tables/provisional_qa_work"

with open(WORK / "qa_adjudication_checkpoint.csv", encoding="utf-8-sig") as f:
    adjudications = list(csv.DictReader(f))

adj_by_incident = {a["incident_id"]: a for a in adjudications}

with open(ROOT / "01_data/processed/reviews_classified_24m_provisional.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))
with open(ROOT / "01_data/processed/review_incidents_24m_provisional.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

adj_incidents = []
incident_count_by_review = Counter()
for inc in incidents:
    iid = inc["incident_id"]
    adj = adj_by_incident.get(iid)
    if adj and adj["decision"] not in ("", "N/A"):
        new_inc = dict(inc)
        if adj["decision"] == "REMOVE_INCIDENT":
            continue
        new_inc["pain_point_family"] = adj["final_family"]
        new_inc["pain_point_subtype"] = adj["final_subtype"]
        new_inc["journey"] = adj["final_journey"]
        new_inc["severity"] = adj["final_severity"]
        adj_incidents.append(new_inc)
        incident_count_by_review[inc["review_id"]] += 1
    else:
        adj_incidents.append(inc)
        incident_count_by_review[inc["review_id"]] += 1

adj_reviews = []
for r in reviews:
    new_r = dict(r)
    rid = r["review_id"]
    r_incidents = [i for i in adj_incidents if i["review_id"] == rid]
    new_r["incident_count"] = len(r_incidents)
    new_r["incident_present"] = len(r_incidents) > 0
    if r_incidents:
        new_r["primary_pain_point_family"] = r_incidents[0]["pain_point_family"]
        new_r["primary_pain_point_subtype"] = r_incidents[0]["pain_point_subtype"]
        new_r["primary_journey"] = r_incidents[0]["journey"]
        new_r["max_severity"] = r_incidents[0]["severity"]
    adj_reviews.append(new_r)

REVIEW_COLS = list(reviews[0].keys())
INCIDENT_COLS = list(incidents[0].keys())

with open(ROOT / "01_data/processed/reviews_classified_24m_provisional_adjudicated.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=REVIEW_COLS)
    w.writeheader()
    w.writerows(adj_reviews)

with open(ROOT / "01_data/processed/review_incidents_24m_provisional_adjudicated.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=INCIDENT_COLS)
    w.writeheader()
    w.writerows(adj_incidents)

ADJ_OUT_COLS = [
    "source", "review_id", "incident_id",
    "original_family", "original_subtype", "original_journey", "original_severity",
    "decision", "final_family", "final_subtype", "final_journey", "final_severity",
    "new_theme_decision", "reason",
]
with open(ROOT / "05_outputs/tables/provisional_classification_adjudication.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ADJ_OUT_COLS)
    w.writeheader()
    w.writerows(adjudications)

decision_counts = Counter(a["decision"] for a in adjudications)
new_theme_decisions = Counter(a["new_theme_decision"] for a in adjudications if a["new_theme_decision"] not in ("", "N/A"))

removed_count = sum(1 for a in adjudications if a["decision"] == "REMOVE_INCIDENT")
flagged_review_keys = set()
with open(WORK / "qa_completed_review_keys.csv", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "|" in line:
            flagged_review_keys.add(line)
flagged_reviews_count = len(flagged_review_keys)

summary_rows = [
    {"metric": "flagged_reviews_total", "value": 93},
    {"metric": "flagged_reviews_reviewed", "value": flagged_reviews_count},
    {"metric": "flagged_incidents_total", "value": 103},
    {"metric": "flagged_incidents_reviewed", "value": sum(1 for a in adjudications if a["incident_id"] in {i["incident_id"] for i in incidents if i["review_id"] in {rk.split("|")[1] for rk in flagged_review_keys}})},
    {"metric": "additional_nonflagged_new_theme_incidents_total", "value": 12},
    {"metric": "additional_nonflagged_new_theme_incidents_reviewed", "value": 12},
    {"metric": "total_incidents_adjudicated", "value": len(adjudications)},
    {"metric": "decision_KEEP", "value": decision_counts.get("KEEP", 0)},
    {"metric": "decision_RECODE_FAMILY", "value": decision_counts.get("RECODE_FAMILY", 0)},
    {"metric": "decision_RECODE_SUBTYPE", "value": decision_counts.get("RECODE_SUBTYPE", 0)},
    {"metric": "decision_RECODE_JOURNEY", "value": decision_counts.get("RECODE_JOURNEY", 0)},
    {"metric": "decision_RECODE_SEVERITY", "value": decision_counts.get("RECODE_SEVERITY", 0)},
    {"metric": "decision_REMOVE_INCIDENT", "value": decision_counts.get("REMOVE_INCIDENT", 0)},
    {"metric": "decision_SPLIT_INCIDENT", "value": decision_counts.get("SPLIT_INCIDENT", 0)},
    {"metric": "decision_MERGE_INCIDENT", "value": decision_counts.get("MERGE_INCIDENT", 0)},
    {"metric": "decision_UNCLEAR", "value": decision_counts.get("UNCLEAR", 0)},
    {"metric": "new_theme_total_corpus", "value": 18},
    {"metric": "new_theme_RECLASSIFIED_TO_EXISTING", "value": new_theme_decisions.get("RECLASSIFIED_TO_EXISTING", 0)},
    {"metric": "new_theme_CONFIRMED", "value": new_theme_decisions.get("NEW_THEME_CONFIRMED", 0)},
    {"metric": "new_theme_UNCLEAR", "value": new_theme_decisions.get("UNCLEAR", 0)},
    {"metric": "incidents_removed", "value": removed_count},
    {"metric": "review_rows_after_qa", "value": len(adj_reviews)},
    {"metric": "incident_rows_after_qa", "value": len(adj_incidents)},
]

with open(ROOT / "05_outputs/tables/provisional_qa_summary.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["metric", "value"])
    w.writeheader()
    w.writerows(summary_rows)

print(f"Adjudicated reviews: {len(adj_reviews)}")
print(f"Adjudicated incidents: {len(adj_incidents)}")
print(f"Removed incidents: {removed_count}")
print(f"Decision counts: {dict(decision_counts)}")
print(f"New theme decisions: {dict(new_theme_decisions)}")
print(f"Wrote provisional_classification_adjudication.csv with {len(adjudications)} rows")
print(f"Wrote provisional_qa_summary.csv with {len(summary_rows)} metrics")
