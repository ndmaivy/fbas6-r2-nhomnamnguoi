"""Phase H — Provisional Pain-Point Prioritization.

Builds prioritization matrix, selects STRONG_CANDIDATE set,
creates problem cards and M4/M5 handoff.
"""
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(".")
TABLES = ROOT / "05_outputs/tables"

with open(ROOT / "01_data/processed/reviews_classified_24m_provisional_adjudicated.csv", encoding="utf-8-sig") as f:
    reviews = list(csv.DictReader(f))
with open(ROOT / "01_data/processed/review_incidents_24m_provisional_adjudicated.csv", encoding="utf-8-sig") as f:
    incidents = list(csv.DictReader(f))

with open(TABLES / "pain_point_frequency_provisional.csv", encoding="utf-8-sig") as f:
    freq = list(csv.DictReader(f))
with open(TABLES / "pain_point_severity_provisional.csv", encoding="utf-8-sig") as f:
    sev = list(csv.DictReader(f))
with open(TABLES / "pain_point_rating_provisional.csv", encoding="utf-8-sig") as f:
    rating = list(csv.DictReader(f))
with open(TABLES / "pain_point_source_comparison_provisional.csv", encoding="utf-8-sig") as f:
    source = list(csv.DictReader(f))
with open(TABLES / "pain_point_summary_provisional.csv", encoding="utf-8-sig") as f:
    summary = list(csv.DictReader(f))
with open(TABLES / "pain_point_representative_evidence_provisional.csv", encoding="utf-8-sig") as f:
    rep = list(csv.DictReader(f))

CANONICAL_FAMILIES = [
    "PERFORMANCE_RELIABILITY", "UX_NAVIGATION_COMPLEXITY", "ONBOARDING_KYC",
    "AUTHENTICATION_IOTP", "TRADING_ORDER_EXECUTION", "DEPOSIT_WITHDRAWAL_TRANSFER",
    "CUSTOMER_SUPPORT", "MARKET_DATA_INFORMATION", "PORTFOLIO_ACCOUNT_INFORMATION",
    "FEE_PRICING", "ACCOUNT_RECOVERY_PROFILE_CHANGE", "SECURITY_ACCOUNT_PROTECTION",
    "NOTIFICATION_COMMUNICATION", "MARKET_RESEARCH_RECOMMENDATION_UTILITY",
    "EXCESSIVE_DATA_CONSUMPTION",
]

JOURNEY_CRITICALITY = {
    "TRADING_ORDER_MANAGEMENT": "HIGH",
    "FUNDING_CASH_TRANSFER": "HIGH",
    "LOGIN_AUTHENTICATION": "HIGH",
    "ACCOUNT_OPENING_KYC": "MEDIUM",
    "ACCOUNT_PROFILE_MAINTENANCE": "MEDIUM",
    "PORTFOLIO_TRACKING": "MEDIUM",
    "PRODUCT_DISCOVERY_MARKET_DATA": "LOW",
    "CUSTOMER_SUPPORT": "MEDIUM",
    "GENERAL_CROSS_JOURNEY": "MEDIUM",
    "OTHER": "LOW",
    "UNKNOWN": "INSUFFICIENT",
}

def evidence_level(value, thresholds):
    for level, (lo, hi) in thresholds.items():
        if lo <= value <= hi:
            return level
    return "INSUFFICIENT"

