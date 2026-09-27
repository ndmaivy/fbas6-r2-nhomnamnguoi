#!/usr/bin/env python3
"""Read-only data-quality and temporal-coverage audit for standardized reviews."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
MERGED_PATH = ROOT / "01_data/interim/reviews_merged_standardized.csv"
GP_PATH = ROOT / "01_data/interim/google_play_standardized.csv"
AS_PATH = ROOT / "01_data/interim/app_store_standardized.csv"
RAW_GP_PATH = ROOT / "01_data/raw/google_play/2026-09-22_google_play_raw.csv"
RAW_AS_PATH = ROOT / "01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv"
TABLE_DIR = ROOT / "05_outputs/tables"
CHART_DIR = ROOT / "05_outputs/charts"
REPORT_PATH = ROOT / "04_analysis/validation/data_quality_audit.md"

ANCHOR = pd.Timestamp("2026-09-22T23:59:59.999999999Z")
SOURCES = ["Google Play", "App Store"]
COLORS = {"Google Play": "#4285F4", "App Store": "#0B7A53"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def missing_mask(series: pd.Series) -> pd.Series:
    return series.isna() | series.astype("string").str.strip().eq("").fillna(False)


def fmt_date(value: object) -> str:
    if pd.isna(value):
        return "—"
    return pd.Timestamp(value).isoformat()


def pct(n: int | float, d: int | float) -> float:
    return round(100 * n / d, 2) if d else 0.0


def md_table(frame: pd.DataFrame, max_rows: int | None = None) -> str:
    shown = frame if max_rows is None else frame.head(max_rows)
    if shown.empty:
        return "_None._"
    headers = [str(c) for c in shown.columns]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in shown.itertuples(index=False, name=None):
        vals = []
        for value in row:
            if pd.isna(value):
                text = ""
            elif isinstance(value, float):
                text = f"{value:.2f}"
            else:
                text = str(value)
            vals.append(text.replace("|", "\\|").replace("\n", " "))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def window_stats(df: pd.DataFrame, name: str, start: pd.Timestamp, end: pd.Timestamp) -> dict[str, object]:
    selected = df[df["_date"].between(start, end, inclusive="both")]
    total = len(selected)
    gp = int(selected["source"].eq("Google Play").sum())
    app = int(selected["source"].eq("App Store").sum())
    ratings = selected["_rating"].value_counts().reindex(range(1, 6), fill_value=0)
    low = int(selected["_rating"].isin([1, 2]).sum())
    return {
        "option": name,
        "start_date": start.date().isoformat(),
        "end_date": end.date().isoformat(),
        "total_reviews": total,
        "google_play_reviews": gp,
        "app_store_reviews": app,
        "google_play_share_pct": pct(gp, total),
        "app_store_share_pct": pct(app, total),
        "rating_1": int(ratings[1]),
        "rating_2": int(ratings[2]),
        "rating_3": int(ratings[3]),
        "rating_4": int(ratings[4]),
        "rating_5": int(ratings[5]),
        "average_rating": round(float(selected["_rating"].mean()), 3) if total else np.nan,
        "median_rating": round(float(selected["_rating"].median()), 3) if total else np.nan,
        "low_rating_1_2_count": low,
        "low_rating_1_2_pct": pct(low, total),
        "earliest_actual_review": fmt_date(selected["_date"].min()),
        "latest_actual_review": fmt_date(selected["_date"].max()),
    }


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    protected = [MERGED_PATH, GP_PATH, AS_PATH, RAW_GP_PATH, RAW_AS_PATH]
    before_hashes = {str(p.relative_to(ROOT)): sha256(p) for p in protected}

    merged = pd.read_csv(MERGED_PATH, dtype={"review_id": "string"})
    gp_file = pd.read_csv(GP_PATH, dtype={"review_id": "string"})
    app_file = pd.read_csv(AS_PATH, dtype={"review_id": "string"})
    if len(merged) != 3745 or len(gp_file) != 3223 or len(app_file) != 522:
        raise RuntimeError(
            f"Unexpected row counts: merged={len(merged)}, Google Play={len(gp_file)}, App Store={len(app_file)}"
        )

    df = merged.copy()
    df["_date"] = pd.to_datetime(df["review_date"], utc=True, errors="coerce")
    df["_rating"] = pd.to_numeric(df["rating"], errors="coerce")
    text = df["review_text_raw"].astype("string")
    df["_char_length"] = text.str.len()
    df["_word_length"] = text.str.findall(r"\S+").str.len()
    df["_whitespace_normalized"] = text.str.replace(r"\s+", " ", regex=True).str.strip()

    # Basic quality and rating table.
    key_dupes = int(df.duplicated(["source", "review_id"], keep=False).sum())
    quality_rows: list[dict[str, object]] = []

    def add_quality(metric: str, source: str, count: int, denominator: int, classification: str, note: str = "") -> None:
        quality_rows.append({
            "metric": metric,
            "source": source,
            "count": int(count),
            "denominator": int(denominator),
            "percentage": pct(count, denominator),
            "classification": classification,
            "note": note,
        })

    for source in ["Total"] + SOURCES:
        sub = df if source == "Total" else df[df["source"].eq(source)]
        n = len(sub)
        add_quality("rows", source, n, n, "overview")
        add_quality("unique_review_id", source, sub["review_id"].nunique(dropna=True), n, "overview")
        for column in [
            "review_id", "review_date", "rating", "review_text_raw", "title", "app_version",
            "developer_reply", "collection_country", "collection_language", "collection_locale",
            "storefront", "detected_language",
        ]:
            count = int(missing_mask(sub[column]).sum())
            if column == "title" and source == "Google Play":
                classification = "source-unavailable"
            elif column in {"developer_reply", "storefront"} and source == "Google Play":
                classification = "natural/source-specific missingness"
            elif column in {"developer_reply", "collection_country", "collection_language", "collection_locale"} and source == "App Store":
                classification = "source-unavailable"
            elif column == "detected_language":
                classification = "methodological limitation"
            elif column == "app_version":
                classification = "data-quality limitation"
            else:
                classification = "data-quality issue" if count else "complete"
            add_quality(f"missing_{column}", source, count, n, classification)
        invalid_rating = int((~sub["_rating"].between(1, 5) & sub["_rating"].notna()).sum())
        add_quality("rating_outside_1_5", source, invalid_rating, n, "data-quality issue" if invalid_rating else "valid")

    quality_df = pd.DataFrame(quality_rows)
    quality_df.to_csv(TABLE_DIR / "data_quality_summary.csv", index=False)

    rating_rows = []
    for source in ["Total"] + SOURCES:
        sub = df if source == "Total" else df[df["source"].eq(source)]
        counts = sub["_rating"].value_counts().reindex(range(1, 6), fill_value=0)
        for rating, count in counts.items():
            rating_rows.append({"source": source, "rating": rating, "count": int(count), "percentage": pct(count, len(sub))})
    rating_df = pd.DataFrame(rating_rows)
    rating_df.to_csv(TABLE_DIR / "rating_distribution_by_source.csv", index=False)

    # Text length statistics.
    text_stats = []
    for source in ["Total"] + SOURCES:
        sub = df if source == "Total" else df[df["source"].eq(source)]
        row: dict[str, object] = {"source": source, "records": len(sub)}
        for label, col in [("characters", "_char_length"), ("token_like", "_word_length")]:
            vals = sub[col]
            row.update({
                f"{label}_min": float(vals.min()),
                f"{label}_p25": round(float(vals.quantile(0.25)), 2),
                f"{label}_median": round(float(vals.median()), 2),
                f"{label}_mean": round(float(vals.mean()), 2),
                f"{label}_p75": round(float(vals.quantile(0.75)), 2),
                f"{label}_p90": round(float(vals.quantile(0.90)), 2),
                f"{label}_p95": round(float(vals.quantile(0.95)), 2),
                f"{label}_max": float(vals.max()),
            })
        stripped = sub["review_text_raw"].astype("string").str.strip()
        row["empty_or_missing"] = int(sub["review_text_raw"].isna().sum() + stripped.eq("").fillna(False).sum())
        row["whitespace_only"] = int(sub["review_text_raw"].notna().sum() - stripped.ne("").fillna(False).sum())
        for threshold in [2, 5, 10, 20]:
            row[f"characters_le_{threshold}"] = int(sub["_char_length"].le(threshold).sum())
        text_stats.append(row)
    text_stats_df = pd.DataFrame(text_stats)

    # Duplicate-text audit. Exact strings remain unchanged; normalized text is audit-only.
    dup_rows: list[dict[str, object]] = []
    exact_all = df.groupby("review_text_raw", dropna=False).filter(lambda x: len(x) > 1)
    exact_groups = df.groupby("review_text_raw", dropna=False)
    for content, group in exact_groups:
        if len(group) <= 1 or pd.isna(content):
            continue
        sources = sorted(group["source"].unique())
        dup_rows.append({
            "audit_type": "exact_text_all_sources",
            "source_scope": ", ".join(sources),
            "representative_text": content,
            "normalized_text": re.sub(r"\s+", " ", str(content)).strip(),
            "record_count": len(group),
            "unique_review_ids": group["review_id"].nunique(),
            "source_count": len(sources),
            "review_ids": ";".join(group["review_id"].astype(str)),
        })
    for source in SOURCES:
        sub = df[df["source"].eq(source)]
        for content, group in sub.groupby("review_text_raw", dropna=False):
            if len(group) <= 1 or pd.isna(content):
                continue
            dup_rows.append({
                "audit_type": "exact_text_within_source",
                "source_scope": source,
                "representative_text": content,
                "normalized_text": re.sub(r"\s+", " ", str(content)).strip(),
                "record_count": len(group),
                "unique_review_ids": group["review_id"].nunique(),
                "source_count": 1,
                "review_ids": ";".join(group["review_id"].astype(str)),
            })
    for normalized, group in df.groupby("_whitespace_normalized", dropna=False):
        if len(group) <= 1 or pd.isna(normalized) or group["review_text_raw"].nunique(dropna=False) <= 1:
            continue
        dup_rows.append({
            "audit_type": "whitespace_normalized_only",
            "source_scope": ", ".join(sorted(group["source"].unique())),
            "representative_text": group["review_text_raw"].iloc[0],
            "normalized_text": normalized,
            "record_count": len(group),
            "unique_review_ids": group["review_id"].nunique(),
            "source_count": group["source"].nunique(),
            "review_ids": ";".join(group["review_id"].astype(str)),
        })
    dup_df = pd.DataFrame(dup_rows, columns=[
        "audit_type", "source_scope", "representative_text", "normalized_text", "record_count",
        "unique_review_ids", "source_count", "review_ids",
    ])
    dup_df.to_csv(TABLE_DIR / "duplicate_text_audit.csv", index=False)

    exact_summary = []
    for source in SOURCES:
        sub = df[df["source"].eq(source)]
        sizes = sub.groupby("review_text_raw").size()
        groups = sizes[sizes > 1]
        exact_summary.append({"scope": source, "groups": len(groups), "records_involved": int(groups.sum())})
    all_sizes = df.groupby("review_text_raw").size()
    all_dup_sizes = all_sizes[all_sizes > 1]
    exact_summary.append({"scope": "All sources", "groups": len(all_dup_sizes), "records_involved": int(all_dup_sizes.sum())})
    cross = df.groupby("review_text_raw").agg(records=("review_id", "size"), sources=("source", "nunique"))
    cross = cross[(cross["records"] > 1) & (cross["sources"] > 1)]

    # Version and developer-reply coverage.
    version_rows = []
    top_version_rows = []
    for source in SOURCES:
        sub = df[df["source"].eq(source)]
        available = ~missing_mask(sub["app_version"])
        version_rows.append({
            "source": source, "available": int(available.sum()), "missing": int((~available).sum()),
            "coverage_pct": pct(available.sum(), len(sub)),
        })
        for version, count in sub.loc[available, "app_version"].value_counts().head(10).items():
            version_sub = sub[sub["app_version"].eq(version)]
            top_version_rows.append({
                "source": source, "app_version": version, "reviews": int(count),
                "earliest": fmt_date(version_sub["_date"].min()), "latest": fmt_date(version_sub["_date"].max()),
            })
    version_df = pd.DataFrame(version_rows)
    top_versions_df = pd.DataFrame(top_version_rows)

    reply_rows = []
    for source in SOURCES:
        sub = df[df["source"].eq(source)]
        count = int((~missing_mask(sub["developer_reply"])).sum())
        reply_rows.append({
            "source": source,
            "field_availability": "available in source schema" if source == "Google Play" else "unavailable in saved source evidence",
            "reviews_with_reply": count,
            "reply_pct": pct(count, len(sub)),
        })
    reply_df = pd.DataFrame(reply_rows)

    # Monthly and yearly temporal coverage, including zero-review months in source coverage.
    monthly_parts = []
    for source in SOURCES:
        sub = df[df["source"].eq(source)].copy()
        sub["month"] = sub["_date"].dt.tz_localize(None).dt.to_period("M")
        grouped = sub.groupby("month").agg(
            review_count=("review_id", "size"), average_rating=("_rating", "mean"),
            low_rating_1_2_count=("_rating", lambda s: int(s.isin([1, 2]).sum())),
            five_star_count=("_rating", lambda s: int(s.eq(5).sum())),
        )
        full_index = pd.period_range(sub["month"].min(), sub["month"].max(), freq="M")
        grouped = grouped.reindex(full_index)
        grouped.index.name = "month"
        grouped["review_count"] = grouped["review_count"].fillna(0).astype(int)
        grouped["low_rating_1_2_count"] = grouped["low_rating_1_2_count"].fillna(0).astype(int)
        grouped["five_star_count"] = grouped["five_star_count"].fillna(0).astype(int)
        grouped["low_rating_1_2_pct"] = np.where(
            grouped["review_count"] > 0, 100 * grouped["low_rating_1_2_count"] / grouped["review_count"], np.nan
        )
        grouped["source"] = source
        monthly_parts.append(grouped.reset_index())
    monthly_sources = pd.concat(monthly_parts, ignore_index=True)

    all_months = pd.period_range(
        df["_date"].min().tz_localize(None).to_period("M"),
        df["_date"].max().tz_localize(None).to_period("M"), freq="M"
    )
    temp = df.copy()
    temp["month"] = temp["_date"].dt.tz_localize(None).dt.to_period("M")
    total_monthly = temp.groupby("month").agg(
        review_count=("review_id", "size"), average_rating=("_rating", "mean"),
        low_rating_1_2_count=("_rating", lambda s: int(s.isin([1, 2]).sum())),
        five_star_count=("_rating", lambda s: int(s.eq(5).sum())),
    ).reindex(all_months)
    total_monthly.index.name = "month"
    for col in ["review_count", "low_rating_1_2_count", "five_star_count"]:
        total_monthly[col] = total_monthly[col].fillna(0).astype(int)
    total_monthly["low_rating_1_2_pct"] = np.where(
        total_monthly["review_count"] > 0,
        100 * total_monthly["low_rating_1_2_count"] / total_monthly["review_count"], np.nan,
    )
    total_monthly["source"] = "Total"
    monthly = pd.concat([monthly_sources, total_monthly.reset_index()], ignore_index=True)
    monthly["month"] = monthly["month"].astype(str)
    monthly = monthly[["month", "source", "review_count", "average_rating", "low_rating_1_2_count", "low_rating_1_2_pct", "five_star_count"]]
    monthly.to_csv(TABLE_DIR / "monthly_review_volume.csv", index=False)

    temp["year"] = temp["_date"].dt.year
    yearly = temp.pivot_table(index="year", columns="source", values="review_id", aggfunc="size", fill_value=0)
    for source in SOURCES:
        if source not in yearly:
            yearly[source] = 0
    yearly["Total"] = yearly[SOURCES].sum(axis=1)
    yearly = yearly.reset_index()

    # Time windows and source imbalance.
    actual_min, actual_max = df["_date"].min(), df["_date"].max()
    as_min = df.loc[df["source"].eq("App Store"), "_date"].min()
    as_max = df.loc[df["source"].eq("App Store"), "_date"].max()
    options = [
        ("Full available history", actual_min, actual_max),
        ("Cross-platform overlap", as_min, as_max),
        ("Last 24 months", pd.Timestamp("2024-09-22T00:00:00Z"), ANCHOR),
        ("Last 18 months", pd.Timestamp("2025-03-22T00:00:00Z"), ANCHOR),
        ("Last 12 months", pd.Timestamp("2025-09-22T00:00:00Z"), ANCHOR),
        ("Last 6 months", pd.Timestamp("2026-03-22T00:00:00Z"), ANCHOR),
    ]
    window_df = pd.DataFrame([window_stats(df, name, start, end) for name, start, end in options])
    window_df.to_csv(TABLE_DIR / "time_window_comparison.csv", index=False)

    overlap = df[df["_date"].between(as_min, as_max, inclusive="both")]
    overlap_rating = (
        overlap.groupby(["source", "_rating"]).size().rename("count").reset_index().rename(columns={"_rating": "rating"})
    )
    gp_only = df[df["source"].eq("Google Play")]
    gp_before = gp_only[gp_only["_date"] < as_min]
    gp_after = gp_only[gp_only["_date"] > as_max]

    # Spikes: counts greater than Q3 + 1.5*IQR, separately by source.
    spike_rows = []
    spike_thresholds = []
    for source in SOURCES:
        source_months = monthly[monthly["source"].eq(source)].copy()
        counts = source_months["review_count"]
        q1, q3 = float(counts.quantile(0.25)), float(counts.quantile(0.75))
        iqr = q3 - q1
        threshold = q3 + 1.5 * iqr
        spike_thresholds.append({"source": source, "q1": q1, "q3": q3, "iqr": iqr, "threshold": threshold})
        for row in source_months[source_months["review_count"] > threshold].itertuples(index=False):
            month_records = temp[(temp["source"].eq(source)) & (temp["month"].astype(str).eq(row.month))]
            dist = month_records["_rating"].value_counts().reindex(range(1, 6), fill_value=0)
            spike_rows.append({
                "month": row.month, "source": source, "review_count": int(row.review_count),
                "rating_1": int(dist[1]), "rating_2": int(dist[2]), "rating_3": int(dist[3]),
                "rating_4": int(dist[4]), "rating_5": int(dist[5]),
                "low_rating_share_pct": pct(dist[1] + dist[2], row.review_count),
                "threshold": round(threshold, 2),
            })
    spikes_df = pd.DataFrame(spike_rows)
    thresholds_df = pd.DataFrame(spike_thresholds)

    # Issues register distinguishes errors, natural missingness and methodological limitations.
    short10 = int(df["_char_length"].le(10).sum())
    gp_missing_version = int(missing_mask(df.loc[df["source"].eq("Google Play"), "app_version"]).sum())
    total_exact_records = int(all_dup_sizes.sum())
    issues = [
        ["Missing app_version", "Google Play", gp_missing_version, pct(gp_missing_version, 3223), "data limitation", "medium", "Keep null; stratify version analyses by known-version coverage.", "No"],
        ["Very short reviews (<=10 characters)", "Both", short10, pct(short10, len(df)), "natural data characteristic", "low", "Retain; review manually and treat as low-context text.", "Yes"],
        ["Exact duplicate review text", "Both", total_exact_records, pct(total_exact_records, len(df)), "natural/ambiguous duplication", "medium", "Retain distinct review IDs; inspect groups before text-level modeling.", "Yes"],
        ["Missing title", "Google Play", 3223, 100.0, "source-unavailable field", "none", "Represent as null; do not treat as a quality failure.", "No"],
        ["Detected language unavailable", "Both", len(df), 100.0, "methodological limitation", "medium", "Run language detection later; do not substitute collection locale.", "No"],
        ["Developer reply unavailable", "App Store", 522, 100.0, "source-unavailable field", "low", "Report platform availability separately.", "No"],
        ["Collection locale unavailable", "App Store", 522, 100.0, "source-unavailable field", "low", "Use storefront metadata only; do not infer language.", "No"],
        ["Source imbalance", "Both", abs(3223 - 522), pct(3223, len(df)), "methodological limitation", "high", "Report source shares and consider source-stratified analysis; do not weight automatically.", "No"],
        ["Temporal coverage mismatch", "Both", len(gp_before) + len(gp_after), pct(len(gp_before) + len(gp_after), len(df)), "methodological limitation", "high", "Use overlap or recent windows for cross-platform comparisons.", "No"],
        ["App Store public endpoint instability", "App Store", 522, 100.0, "methodological limitation", "high", "Preserve provenance and qualify retrievability; do not claim lifetime completeness.", "No"],
    ]
    issues_df = pd.DataFrame(issues, columns=[
        "issue", "affected_source", "affected_rows", "percentage", "issue_type",
        "severity_for_analysis", "recommended_handling", "needs_manual_check",
    ])
    issues_df.to_csv(TABLE_DIR / "data_quality_issues.csv", index=False)

    # Charts.
    chart_rating = rating_df[rating_df["source"].isin(SOURCES)].pivot(index="rating", columns="source", values="count").reindex(range(1, 6))
    ax = chart_rating[SOURCES].plot(kind="bar", figsize=(9, 5.5), color=[COLORS[s] for s in SOURCES])
    ax.set_title("TCInvest Review Rating Distribution by Source")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Review count")
    ax.legend(title="Source")
    ax.grid(axis="y", alpha=0.25)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "rating_distribution_by_source.png", dpi=180)
    plt.close()

    plot_monthly = monthly[monthly["source"].isin(SOURCES)].pivot(index="month", columns="source", values="review_count").fillna(0)
    ax = plot_monthly[SOURCES].plot(figsize=(13, 5.5), color=[COLORS[s] for s in SOURCES], linewidth=1.8)
    ax.set_title("Monthly TCInvest Review Volume by Source")
    ax.set_xlabel("Month")
    ax.set_ylabel("Review count")
    tick_positions = np.arange(0, len(plot_monthly), 12)
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([plot_monthly.index[i] for i in tick_positions], rotation=45, ha="right")
    ax.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_review_volume_by_source.png", dpi=180)
    plt.close()

    plot_avg = monthly[monthly["source"].isin(SOURCES)].pivot(index="month", columns="source", values="average_rating")
    ax = plot_avg[SOURCES].plot(figsize=(13, 5.5), color=[COLORS[s] for s in SOURCES], linewidth=1.6, marker="o", markersize=2)
    ax.set_title("Monthly Average Rating by Source")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average rating")
    ax.set_ylim(1, 5.1)
    tick_positions = np.arange(0, len(plot_avg), 12)
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([plot_avg.index[i] for i in tick_positions], rotation=45, ha="right")
    ax.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_average_rating_by_source.png", dpi=180)
    plt.close()

    source_window = window_df.set_index("option")[["google_play_reviews", "app_store_reviews"]]
    source_window.columns = SOURCES
    ax = source_window[SOURCES].plot(kind="bar", stacked=True, figsize=(11, 6), color=[COLORS[s] for s in SOURCES])
    ax.set_title("Source Distribution Across Candidate Analysis Windows")
    ax.set_xlabel("Analysis window")
    ax.set_ylabel("Review count")
    ax.legend(title="Source")
    ax.grid(axis="y", alpha=0.25)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "time_window_source_distribution.png", dpi=180)
    plt.close()

    # Narrative report.
    overview = pd.DataFrame([
        {"Source": source, "Rows": len(df[df["source"].eq(source)]),
         "Unique review IDs": df.loc[df["source"].eq(source), "review_id"].nunique(),
         "Earliest": fmt_date(df.loc[df["source"].eq(source), "_date"].min()),
         "Latest": fmt_date(df.loc[df["source"].eq(source), "_date"].max())}
        for source in SOURCES
    ])
    missing_report = quality_df[(quality_df["source"].isin(SOURCES)) & quality_df["metric"].str.startswith("missing_")].copy()
    missing_report["Field"] = missing_report["metric"].str.removeprefix("missing_")
    missing_report = missing_report[["source", "Field", "count", "percentage", "classification"]]

    duplicate_examples = dup_df[dup_df["audit_type"].eq("exact_text_all_sources")].copy()
    duplicate_examples["representative_text"] = duplicate_examples["representative_text"].astype(str).str.slice(0, 100)
    duplicate_examples = duplicate_examples.sort_values("record_count", ascending=False)[
        ["source_scope", "representative_text", "record_count", "unique_review_ids"]
    ].head(10)

    time_options = window_df[[
        "option", "start_date", "end_date", "total_reviews", "google_play_reviews", "app_store_reviews",
        "google_play_share_pct", "app_store_share_pct", "low_rating_1_2_count",
    ]].copy()
    merits = {
        "Full available history": ("Maximum sample and long-term trend capability.", "Large source/coverage imbalance; older product states may be less relevant."),
        "Cross-platform overlap": ("Both sources are observable throughout the defined span.", "Still imbalanced and includes several product eras."),
        "Last 24 months": ("Recent, large sample with both platforms.", "May still mix older and current app versions."),
        "Last 18 months": ("Stronger current-product relevance with trend depth.", "Smaller sample and possible source imbalance."),
        "Last 12 months": ("High recency and both platforms represented.", "Less seasonality/history and smaller subgroup samples."),
        "Last 6 months": ("Most current customer voice.", "Smallest sample and weak trend/seasonality capability."),
    }
    time_options["Advantages"] = time_options["option"].map(lambda x: merits[x][0])
    time_options["Limitations"] = time_options["option"].map(lambda x: merits[x][1])

    source_imbalance = window_df[["option", "total_reviews", "google_play_share_pct", "app_store_share_pct"]].copy()
    source_imbalance["absolute_share_gap_pp"] = (source_imbalance["google_play_share_pct"] - source_imbalance["app_store_share_pct"]).abs()
    imbalance_low = source_imbalance.loc[source_imbalance["absolute_share_gap_pp"].idxmin(), "option"]
    imbalance_high = source_imbalance.loc[source_imbalance["absolute_share_gap_pp"].idxmax(), "option"]

    report = f"""# Data Quality Audit

