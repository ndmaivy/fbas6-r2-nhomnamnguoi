"""Normalize non-canonical family values in provisional outputs."""
import csv
from pathlib import Path

FAMILY_MAP = {
    "LOGIN_AUTHENTICATION": "AUTHENTICATION_IOTP",
    "PORTFOLIO_TRACKING": "PRODUCT_PORTFOLIO_INFORMATION",
    "PORTFOLIO_ACCOUNT_INFORMATION": "PRODUCT_PORTFOLIO_INFORMATION",
    "MARKET_DATA_INFORMATION": "MARKET_DATA_STALENESS_ACCURACY",
    "DOMAIN_OR_OTHER_NEW_THEME": "OTHER",
    "OTHER_NEW_THEME": "OTHER",
    "NONE": "",
}

for path in [
    "01_data/processed/reviews_classified_24m_provisional.csv",
    "01_data/processed/review_incidents_24m_provisional.csv",
    "01_data/processed/provisional_classification_work/reviews_classified_checkpoint.csv",
    "01_data/processed/provisional_classification_work/incidents_classified_checkpoint.csv",
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