# ============================================================
# 8. PRIORITIZATION MATRIX
# ============================================================
matrix_rows = []
for s in summary:
    fam = s["pain_point_family"]
    rc = int(s["review_count"])
    ic = int(s["incident_count"])
    high = int(s["high_severity_count"])
    high_share = float(s["high_severity_share"])
    med_rating = float(s["median_rating"]) if s["median_rating"] else 0
    one_two = float(s["one_two_star_share"])
    trend = s["trend_direction"]
    rep_journey = s["representative_journey"]
    jc = JOURNEY_CRITICALITY.get(rep_journey, "LOW")

    # Frequency evidence
    if rc >= 100:
        freq_ev = "HIGH"
    elif rc >= 30:
        freq_ev = "MEDIUM"
    elif rc >= 10:
        freq_ev = "LOW"
    else:
        freq_ev = "INSUFFICIENT"

    # Severity evidence
    if high_share >= 50:
        sev_ev = "HIGH"
    elif high_share >= 25:
        sev_ev = "MEDIUM"
    else:
        sev_ev = "LOW"

    # Rating evidence
    if one_two >= 90:
        rat_ev = "HIGH"
    elif one_two >= 70:
        rat_ev = "MEDIUM"
    else:
        rat_ev = "LOW"

    # Trend evidence
    if trend in ("INCREASING", "DECREASING"):
        trend_ev = "MEDIUM"
    elif trend == "STABLE":
        trend_ev = "LOW"
    elif trend == "VOLATILE":
        trend_ev = "MEDIUM"
    else:
        trend_ev = "INSUFFICIENT"

    # Source coverage
    gp = int(s["google_play_count"])
    asp = int(s["app_store_count"])
    if gp > 0 and asp > 0:
        src_cov = "BOTH"
    elif gp > 0:
        src_cov = "GOOGLE_PLAY_ONLY"
    else:
        src_cov = "APP_STORE_ONLY"

    # Evidence confidence
    conf_note = s["evidence_confidence_note"]
    high_conf_count = int(conf_note.split("/")[0]) if "/" in conf_note else 0
    if rc >= 30 and high_conf_count / ic >= 0.7 if ic else False:
        ev_conf = "HIGH"
    elif rc >= 10:
        ev_conf = "MEDIUM"
    else:
        ev_conf = "LOW"

    # Prioritization rationale
    strong_signals = sum([freq_ev == "HIGH", sev_ev == "HIGH", jc == "HIGH", rat_ev == "HIGH"])
    medium_signals = sum([freq_ev == "MEDIUM", sev_ev == "MEDIUM", jc == "MEDIUM", rat_ev == "MEDIUM"])

    if strong_signals >= 2 and ev_conf in ("HIGH", "MEDIUM") and src_cov == "BOTH":
        priority = "STRONG_CANDIDATE"
        rationale = f"Strong signals: {strong_signals} HIGH dimensions; evidence confidence {ev_conf}; both platforms represented."
    elif (strong_signals >= 1 or medium_signals >= 3) and ev_conf != "INSUFFICIENT":
        priority = "SECONDARY_CANDIDATE"
        rationale = f"Moderate signals: {strong_signals} HIGH + {medium_signals} MEDIUM dimensions; evidence confidence {ev_conf}."
    elif rc >= 5:
        priority = "MONITOR"
        rationale = f"Low evidence: {rc} reviews; monitor for recurrence."
    else:
        priority = "INSUFFICIENT_EVIDENCE"
        rationale = f"Sparse data: {rc} reviews; insufficient for prioritization."

    matrix_rows.append({
        "pain_point_family": fam,
        "review_count": rc,
        "pct_all_reviews": s["pct_all_reviews"],
        "incident_count": ic,
        "frequency_evidence": freq_ev,
        "high_severity_count": high,
        "high_severity_share": s["high_severity_share"],
        "severity_evidence": sev_ev,
        "primary_journey": rep_journey,
        "journey_criticality": jc,
        "median_rating": s["median_rating"],
        "one_two_star_share": s["one_two_star_share"],
        "rating_evidence": rat_ev,
        "trend_direction": trend,
        "trend_evidence": trend_ev,
        "source_coverage": src_cov,
        "evidence_confidence": ev_conf,
        "prioritization_rationale": rationale,
        "priority_candidate": priority,
    })