## Dataset Overview

This is a read-only audit of the standardized TCInvest review data. It does not clean, remove, impute, classify, or modify records.

{md_table(overview)}

- Merged rows: **{len(df):,}**
- Unique `(source, review_id)` keys: **{df.drop_duplicates(['source', 'review_id']).shape[0]:,}**
- Duplicate `(source, review_id)` records involved: **{key_dupes:,}**
- Merged columns: **{len(merged.columns)} standardized fields** (temporary audit columns excluded)

## Missingness

{md_table(missing_report)}

Missing title on Google Play and missing developer-reply/collection-locale fields on App Store reflect source availability, not malformed rows. Missing `detected_language` is a methodological gap: collection locale and storefront must not be treated as actual review language.

## Rating Quality

- Rating minimum: **{df['_rating'].min():.0f}**; maximum: **{df['_rating'].max():.0f}**.
- Ratings outside 1–5: **{int((~df['_rating'].between(1,5) & df['_rating'].notna()).sum())}**.

{md_table(rating_df.pivot(index='rating', columns='source', values='count').reset_index())}

## Text Quality

Length metrics are descriptive only. Token-like length counts whitespace-separated non-empty sequences; it is not linguistic tokenization.

{md_table(text_stats_df)}

Short reviews are retained. They may be valid customer voice but contain less context for downstream analysis.

