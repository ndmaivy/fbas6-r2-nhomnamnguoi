"""Normalize non-canonical family values in adjudicated outputs."""
import csv
from pathlib import Path

FAMILY_MAP = {
    "MARKET_DATA_STALENESS_ACCURACY": "MARKET_DATA_INFORMATION",
    "MOBILE_TABLET_RESPONSIVENESS": "UX_NAVIGATION_COMPLEXITY",
    "AI_SUPPORT_CONTEXT_QUALITY": "CUSTOMER_SUPPORT",
    "PRODUCT_PORTFOLIO_INFORMATION": "PORTFOLIO_ACCOUNT_INFORMATION",
    "DIGITAL_SIGNATURE_FLOW": "ONBOARDING_KYC",
    "PRODUCT_DISCOVERY_MARKET_DATA": "MARKET_DATA_INFORMATION",
}

for path in [
    "01_data/processed/reviews_classified_24m_provisional_adjudicated.csv",
    "01_data/processed/review_incidents_24m_provisional_adjudicated.csv",
]:
    p = Path(path)
    with open(p, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        continue
    changed = 0
    field = "primary_pain_point_family" if "reviews" in path else "pain_point_family"
    for r in rows:
        old = r.get(field, "")
        if old in FAMILY_MAP:
            r[field] = FAMILY_MAP[old]
            changed += 1
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{path}: {changed} rows normalized")