with open(TABLES / "pain_point_prioritization_matrix_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
    w.writeheader()
    w.writerows(matrix_rows)

# ============================================================
# 9. STRONG CANDIDATE SET
# ============================================================
strong = [r for r in matrix_rows if r["priority_candidate"] == "STRONG_CANDIDATE"]
strong.sort(key=lambda x: (
    -int(x["review_count"]),
    -float(x["high_severity_share"]),
    -({"HIGH": 3, "MEDIUM": 2, "LOW": 1, "INSUFFICIENT": 0}[x["journey_criticality"]]),
))

# Select up to 5
selected = strong[:5]

# ============================================================
# 10. PROBLEM CARDS
# ============================================================
review_by_id = {r["review_id"]: r for r in reviews}
rep_by_family = defaultdict(list)
for r in rep:
    rep_by_family[r["pain_point_family"]].append(r)

PROBLEM_STATEMENTS = {
    "PERFORMANCE_RELIABILITY": "Public reviewers repeatedly report app lag, freezing, and crashes during general use, which is associated with inability to complete tasks and visible frustration across multiple journeys.",
    "UX_NAVIGATION_COMPLEXITY": "Public reviewers repeatedly report difficulty navigating the app due to cluttered layout, unintuitive controls, and excessive steps, which is associated with task abandonment and requests to revert to older versions.",
    "TRADING_ORDER_EXECUTION": "Public reviewers repeatedly report inability to place, modify, or cancel stock orders, which is associated with missed trading opportunities and explicit financial-loss claims.",
    "DEPOSIT_WITHDRAWAL_TRANSFER": "Public reviewers repeatedly report delays or failures in depositing, withdrawing, or transferring funds, which is associated with inability to access money and high-severity financial impact.",
    "AUTHENTICATION_IOTP": "Public reviewers repeatedly report login failures, missing iOTP, and biometric authentication issues, which is associated with inability to access the account and downstream task blockage.",
    "CUSTOMER_SUPPORT": "Public reviewers repeatedly report inability to reach human support, AI/bot frustration, and unresolved issues, which is associated with prolonged problem duration and escalation to public complaints.",
}

JOURNEY_EXPLANATION = {
    "TRADING_ORDER_MANAGEMENT": "Transaction-critical: inability to trade directly causes financial impact.",
    "FUNDING_CASH_TRANSFER": "Transaction-critical: inability to move money directly causes financial impact.",
    "LOGIN_AUTHENTICATION": "Access-critical: blocks all downstream tasks.",
    "GENERAL_CROSS_JOURNEY": "Cross-app: affects multiple journeys simultaneously.",
    "ACCOUNT_OPENING_KYC": "Onboarding-critical: blocks new customer acquisition.",
    "ACCOUNT_PROFILE_MAINTENANCE": "Maintenance-critical: blocks account updates and recovery.",
    "PORTFOLIO_TRACKING": "Information-critical: affects ability to monitor own holdings.",
    "PRODUCT_DISCOVERY_MARKET_DATA": "Discovery-critical: affects research and monitoring of market data.",
    "CUSTOMER_SUPPORT": "Service-critical: affects ability to resolve issues.",
}

ROOT_CAUSE_HYPOTHESES = {
    "PERFORMANCE_RELIABILITY": [
        "Backend latency or capacity issues during peak market hours",
        "Client-side rendering or memory issues on mobile devices",
        "Network synchronization failures between client and server",
        "Insufficient error handling leading to app freeze on edge cases",
    ],
    "UX_NAVIGATION_COMPLEXITY": [
        "Feature accumulation without consolidation or simplification",
        "Inconsistent navigation patterns across app sections",
        "Missing user research or usability testing in design process",
        "Legacy UI patterns not updated for mobile-first usage",
    ],
    "TRADING_ORDER_EXECUTION": [
        "Order-state synchronization delays between client and exchange",
        "Backend order-matching engine latency",
        "Authentication dependency causing order placement failures",
        "Missing or delayed order status feedback to user",
    ],
    "DEPOSIT_WITHDRAWAL_TRANSFER": [
        "Bank-linking validation failures or delays",
        "Settlement process delays (T+2 or similar)",
        "Fund-availability calculation errors",
        "Compliance/verification steps causing unexpected blocks",
    ],
    "AUTHENTICATION_IOTP": [
        "iOTP delivery infrastructure issues (SMS/email gateway)",
        "Biometric authentication compatibility across devices",
        "Session management or token expiration issues",
        "Device authorization flow complexity",
    ],
    "CUSTOMER_SUPPORT": [
        "Insufficient human support staffing",
        "AI/bot system lacking context or escalation logic",
        "Support process not integrated with product issue tracking",
        "Communication channel fragmentation (phone, chat, email, in-app)",
    ],
}

VALIDATION_NEEDED = {
    "PERFORMANCE_RELIABILITY": "M4: reproduce app freeze/lag on representative devices and network conditions; measure latency at key API endpoints. M5: assess impact on trading volume and customer retention.",
    "UX_NAVIGATION_COMPLEXITY": "M4: conduct usability testing with representative users; map current navigation flows. M5: assess impact on task completion rate and support ticket volume.",
    "TRADING_ORDER_EXECUTION": "M4: reproduce order placement/cancellation failures; audit order-state synchronization. M5: assess financial impact of failed orders and customer compensation history.",
    "DEPOSIT_WITHDRAWAL_TRANSFER": "M4: trace deposit/withdrawal flow end-to-end; identify failure points. M5: assess financial impact and regulatory/compliance constraints.",
    "AUTHENTICATION_IOTP": "M4: reproduce login failures across devices; audit iOTP delivery infrastructure. M5: assess impact on customer acquisition and retention.",
    "CUSTOMER_SUPPORT": "M4: audit support response times and resolution rates; identify AI/bot limitations. M5: assess support cost and customer satisfaction impact.",
}

problem_cards = []
for i, cand in enumerate(selected, 1):
    fam = cand["pain_point_family"]
    rep_quotes = rep_by_family.get(fam, [])
    quotes = [r["evidence_span"] for r in rep_quotes[:3]]
    while len(quotes) < 3:
        quotes.append("")
    problem_cards.append({
        "candidate_id": f"CAND-{i:02d}",
        "pain_point_family": fam,
        "candidate_problem_statement": PROBLEM_STATEMENTS.get(fam, ""),
        "affected_journey": cand["primary_journey"],
        "observed_customer_experience": f"Reviewers describe {fam.replace('_', ' ').lower()} issues with clear evidence spans; {cand['review_count']} unique reviews in the analyzed sample.",
        "review_count": cand["review_count"],
        "pct_all_reviews": cand["pct_all_reviews"],
        "pct_complaint_reviews": summary[CANONICAL_FAMILIES.index(fam)]["pct_complaint_reviews"],
        "incident_count": cand["incident_count"],
        "high_severity_share": cand["high_severity_share"],
        "median_rating": cand["median_rating"],
        "one_two_star_share": cand["one_two_star_share"],
        "trend_signal": cand["trend_direction"],
        "google_play_evidence": int(summary[CANONICAL_FAMILIES.index(fam)]["google_play_count"]),
        "app_store_evidence": int(summary[CANONICAL_FAMILIES.index(fam)]["app_store_count"]),
        "representative_quote_1": quotes[0],
        "representative_quote_2": quotes[1],
        "representative_quote_3": quotes[2],
        "evidence_strength": cand["evidence_confidence"],
        "interpretation": f"This family shows {cand['frequency_evidence']} frequency, {cand['severity_evidence']} severity, and {cand['journey_criticality']} journey criticality. It is a strong candidate for deeper validation.",
        "root_cause_hypotheses": " | ".join(ROOT_CAUSE_HYPOTHESES.get(fam, [])),
        "limitations": "Public reviewers are self-selected; classification is PROVISIONAL; single-coder; taxonomy not frozen.",
        "validation_needed": VALIDATION_NEEDED.get(fam, ""),
    })

with open(TABLES / "candidate_problem_cards_provisional.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(problem_cards[0].keys()))
    w.writeheader()
    w.writerows(problem_cards)

# ============================================================
# 14. M4/M5 HANDOFF
# ============================================================
handoff_rows = []
for card in problem_cards:
    fam = card["pain_point_family"]
    handoff_rows.append({
        "pain_point_family": fam,
        "journey": card["affected_journey"],
        "observed_evidence": f"{card['review_count']} reviews ({card['pct_all_reviews']}% of analyzed sample); {card['high_severity_share']}% HIGH severity; median rating {card['median_rating']}.",
        "open_question": f"Is {fam.replace('_', ' ').lower()} a real, reproducible product issue affecting TCInvest users?",
        "hypothesis_to_test": " | ".join(ROOT_CAUSE_HYPOTHESES.get(fam, [])),
        "what_M4_should_check": VALIDATION_NEEDED.get(fam, "").split("M5:")[0].replace("M4:", "").strip() if "M4:" in VALIDATION_NEEDED.get(fam, "") else "",
        "what_M5_should_assess": VALIDATION_NEEDED.get(fam, "").split("M5:")[1].strip() if "M5:" in VALIDATION_NEEDED.get(fam, "") else "",
        "validation_priority": "HIGH" if card["evidence_strength"] == "HIGH" else "MEDIUM",
    })

with open(TABLES / "m4_m5_validation_handoff.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(handoff_rows[0].keys()))
    w.writeheader()
    w.writerows(handoff_rows)

print(f"Strong candidates: {len(selected)}")
for c in selected:
    print(f"  {c['pain_point_family']}: {c['review_count']} reviews, {c['high_severity_share']}% HIGH, journey={c['primary_journey']}")
print(f"Problem cards: {len(problem_cards)}")
print(f"Handoff rows: {len(handoff_rows)}")