## Duplicate Text

{md_table(pd.DataFrame(exact_summary))}

- Exact-text groups appearing in both sources: **{len(cross):,}**, involving **{int(cross['records'].sum()) if len(cross) else 0:,} records**.
- Whitespace-only normalized duplicate groups with more than one exact serialization: **{int((dup_df['audit_type'] == 'whitespace_normalized_only').sum()):,}**.
- Exact same text is not evidence of the same user or invalidity; no review was removed.

Examples:

{md_table(duplicate_examples)}

## App Version Coverage

{md_table(version_df)}

Top versions and their observed review-date ranges:

{md_table(top_versions_df)}

No version was imputed. Google Play missing-version count is **{gp_missing_version:,}**.

## Developer Reply Coverage

{md_table(reply_df)}

App Store reply data are unavailable in the saved standardized source; that absence is not treated as a row-level quality failure.

## Temporal Coverage

Yearly review counts:

{md_table(yearly)}

Monthly volume, monthly average rating, low-rating counts, and five-star counts are provided in `monthly_review_volume.csv`. Monthly patterns are descriptive and do not establish causes.

## Source Imbalance

{md_table(source_imbalance)}

Among these options, **{imbalance_low}** has the lowest absolute source-share gap, while **{imbalance_high}** has the highest. This does not imply a weighting decision.

