"""Phase G — Provisional Measurement.

Generates all measurement tables from adjudicated provisional outputs.
All results are PROVISIONAL / EXPLORATORY.
"""
import csv
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(".")
TABLES = ROOT / "05_outputs/tables"
CHARTS = ROOT / "05_outputs/charts"
CHARTS.mkdir(parents=True, exist_ok=True)

with open(ROOT / "01_data/processed/reviews_classified_24m_provisional_adjudicated.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))
with open(ROOT / "01_data/processed/review_incidents_24m_provisional_adjudicated.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

N_REVIEWS = len(reviews)
N_INCIDENTS = len(incidents)
N_GP = sum(1 for r in reviews if r["source"] == "Google Play")
N_AS = sum(1 for r in reviews if r["source"] == "App Store")
N_COMPLAINT = sum(1 for r in reviews if r["complaint_present"] == "True")

CANONICAL_FAMILIES = [
    "PERFORMANCE_RELIABILITY", "UX_NAVIGATION_COMPLEXITY", "ONBOARDING_KYC",
    "AUTHENTICATION_IOTP", "TRADING_ORDER_EXECUTION", "DEPOSIT_WITHDRAWAL_TRANSFER",
    "CUSTOMER_SUPPORT", "MARKET_DATA_INFORMATION", "PORTFOLIO_ACCOUNT_INFORMATION",
    "FEE_PRICING", "ACCOUNT_RECOVERY_PROFILE_CHANGE", "SECURITY_ACCOUNT_PROTECTION",
    "NOTIFICATION_COMMUNICATION", "MARKET_RESEARCH_RECOMMENDATION_UTILITY",
    "EXCESSIVE_DATA_CONSUMPTION",
]

def pct(num, denom):
    return round(100.0 * num / denom, 2) if denom else 0.0

# ============================================================
# 3. PAIN-POINT FREQUENCY
# ============================================================
family_incidents = defaultdict(list)
family_reviews = defaultdict(set)
for inc in incidents:
    fam = inc["pain_point_family"]
    if fam in CANONICAL_FAMILIES:
        family_incidents[fam].append(inc)
        family_reviews[fam].add(inc["review_id"])

freq_rows = []
for fam in CANONICAL_FAMILIES:
    incs = family_incidents[fam]
    rids = family_reviews[fam]
    gp_rids = set(i["review_id"] for i in incs if i["source"] == "Google Play")
    as_rids = set(i["review_id"] for i in incs if i["source"] == "App Store")
    freq_rows.append({
        "pain_point_family": fam,
        "incident_count": len(incs),
        "unique_review_count": len(rids),
        "pct_all_reviews": pct(len(rids), N_REVIEWS),
        "pct_complaint_reviews": pct(len(rids), N_COMPLAINT),
        "google_play_review_count": len(gp_rids),
        "app_store_review_count": len(as_rids),
        "google_play_share": pct(len(gp_rids), len(rids)) if rids else 0.0,
        "app_store_share": pct(len(as_rids), len(rids)) if rids else 0.0,
    })

with open(TABLES / "pain_point_frequency_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(freq_rows[0].keys()))
    w.writeheader()
    w.writerows(freq_rows)

# ============================================================
# 4. SEVERITY
# ============================================================
sev_rows = []
for fam in CANONICAL_FAMILIES:
    incs = family_incidents[fam]
    sev_counts = Counter(i["severity"] for i in incs)
    total = len(incs)
    high = sev_counts.get("HIGH", 0)
    med = sev_counts.get("MEDIUM", 0)
    low = sev_counts.get("LOW", 0)
    none = sev_counts.get("NONE", 0)
    sev_rows.append({
        "pain_point_family": fam,
        "incident_count": total,
        "low_count": low,
        "medium_count": med,
        "high_count": high,
        "none_count": none,
        "pct_high": pct(high, total),
        "pct_medium_high": pct(med + high, total),
    })

with open(TABLES / "pain_point_severity_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(sev_rows[0].keys()))
    w.writeheader()
    w.writerows(sev_rows)

# ============================================================
# 5. RATING
# ============================================================
review_by_id = {r["review_id"]: r for r in reviews}
rating_rows = []
for fam in CANONICAL_FAMILIES:
    rids = family_reviews[fam]
    fam_reviews = [review_by_id[rid] for rid in rids]
    ratings = [int(r["rating"]) for r in fam_reviews if r["rating"]]
    if not ratings:
        continue
    one_star = sum(1 for x in ratings if x == 1)
    one_two = sum(1 for x in ratings if x <= 2)
    four_five = sum(1 for x in ratings if x >= 4)
    rating_rows.append({
        "pain_point_family": fam,
        "review_count": len(ratings),
        "avg_rating": round(statistics.mean(ratings), 2),
        "median_rating": statistics.median(ratings),
        "one_star_count": one_star,
        "one_star_share": pct(one_star, len(ratings)),
        "one_two_star_count": one_two,
        "one_two_star_share": pct(one_two, len(ratings)),
        "four_five_star_count": four_five,
        "four_five_star_share": pct(four_five, len(ratings)),
    })

with open(TABLES / "pain_point_rating_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rating_rows[0].keys()))
    w.writeheader()
    w.writerows(rating_rows)

# ============================================================
# 6. SENTIMENT
# ============================================================
sent_rows = []
for fam in CANONICAL_FAMILIES:
    rids = family_reviews[fam]
    fam_reviews = [review_by_id[rid] for rid in rids]
    sent_counts = Counter(r["sentiment"] for r in fam_reviews)
    sent_rows.append({
        "pain_point_family": fam,
        "review_count": len(fam_reviews),
        "negative_count": sent_counts.get("NEGATIVE", 0),
        "mixed_count": sent_counts.get("MIXED", 0),
        "neutral_count": sent_counts.get("NEUTRAL", 0),
        "positive_count": sent_counts.get("POSITIVE", 0),
        "unclear_count": sent_counts.get("UNCLEAR", 0),
    })

with open(TABLES / "pain_point_sentiment_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(sent_rows[0].keys()))
    w.writeheader()
    w.writerows(sent_rows)

# ============================================================
# 7. JOURNEY ANALYSIS
# ============================================================
journey_incidents = defaultdict(list)
journey_reviews = defaultdict(set)
journey_families = defaultdict(set)
for inc in incidents:
    j = inc["journey"]
    if j:
        journey_incidents[j].append(inc)
        journey_reviews[j].add(inc["review_id"])
        if inc["pain_point_family"] in CANONICAL_FAMILIES:
            journey_families[j].add(inc["pain_point_family"])

journey_rows = []
for j in sorted(journey_incidents.keys()):
    incs = journey_incidents[j]
    rids = journey_reviews[j]
    high = sum(1 for i in incs if i["severity"] == "HIGH")
    gp = sum(1 for i in incs if i["source"] == "Google Play")
    asp = sum(1 for i in incs if i["source"] == "App Store")
    journey_rows.append({
        "journey": j,
        "unique_review_count": len(rids),
        "incident_count": len(incs),
        "high_severity_count": high,
        "pain_point_families_represented": len(journey_families[j]),
        "google_play_incident_count": gp,
        "app_store_incident_count": asp,
    })

with open(TABLES / "journey_pain_point_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(journey_rows[0].keys()))
    w.writeheader()
    w.writerows(journey_rows)

# Pain-point × journey matrix
matrix = defaultdict(lambda: defaultdict(int))
for inc in incidents:
    fam = inc["pain_point_family"]
    j = inc["journey"]
    if fam in CANONICAL_FAMILIES and j:
        matrix[fam][j] += 1

all_journeys = sorted(set(j for fam in matrix for j in matrix[fam]))
matrix_rows = []
for fam in CANONICAL_FAMILIES:
    row = {"pain_point_family": fam}
    for j in all_journeys:
        row[j] = matrix[fam].get(j, 0)
    row["total"] = sum(matrix[fam].values())
    matrix_rows.append(row)

with open(TABLES / "pain_point_journey_matrix_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
    w.writeheader()
    w.writerows(matrix_rows)

# ============================================================
# 8. SOURCE COMPARISON
# ============================================================
source_rows = []
for fam in CANONICAL_FAMILIES:
    incs = family_incidents[fam]
    rids = family_reviews[fam]
    gp_rids = set(i["review_id"] for i in incs if i["source"] == "Google Play")
    as_rids = set(i["review_id"] for i in incs if i["source"] == "App Store")
    gp_rate = pct(len(gp_rids), N_GP)
    as_rate = pct(len(as_rids), N_AS)
    source_rows.append({
        "pain_point_family": fam,
        "google_play_review_count": len(gp_rids),
        "app_store_review_count": len(as_rids),
        "google_play_within_source_rate": gp_rate,
        "app_store_within_source_rate": as_rate,
        "difference_pp": round(gp_rate - as_rate, 2),
    })

with open(TABLES / "pain_point_source_comparison_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(source_rows[0].keys()))
    w.writeheader()
    w.writerows(source_rows)

# ============================================================
# 9. TREND (monthly)
# ============================================================
def month_key(date_str):
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m")
    except Exception:
        return None

monthly_all = Counter()
monthly_family = defaultdict(lambda: defaultdict(set))
for r in reviews:
    mk = month_key(r["review_date"])
    if mk:
        monthly_all[mk] += 1
        for inc in incidents:
            if inc["review_id"] == r["review_id"] and inc["pain_point_family"] in CANONICAL_FAMILIES:
                monthly_family[mk][inc["pain_point_family"]].add(r["review_id"])

trend_rows = []
for mk in sorted(monthly_all.keys()):
    total = monthly_all[mk]
    for fam in CANONICAL_FAMILIES:
        rids = monthly_family[mk].get(fam, set())
        gp_rids = set()
        as_rids = set()
        for rid in rids:
            r = review_by_id.get(rid)
            if r:
                if r["source"] == "Google Play":
                    gp_rids.add(rid)
                else:
                    as_rids.add(rid)
        trend_rows.append({
            "month": mk,
            "pain_point_family": fam,
            "pain_point_review_count": len(rids),
            "all_reviews_in_month": total,
            "pain_point_review_rate": pct(len(rids), total),
            "google_play_count": len(gp_rids),
            "app_store_count": len(as_rids),
        })

with open(TABLES / "pain_point_monthly_trend_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(trend_rows[0].keys()))
    w.writeheader()
    w.writerows(trend_rows)

# ============================================================
# 10. REPRESENTATIVE EVIDENCE
# ============================================================
def select_representative(fam, max_n=3):
    incs = family_incidents[fam]
    high_conf = [i for i in incs if i["confidence"] == "HIGH"]
    candidates = high_conf if len(high_conf) >= max_n else incs
    candidates = sorted(candidates, key=lambda x: (
        -(1 if x["source"] == "Google Play" else 0),
        review_by_id.get(x["review_id"], {}).get("review_date", "")
    ))
    selected = []
    sources_used = set()
    for inc in candidates:
        if len(selected) >= max_n:
            break
        if inc["source"] not in sources_used or len(selected) < 2:
            selected.append(inc)
            sources_used.add(inc["source"])
    return selected[:max_n]

rep_rows = []
for fam in CANONICAL_FAMILIES:
    selected = select_representative(fam, 3)
    for inc in selected:
        r = review_by_id.get(inc["review_id"], {})
        rep_rows.append({
            "pain_point_family": fam,
            "source": inc["source"],
            "review_id": inc["review_id"],
            "review_date": r.get("review_date", ""),
            "rating": r.get("rating", ""),
            "journey": inc["journey"],
            "severity": inc["severity"],
            "evidence_span": inc["evidence_span"],
            "selection_reason": "HIGH confidence; source/date diversity" if inc["confidence"] == "HIGH" else "MEDIUM confidence; source/date diversity",
        })

with open(TABLES / "pain_point_representative_evidence_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rep_rows[0].keys()))
    w.writeheader()
    w.writerows(rep_rows)

# ============================================================
# 11. NEW THEMES
# ============================================================
new_theme_rows = []
new_theme_incidents = [i for i in incidents if i.get("new_theme_flag") == "True"]
new_theme_by_subtype = defaultdict(list)
for inc in new_theme_incidents:
    sub = inc.get("pain_point_subtype", "")
    if sub:
        new_theme_by_subtype[sub].append(inc)

for sub, incs in new_theme_by_subtype.items():
    rids = set(i["review_id"] for i in incs)
    new_theme_rows.append({
        "new_theme_subtype": sub,
        "incident_count": len(incs),
        "review_count": len(rids),
        "evidence_examples": " | ".join(i["evidence_span"][:80] for i in incs[:2]),
        "recurring_theme_consideration": "YES — multiple incidents" if len(incs) > 1 else "NO — single isolated case",
    })

with open(TABLES / "new_theme_summary_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(new_theme_rows[0].keys()))
    w.writeheader()
    w.writerows(new_theme_rows)

# ============================================================
# 12. MASTER SUMMARY
# ============================================================
# Trend direction: compare first half vs second half of time window
sorted_months = sorted(monthly_all.keys())
mid = len(sorted_months) // 2
first_half = set(sorted_months[:mid])
second_half = set(sorted_months[mid:])

def trend_direction(fam):
    first_count = sum(len(monthly_family[m].get(fam, set())) for m in first_half)
    second_count = sum(len(monthly_family[m].get(fam, set())) for m in second_half)
    total = first_count + second_count
    if total < 5:
        return "INSUFFICIENT_DATA"
    if second_count > first_count * 1.5:
        return "INCREASING"
    if second_count < first_count * 0.5:
        return "DECREASING"
    return "STABLE"

# Latest 6 months
latest_6m = sorted_months[-6:] if len(sorted_months) >= 6 else sorted_months

master_rows = []
for fam in CANONICAL_FAMILIES:
    incs = family_incidents[fam]
    rids = family_reviews[fam]
    fam_reviews = [review_by_id[rid] for rid in rids]
    ratings = [int(r["rating"]) for r in fam_reviews if r["rating"]]
    high = sum(1 for i in incs if i["severity"] == "HIGH")
    med = sum(1 for i in incs if i["severity"] == "MEDIUM")
    one_two = sum(1 for x in ratings if x <= 2)
    latest_6m_count = sum(len(monthly_family[m].get(fam, set())) for m in latest_6m)
    # Representative journey (most common)
    journey_counts = Counter(i["journey"] for i in incs)
    rep_journey = journey_counts.most_common(1)[0][0] if journey_counts else ""
    # Evidence confidence note
    conf_counts = Counter(i["confidence"] for i in incs)
    high_conf = conf_counts.get("HIGH", 0)
    conf_note = f"{high_conf}/{len(incs)} HIGH confidence"
    master_rows.append({
        "pain_point_family": fam,
        "review_count": len(rids),
        "incident_count": len(incs),
        "pct_all_reviews": pct(len(rids), N_REVIEWS),
        "pct_complaint_reviews": pct(len(rids), N_COMPLAINT),
        "high_severity_count": high,
        "high_severity_share": pct(high, len(incs)) if incs else 0.0,
        "median_rating": statistics.median(ratings) if ratings else "",
        "one_two_star_share": pct(one_two, len(ratings)) if ratings else 0.0,
        "google_play_count": len(set(i["review_id"] for i in incs if i["source"] == "Google Play")),
        "app_store_count": len(set(i["review_id"] for i in incs if i["source"] == "App Store")),
        "latest_6m_review_count": latest_6m_count,
        "trend_direction": trend_direction(fam),
        "representative_journey": rep_journey,
        "evidence_confidence_note": conf_note,
    })

with open(TABLES / "pain_point_summary_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(master_rows[0].keys()))
    w.writeheader()
    w.writerows(master_rows)

# ============================================================
# 14. PRIORITIZATION INPUTS
# ============================================================
prio_rows = []
for fam in CANONICAL_FAMILIES:
    incs = family_incidents[fam]
    rids = family_reviews[fam]
    fam_reviews = [review_by_id[rid] for rid in rids]
    ratings = [int(r["rating"]) for r in fam_reviews if r["rating"]]
    high = sum(1 for i in incs if i["severity"] == "HIGH")
    med = sum(1 for i in incs if i["severity"] == "MEDIUM")
    one_two = sum(1 for x in ratings if x <= 2)
    sources = set(i["source"] for i in incs)
    conf_counts = Counter(i["confidence"] for i in incs)
    high_conf_share = pct(conf_counts.get("HIGH", 0), len(incs)) if incs else 0.0
    td = trend_direction(fam)
    # Journey criticality: TRADING/FUNDING/LOGIN = high; others = medium/low
    journey_crit = {"TRADING_ORDER_MANAGEMENT": "HIGH", "FUNDING_CASH_TRANSFER": "HIGH", "LOGIN_AUTHENTICATION": "HIGH"}.get(
        Counter(i["journey"] for i in incs).most_common(1)[0][0] if incs else "", "MEDIUM"
    )
    prio_rows.append({
        "pain_point_family": fam,
        "frequency": len(rids),
        "severity_high_count": high,
        "severity_medium_count": med,
        "journey_criticality": journey_crit,
        "rating_association_one_two_star_share": pct(one_two, len(ratings)) if ratings else 0.0,
        "trend_signal": td,
        "evidence_confidence_high_share": high_conf_share,
        "source_coverage": "BOTH" if len(sources) == 2 else list(sources)[0] if sources else "NONE",
    })

with open(TABLES / "pain_point_prioritization_inputs_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(prio_rows[0].keys()))
    w.writeheader()
    w.writerows(prio_rows)

print("All measurement tables generated.")
print(f"Denominators: N_REVIEWS={N_REVIEWS}, N_INCIDENTS={N_INCIDENTS}, N_GP={N_GP}, N_AS={N_AS}, N_COMPLAINT={N_COMPLAINT}")
print(f"Families measured: {len(CANONICAL_FAMILIES)}")
print(f"Trend months: {len(sorted_months)}")
