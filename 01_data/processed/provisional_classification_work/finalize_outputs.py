"""Finalize provisional classification outputs.

Inputs:
  - 01_data/processed/provisional_classification_work/reviews_classified_checkpoint.csv
  - 01_data/processed/provisional_classification_work/incidents_classified_checkpoint.csv
  - 01_data/processed/provisional_classification_work/classification_progress.json

Outputs:
  - 01_data/processed/reviews_classified_24m_provisional.csv
  - 01_data/processed/review_incidents_24m_provisional.csv
  - 05_outputs/tables/provisional_classification_review_queue.csv
  - 05_outputs/tables/provisional_classification_summary.csv
  - 04_analysis/validation/provisional_classification_validation.md
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(".")
WORK = ROOT / "01_data/processed/provisional_classification_work"

with open(WORK / "classification_progress.json") as f:
    prog = json.load(f)

with open(WORK / "reviews_classified_checkpoint.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))

with open(WORK / "incidents_classified_checkpoint.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

REVIEW_COLS = list(reviews[0].keys())
INCIDENT_COLS = list(incidents[0].keys())

with open(ROOT / "01_data/processed/reviews_classified_24m_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=REVIEW_COLS)
    w.writeheader()
    w.writerows(reviews)

with open(ROOT / "01_data/processed/review_incidents_24m_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=INCIDENT_COLS)
    w.writeheader()
    w.writerows(incidents)

queue_cols = [
    "source", "review_id", "review_date", "rating",
    "primary_pain_point_family", "primary_journey", "max_severity",
    "classification_confidence", "incident_count", "reason_flagged",
]
queue_rows = []
for r in reviews:
    if r["needs_human_review"] == "True":
        reasons = []
        if r["incident_present"] == "True":
            ic = int(r["incident_count"])
            if ic >= 2:
                reasons.append(f"multi_incident({ic})")
        if r["classification_confidence"] == "LOW":
            reasons.append("low_confidence")
        if r["complaint_present"] == "UNCLEAR" or r["product_related"] == "UNCLEAR":
            reasons.append("unclear_signal")
        if r["primary_pain_point_family"] in ("UNCLEAR", "OTHER", ""):
            reasons.append("ambiguous_family")
        if r["sentiment"] == "UNCLEAR":
            reasons.append("unclear_sentiment")
        new_themes = [i for i in incidents
                      if i["review_id"] == r["review_id"] and i["new_theme_flag"] == "True"]
        if new_themes:
            reasons.append(f"new_theme({len(new_themes)})")
        queue_rows.append({
            "source": r["source"],
            "review_id": r["review_id"],
            "review_date": r["review_date"],
            "rating": r["rating"],
            "primary_pain_point_family": r["primary_pain_point_family"],
            "primary_journey": r["primary_journey"],
            "max_severity": r["max_severity"],
            "classification_confidence": r["classification_confidence"],
            "incident_count": r["incident_count"],
            "reason_flagged": ";".join(reasons) if reasons else "general_review",
        })

queue_rows.sort(key=lambda x: (x["review_date"], x["source"], x["review_id"]))

with open(ROOT / "05_outputs/tables/provisional_classification_review_queue.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=queue_cols)
    w.writeheader()
    w.writerows(queue_rows)

family_counts = Counter()
journey_counts = Counter()
severity_counts = Counter()
incident_type_counts = Counter()
sentiment_counts = Counter()
source_counts = Counter()
new_theme_count = 0
low_confidence_count = 0
praise_only_count = 0
multi_incident_review_count = 0
no_incident_count = 0
unclear_family_count = 0

for r in reviews:
    source_counts[r["source"]] += 1
    sentiment_counts[r["sentiment"]] += 1
    if r["incident_present"] == "True":
        family_counts[r["primary_pain_point_family"]] += 1
        journey_counts[r["primary_journey"]] += 1
        severity_counts[r["max_severity"]] += 1
        if int(r["incident_count"]) >= 2:
            multi_incident_review_count += 1
    else:
        no_incident_count += 1
    if r["classification_confidence"] == "LOW":
        low_confidence_count += 1
    if r["primary_pain_point_family"] == "UNCLEAR":
        unclear_family_count += 1
    if (r["incident_present"] == "True" and
        all(i["incident_type"] == "praise" for i in incidents if i["review_id"] == r["review_id"])):
        praise_only_count += 1

for i in incidents:
    incident_type_counts[i["incident_type"]] += 1
    if i["new_theme_flag"] == "True":
        new_theme_count += 1

summary_rows = [
    {"metric": "total_reviews", "value": len(reviews)},
    {"metric": "phase_b_reused_reviews", "value": prog["phase_b_reused_reviews"]},
    {"metric": "new_semantically_classified_reviews", "value": prog["new_semantically_classified_reviews"]},
    {"metric": "total_incidents", "value": len(incidents)},
    {"metric": "reviews_with_incidents", "value": sum(1 for r in reviews if r["incident_present"] == "True")},
    {"metric": "reviews_without_incidents", "value": no_incident_count},
    {"metric": "praise_only_reviews", "value": praise_only_count},
    {"metric": "multi_incident_reviews", "value": multi_incident_review_count},
    {"metric": "needs_human_review_count", "value": len(queue_rows)},
    {"metric": "low_confidence_classifications", "value": low_confidence_count},
    {"metric": "new_theme_flag_incidents", "value": new_theme_count},
    {"metric": "unclear_family_reviews", "value": unclear_family_count},
]
for src, cnt in source_counts.most_common():
    summary_rows.append({"metric": f"source_{src}", "value": cnt})
for sent, cnt in sentiment_counts.most_common():
    summary_rows.append({"metric": f"sentiment_{sent}", "value": cnt})
for fam, cnt in family_counts.most_common():
    summary_rows.append({"metric": f"family_{fam}", "value": cnt})
for jour, cnt in journey_counts.most_common():
    summary_rows.append({"metric": f"journey_{jour}", "value": cnt})
for sev, cnt in severity_counts.most_common():
    summary_rows.append({"metric": f"severity_{sev}", "value": cnt})
for itype, cnt in incident_type_counts.most_common():
    summary_rows.append({"metric": f"incident_type_{itype}", "value": cnt})

with open(ROOT / "05_outputs/tables/provisional_classification_summary.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["metric", "value"])
    w.writeheader()
    w.writerows(summary_rows)

print(f"Wrote reviews: {len(reviews)}")
print(f"Wrote incidents: {len(incidents)}")
print(f"Wrote review queue: {len(queue_rows)}")
print(f"Wrote summary: {len(summary_rows)} metrics")