## Recent Time Windows

Windows are inclusive and anchored to 22 September 2026.

{md_table(window_df[window_df['option'].str.startswith('Last')])}

## Cross-platform Coverage

- Actual overlap: **{fmt_date(as_min)} to {fmt_date(as_max)}**.
- Reviews in overlap: **{len(overlap):,}** — Google Play **{int(overlap['source'].eq('Google Play').sum()):,}**, App Store **{int(overlap['source'].eq('App Store').sum()):,}**.
- Google Play before App Store coverage: **{len(gp_before):,}** reviews ({fmt_date(gp_before['_date'].min())} to {fmt_date(gp_before['_date'].max())}).
- Google Play after latest App Store review: **{len(gp_after):,}** reviews ({fmt_date(gp_after['_date'].min())} to {fmt_date(gp_after['_date'].max())}).

Rating distribution inside the overlap:

{md_table(overlap_rating)}

Cross-platform comparisons are not possible in the Google-Play-only periods without changing the population definition.

## Potential Spikes

Rule: for each source independently, a month is flagged when its review count is greater than `Q3 + 1.5 × IQR`, calculated over all calendar months in that source's observed coverage (including zero-review months).

Thresholds:

{md_table(thresholds_df)}

Flagged months:

{md_table(spikes_df)}

