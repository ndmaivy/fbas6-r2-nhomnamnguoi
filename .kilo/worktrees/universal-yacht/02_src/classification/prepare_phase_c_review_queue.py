"""Retrieve unlabeled Phase C *candidates* for human discovery, not labels.

Run from the repository root: python 02_src/classification/prepare_phase_c_review_queue.py
Only the selected review keys and unmodified source text are exported. The
lexicons are retrieval aids; a match is never evidence that a theme exists.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "01_data/processed/reviews_analysis_24m.csv"
SAMPLE = ROOT / "04_analysis/taxonomy/phase-b/phase_b_reviews_final.csv"
OUTPUT = ROOT / "04_analysis/taxonomy/phase-c/targeted_review_queue.csv"

PATTERNS = {
    "FEE_PRICING": r"phí giao dịch|lãi suất|phí vay|phí lưu ký|phí.{0,12}cao",
    "ACCOUNT_RECOVERY_PROFILE_CHANGE": r"đổi sđt|đổi số điện thoại|thay đổi.{0,12}cccd|cập nhật.{0,12}cccd|điện thoại cũ",
    "MOBILE_TABLET_RESPONSIVENESS": r"ipad|tablet|font|chữ nhỏ|xoay màn hình",
    "MARKET_DATA_STALENESS_ACCURACY": r"bảng điện|bảng giá|giá thị trường|giá nav|realtime|cập nhật.{0,12}giá",
    "AI_SUPPORT_CONTEXT_QUALITY": r"chatbot|chat bot|bot trả lời|ai hỗ trợ|ai chat|tổng đài.{0,12}ai",
    "NOTIFICATION_COMMUNICATION": r"thông báo|email|e-mail|mail|tin nhắn",
    "SECURITY_ACCOUNT_PROTECTION": r"bảo mật|an toàn|bị hack|lừa đảo",
    "EXCESSIVE_DATA_CONSUMPTION": r"dung lượng|tốn.{0,12}data|mb data|dữ liệu di động|hết.{0,12}(?:4g|5g)",
    "DIGITAL_SIGNATURE_FLOW": r"chữ ký số|ký số|chữ ký điện tử",
    "MARKET_RESEARCH_RECOMMENDATION_UTILITY": r"khuyến nghị|báo cáo phân tích|phân tích thị trường|chuyên gia phân tích",
}


def main() -> None:
    analysis = pd.read_csv(INPUT, dtype=str, keep_default_na=False)
    sample = pd.read_csv(SAMPLE, dtype=str, keep_default_na=False)
    assert len(analysis) == 736 and len(sample) == 100
    seen = set(zip(sample.source, sample.review_id))
    pool = analysis[
        [key not in seen for key in zip(analysis.source, analysis.review_id)]
    ].copy()
    pool["search_text"] = (pool.title + " " + pool.review_text_raw).str.lower()
    pool["rank"] = pool.apply(
        lambda row: hashlib.sha256(
            f"{row.source}|{row.review_id}".encode("utf-8")
        ).hexdigest(),
        axis=1,
    )
    used: set[tuple[str, str]] = set()
    selected = []
    for theme, pattern in PATTERNS.items():
        matches = pool.loc[
            pool.search_text.str.contains(pattern, regex=True, na=False)
        ].sort_values("rank")
        chosen = []
        for source in ["App Store", "Google Play"]:
            candidates = matches.loc[
                matches.source.eq(source)
                & ~matches.apply(
                    lambda row: (row.source, row.review_id) in used, axis=1
                )
            ]
            if not candidates.empty:
                chosen.append(candidates.iloc[0])
                used.add((source, candidates.iloc[0].review_id))
        if len(chosen) < 2:
            for row in matches.itertuples(index=False):
                key = (row.source, row.review_id)
                if key not in used:
                    chosen.append(matches.loc[matches.review_id.eq(row.review_id)].iloc[0])
                    used.add(key)
                if len(chosen) == 2:
                    break
        for row in chosen:
            selected.append({
                "source": row.source,
                "review_id": row.review_id,
                "review_date": row.review_date,
                "rating": row.rating,
                "title": row.title,
                "review_text_raw": row.review_text_raw,
                "retrieval_theme": theme,
                "retrieval_pattern": pattern,
                "review_status": "UNREVIEWED",
            })
        print(f"{theme}: {len(matches)} keyword hits, {len(chosen)} queued")
    result = pd.DataFrame(selected, columns=[
        "source", "review_id", "review_date", "rating", "title",
        "review_text_raw", "retrieval_theme", "retrieval_pattern", "review_status",
    ])
    assert not result.duplicated(["source", "review_id"]).any()
    assert all((s, rid) not in seen for s, rid in zip(result.source, result.review_id))
    assert result.review_status.eq("UNREVIEWED").all()
    result.to_csv(OUTPUT, index=False, encoding="utf-8-sig")
    print(f"Total candidates: {len(result)}; saved to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
