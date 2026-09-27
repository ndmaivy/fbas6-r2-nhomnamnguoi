"""Create charts for Phase G provisional measurement."""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

CHARTS = Path("05_outputs/charts")
CHARTS.mkdir(parents=True, exist_ok=True)

with open("05_outputs/tables/pain_point_frequency_provisional.csv", encoding="utf-8-sig") as f:
    freq = list(csv.DictReader(f))
with open("05_outputs/tables/pain_point_severity_provisional.csv", encoding="utf-8-sig") as f:
    sev = list(csv.DictReader(f))
with open("05_outputs/tables/pain_point_journey_matrix_provisional.csv", encoding="utf-8-sig") as f:
    matrix = list(csv.DictReader(f))
with open("05_outputs/tables/pain_point_source_comparison_provisional.csv", encoding="utf-8-sig") as f:
    source = list(csv.DictReader(f))
with open("05_outputs/tables/pain_point_monthly_trend_provisional.csv", encoding="utf-8-sig") as f:
    trend = list(csv.DictReader(f))

WATERMARK = "Provisional / Exploratory Classification\nPublic App-Store Review Sample (N=736)"

# Chart 1: Pain-point frequency
freq_sorted = sorted(freq, key=lambda x: int(x["unique_review_count"]), reverse=True)
fig, ax = plt.subplots(figsize=(10, 6))
families = [r["pain_point_family"].replace("_", "\n") for r in freq_sorted]
counts = [int(r["unique_review_count"]) for r in freq_sorted]
ax.barh(families, counts, color="steelblue")
ax.set_xlabel("Unique Review Count")
ax.set_title("Pain-Point Family Frequency (Unique Reviews)")
ax.invert_yaxis()
fig.text(0.5, 0.02, WATERMARK, ha="center", fontsize=8, style="italic", color="gray")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(CHARTS / "pain_point_review_frequency_provisional.png", dpi=100, bbox_inches="tight")
plt.close()

# Chart 2: Severity distribution
fig, ax = plt.subplots(figsize=(10, 6))
families = [r["pain_point_family"].replace("_", "\n") for r in sev]
high = [int(r["high_count"]) for r in sev]
med = [int(r["medium_count"]) for r in sev]
low = [int(r["low_count"]) for r in sev]
import numpy as np
y = np.arange(len(families))
ax.barh(y, high, color="firebrick", label="HIGH")
ax.barh(y, med, left=high, color="goldenrod", label="MEDIUM")
ax.barh(y, low, left=[h + m for h, m in zip(high, med)], color="lightgreen", label="LOW")
ax.set_yticks(y)
ax.set_yticklabels(families)
ax.set_xlabel("Incident Count")
ax.set_title("Pain-Point Severity Distribution")
ax.legend(loc="lower right")
ax.invert_yaxis()
fig.text(0.5, 0.02, WATERMARK, ha="center", fontsize=8, style="italic", color="gray")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(CHARTS / "pain_point_severity_distribution_provisional.png", dpi=100, bbox_inches="tight")
plt.close()

# Chart 3: Pain-point by journey (stacked)
journeys = [c for c in matrix[0].keys() if c not in ("pain_point_family", "total")]
fig, ax = plt.subplots(figsize=(10, 6))
families = [r["pain_point_family"].replace("_", "\n") for r in matrix]
bottom = [0] * len(families)
colors = plt.cm.tab20.colors[:len(journeys)]
for i, j in enumerate(journeys):
    vals = [int(r[j]) for r in matrix]
    ax.barh(families, vals, left=bottom, color=colors[i], label=j.replace("_", "\n"))
    bottom = [b + v for b, v in zip(bottom, vals)]
ax.set_xlabel("Incident Count")
ax.set_title("Pain-Point Family by Journey Stage")
ax.legend(loc="lower right", fontsize=7, ncol=2)
ax.invert_yaxis()
fig.text(0.5, 0.02, WATERMARK, ha="center", fontsize=8, style="italic", color="gray")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(CHARTS / "pain_point_by_journey_provisional.png", dpi=100, bbox_inches="tight")
plt.close()

# Chart 4: Source comparison
fig, ax = plt.subplots(figsize=(10, 6))
families = [r["pain_point_family"].replace("_", "\n") for r in source]
gp_rate = [float(r["google_play_within_source_rate"]) for r in source]
as_rate = [float(r["app_store_within_source_rate"]) for r in source]
y = np.arange(len(families))
ax.barh(y + 0.2, gp_rate, height=0.4, color="green", label="Google Play (within 403)")
ax.barh(y - 0.2, as_rate, height=0.4, color="purple", label="App Store (within 333)")
ax.set_yticks(y)
ax.set_yticklabels(families)
ax.set_xlabel("Within-Source Rate (%)")
ax.set_title("Pain-Point Family: Source Comparison (Within-Source Rate)")
ax.legend(loc="lower right")
ax.invert_yaxis()
fig.text(0.5, 0.02, WATERMARK, ha="center", fontsize=8, style="italic", color="gray")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(CHARTS / "pain_point_source_comparison_provisional.png", dpi=100, bbox_inches="tight")
plt.close()

# Chart 5: Monthly trend (top 5 families by frequency)
top5 = [r["pain_point_family"] for r in freq_sorted[:5]]
months = sorted(set(r["month"] for r in trend))
fig, ax = plt.subplots(figsize=(12, 6))
for fam in top5:
    rates = []
    for m in months:
        matching = [r for r in trend if r["month"] == m and r["pain_point_family"] == fam]
        rate = float(matching[0]["pain_point_review_rate"]) if matching else 0.0
        rates.append(rate)
    ax.plot(months, rates, marker="o", label=fam.replace("_", "\n"))
ax.set_xlabel("Month")
ax.set_ylabel("Pain-Point Review Rate (% of monthly reviews)")
ax.set_title("Monthly Pain-Point Rate — Top 5 Families")
ax.legend(loc="upper left", fontsize=8)
ax.tick_params(axis="x", rotation=45)
fig.text(0.5, 0.02, WATERMARK, ha="center", fontsize=8, style="italic", color="gray")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(CHARTS / "pain_point_monthly_trend_provisional.png", dpi=100, bbox_inches="tight")
plt.close()

print("All charts created.")