These flags are investigation prompts only; no causal explanation is inferred.

## Data Quality Issues

{md_table(issues_df)}

## Time Range Options

{md_table(time_options)}

No overall score or final time range is selected. The team should weigh recency, sample size, cross-platform coverage, source balance, current-product relevance, and trend capability.

## Limitations

- Reviews are self-selected public feedback and are not representative of all TCInvest customers.
- App Store public endpoint coverage has been unstable; 522 records mean retrievable saved evidence, not all lifetime reviews.
- Collection locale/storefront are metadata, not detected review language.
- Exact duplicate text may represent legitimate independent reviews; identity is keyed by `(source, review_id)`.
- Monthly spikes are statistical flags and cannot establish product-event causes.
- Average ratings do not adjust for source mix or review propensity.

## Recommended Next Decisions

1. Select an analysis time range after agreeing on the intended balance between recency, sample size, and cross-platform comparability.
2. Decide whether downstream reporting should be source-stratified and whether any weighting is methodologically justified.
3. Define handling rules for missing app versions, very short reviews, and duplicate text without deleting valid review IDs by default.
4. Plan language detection separately; do not reuse collection locale as language ground truth.
5. Investigate flagged months against documented product/release events before interpreting them.

## Integrity Verification

The audit script reads the three standardized inputs and both primary raw inputs only for analysis/hash verification. It does not write to those files. SHA-256 checks are compared before and after output generation.
"""
    REPORT_PATH.write_text(report, encoding="utf-8")

    after_hashes = {str(p.relative_to(ROOT)): sha256(p) for p in protected}
    if before_hashes != after_hashes:
        raise RuntimeError("A protected standardized/raw input changed during the audit")

    print("DATA QUALITY + TEMPORAL AUDIT")
    print(f"Total records: {len(df)}")
    print(f"Google Play: {(df['source'] == 'Google Play').sum()}")
    print(f"App Store: {(df['source'] == 'App Store').sum()}")
    print(f"Duplicate keys (records involved): {key_dupes}")
    print(f"Exact duplicate text: {len(all_dup_sizes)} groups, {int(all_dup_sizes.sum())} records")
    print(f"Very short <=10: {short10}")
    print(f"Missing app_version: {int(missing_mask(df['app_version']).sum())} total ({gp_missing_version} Google Play)")
    print("WINDOWS")
    print(window_df.to_string(index=False))
    print("SPIKES")
    print(spikes_df.to_string(index=False))
    print("HASHES_UNCHANGED: YES")
    for path, digest in after_hashes.items():
        print(f"{digest}  {path}")


if __name__ == "__main__":
    main()
