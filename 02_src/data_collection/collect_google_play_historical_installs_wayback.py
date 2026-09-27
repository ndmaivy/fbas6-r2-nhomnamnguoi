"""Collect archived public Google Play install signals for TCInvest.

This is a diagnostic collector, not a downloads collector. Google Play public
pages expose coarse cumulative install bands, and Wayback coverage can be
missing or inconsistent. The script therefore emits exactly one audit row per
target month, leaves missing observations null, and never forward-fills or
interpolates values.
"""

from __future__ import annotations

import csv
import html as html_lib
import json
import re
import time
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import pandas as pd
import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[2]
CURRENT_COLLECTOR = ROOT / "02_src" / "data_collection" / "collect_google_play.py"
OUTPUT_DIR = ROOT / "01_data" / "raw" / "google_play" / "historical_app_metrics"
RAW_HTML_DIR = OUTPUT_DIR / "wayback" / "raw_html"
OUTPUT_CSV = OUTPUT_DIR / "tcinvest_google_play_historical_installs_sep2024_aug2025.csv"
CHANGE_CSV = ROOT / "05_outputs" / "tables" / "google_play_historical_install_change_validation.csv"
TEMPLATE_CSV = ROOT / "05_outputs" / "tables" / "similarweb_google_play_download_validation_template.csv"
METHODOLOGY_FILE = ROOT / "00_docs" / "methodology" / "google_play_historical_install_validation.md"

CDX_ENDPOINT = "https://web.archive.org/cdx/search/cdx"
AVAILABILITY_ENDPOINT = "https://archive.org/wayback/available"
TARGET_MONTHS = pd.period_range("2024-09", "2025-08", freq="M")
CDX_FROM = "20240817"
CDX_TO = "20250915"
MAX_RETRIES = 3
BACKOFF_SECONDS = (1, 2, 4)
REQUEST_DELAY_SECONDS = 1.0
REQUEST_TIMEOUT_SECONDS = 40
USER_AGENT = (
    "TCInvest-research-historical-install-audit/1.0 "
    "(public Wayback diagnostic; low request rate)"
)

OUTPUT_COLUMNS = [
    "target_month",
    "target_month_end",
    "snapshot_timestamp",
    "snapshot_date",
    "days_from_target_month_end",
    "app_id",
    "app_title",
    "installs_text",
    "min_installs",
    "install_band_lower",
    "install_band_upper",
    "rating_score",
    "rating_count",
    "review_count",
    "archive_url",
    "source_url",
    "extraction_method",
    "extraction_confidence",
    "status",
    "notes",
]

INSTALL_LABELS = (
    "downloads",
    "download",
    "installs",
    "install",
    "lượt tải xuống",
    "lượt cài đặt",
    "tải xuống",
)


@dataclass(frozen=True)
class Snapshot:
    timestamp: str
    original: str
    statuscode: str
    mimetype: str
    digest: str
    url_priority: int

    @property
    def instant(self) -> datetime:
        return datetime.strptime(self.timestamp, "%Y%m%d%H%M%S").replace(
            tzinfo=timezone.utc
        )

    @property
    def snapshot_date(self) -> date:
        return self.instant.date()

    @property
    def archive_url(self) -> str:
        return f"https://web.archive.org/web/{self.timestamp}id_/{self.original}"


def load_package_id() -> str:
    """Reuse APP_ID from the existing production review collector."""
    source = CURRENT_COLLECTOR.read_text(encoding="utf-8")
    match = re.search(r'^APP_ID\s*=\s*["\']([^"\']+)["\']', source, flags=re.MULTILINE)
    if not match:
        raise RuntimeError(f"APP_ID not found in {CURRENT_COLLECTOR}")
    return match.group(1)


def request_with_retry(
    session: requests.Session, url: str, *, params: dict[str, Any] | None = None
) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.get(
                url,
                params=params,
                timeout=REQUEST_TIMEOUT_SECONDS,
                allow_redirects=True,
            )
            if response.status_code in {429, 500, 502, 503, 504}:
                raise requests.HTTPError(
                    f"transient HTTP {response.status_code}", response=response
                )
            return response
        except requests.RequestException as exc:
            last_error = exc
            print(f"Request attempt {attempt}/{MAX_RETRIES} failed: {exc}")
            if attempt < MAX_RETRIES:
                time.sleep(BACKOFF_SECONDS[attempt - 1])
    raise RuntimeError(f"request failed after {MAX_RETRIES} attempts: {last_error}")


def query_cdx(
    session: requests.Session,
    source_url: str,
    url_priority: int,
    *,
    match_type: str | None = None,
) -> tuple[list[Snapshot], str | None]:
    params = {
        "url": source_url,
        "from": CDX_FROM,
        "to": CDX_TO,
        "output": "json",
        "fl": "timestamp,original,statuscode,mimetype,digest",
        "filter": "statuscode:200",
        "sort": "ascending",
    }
    if match_type:
        params["matchType"] = match_type
    try:
        response = request_with_retry(session, CDX_ENDPOINT, params=params)
        if response.status_code != 200:
            return [], f"CDX HTTP {response.status_code}"
        payload = response.json()
    except (RuntimeError, ValueError) as exc:
        return [], f"CDX request/parsing failure: {exc}"

    if not isinstance(payload, list) or not payload:
        return [], "CDX returned no rows"

    header = payload[0]
    if not isinstance(header, list):
        return [], "CDX response did not contain a header row"

    snapshots: list[Snapshot] = []
    for raw_row in payload[1:]:
        if not isinstance(raw_row, list) or len(raw_row) != len(header):
            continue
        row = dict(zip(header, raw_row))
        timestamp = str(row.get("timestamp", ""))
        if not re.fullmatch(r"\d{14}", timestamp):
            continue
        snapshots.append(
            Snapshot(
                timestamp=timestamp,
                original=str(row.get("original") or source_url),
                statuscode=str(row.get("statuscode") or ""),
                mimetype=str(row.get("mimetype") or ""),
                digest=str(row.get("digest") or ""),
                url_priority=url_priority,
            )
        )
    return snapshots, None


def query_availability_fallback(
    session: requests.Session,
    source_urls: list[tuple[str, int]],
) -> tuple[list[Snapshot], list[str]]:
    """Ask Wayback's availability API for the closest month-end captures.

    This fallback is used only if CDX returns no captures. Returned timestamps
    still pass the normal within-month/plus-or-minus-15-day selection rule.
    """
    snapshots: list[Snapshot] = []
    notes: list[str] = []
    for month in TARGET_MONTHS:
        target_timestamp = month.end_time.strftime("%Y%m%d235959")
        month_found = False
        for source_url, priority in source_urls:
            try:
                response = request_with_retry(
                    session,
                    AVAILABILITY_ENDPOINT,
                    params={"url": source_url, "timestamp": target_timestamp},
                )
            except (RuntimeError, ValueError) as exc:
                notes.append(f"Availability {month} {source_url}: {exc}")
                time.sleep(REQUEST_DELAY_SECONDS)
                continue
            time.sleep(REQUEST_DELAY_SECONDS)
            if response.status_code != 200:
                notes.append(
                    f"Availability {month} {source_url}: HTTP {response.status_code}"
                )
                continue
            try:
                payload = response.json()
            except ValueError as exc:
                notes.append(f"Availability {month} {source_url}: invalid JSON: {exc}")
                continue

            closest = (payload.get("archived_snapshots") or {}).get("closest") or {}
            timestamp = str(closest.get("timestamp") or "")
            archive_url = str(closest.get("url") or "")
            if closest.get("available") and re.fullmatch(r"\d{14}", timestamp):
                original = source_url
                replay_match = re.search(r"/web/\d+(?:id_)?/(https?://.+)$", archive_url)
                if replay_match:
                    original = replay_match.group(1)
                snapshots.append(
                    Snapshot(
                        timestamp=timestamp,
                        original=original,
                        statuscode=str(closest.get("status") or ""),
                        mimetype="",
                        digest="",
                        url_priority=priority,
                    )
                )
                notes.append(
                    f"Availability {month} {source_url}: closest={timestamp}"
                )
                month_found = True
                break
            notes.append(f"Availability {month} {source_url}: no capture")
    return snapshots, notes


def select_snapshot(month: pd.Period, snapshots: list[Snapshot]) -> tuple[Snapshot | None, str]:
    month_start = month.start_time.date()
    month_end = month.end_time.date()
    within_month = [
        snapshot
        for snapshot in snapshots
        if month_start <= snapshot.snapshot_date <= month_end
    ]
    if within_month:
        selected = max(
            within_month,
            key=lambda item: (item.instant, -item.url_priority),
        )
        return selected, "latest available snapshot within target month"

    nearby = [
        snapshot
        for snapshot in snapshots
        if abs((snapshot.snapshot_date - month_end).days) <= 15
    ]
    if nearby:
        selected = min(
            nearby,
            key=lambda item: (
                abs((item.snapshot_date - month_end).days),
                item.url_priority,
                -item.instant.timestamp(),
            ),
        )
        return selected, "nearest snapshot to month-end within +/-15 days"
    return None, "no snapshot in target month or within +/-15 days of month-end"


def normalize_install_token(token: str) -> int | None:
    cleaned = html_lib.unescape(token).replace("\xa0", " ").strip().upper()
    cleaned = re.sub(r"\s+", "", cleaned).rstrip("+")
    match = re.fullmatch(r"([0-9]+(?:[.,][0-9]+)?)(TR|K|N|M|B|T)?", cleaned)
    if not match:
        # Full thousands-separated numbers such as 1,000,000 or 1.000.000.
        if re.fullmatch(r"[0-9][0-9.,]*", cleaned):
            digits = re.sub(r"[.,]", "", cleaned)
            return int(digits) if digits else None
        return None

    number_text, suffix = match.groups()
    if suffix:
        multiplier = {
            "K": 1_000,
            "N": 1_000,
            "M": 1_000_000,
            "TR": 1_000_000,
            "B": 1_000_000_000,
            "T": 1_000_000_000,
        }[suffix]
        number = float(number_text.replace(",", "."))
        return int(number * multiplier)

    if "," in number_text or "." in number_text:
        # Without a suffix, punctuation is treated as a thousands separator.
        return int(re.sub(r"[.,]", "", number_text))
    return int(number_text)


def contextual_install_candidates(text: str) -> list[tuple[str, str, str]]:
    """Return (token, method, context) only when an install label is nearby."""
    normalized = html_lib.unescape(text).replace("\\u0026", "&")
    token_pattern = r"(?<!\w)([0-9]+(?:[.,][0-9]+)*(?:\s*(?:TR|Tr|tr|K|k|N|n|M|m|B|b|T|t))?\s*\+)"
    label_pattern = "|".join(re.escape(label) for label in INSTALL_LABELS)
    patterns = (
        re.compile(
            rf"{token_pattern}.{{0,100}}?(?:{label_pattern})",
            flags=re.IGNORECASE | re.DOTALL,
        ),
        re.compile(
            rf"(?:{label_pattern}).{{0,100}}?{token_pattern}",
            flags=re.IGNORECASE | re.DOTALL,
        ),
    )
    candidates: list[tuple[str, str, str]] = []
    for pattern in patterns:
        for match in pattern.finditer(normalized):
            token = match.group(1)
            context = re.sub(r"\s+", " ", match.group(0)).strip()[:220]
            candidates.append((token, "CONTEXT_LABEL_REGEX", context))
    return candidates


def iter_json_objects(soup: BeautifulSoup):
    for script in soup.find_all("script"):
        script_type = str(script.get("type") or "").lower()
        if "ld+json" not in script_type:
            continue
        raw = script.string or script.get_text()
        try:
            payload = json.loads(raw)
        except (TypeError, json.JSONDecodeError):
            continue
        if isinstance(payload, list):
            yield from payload
        else:
            yield payload


def find_json_key(payload: Any, key_names: set[str]) -> Any:
    if isinstance(payload, dict):
        for key, value in payload.items():
            if str(key).lower() in key_names and value not in (None, ""):
                return value
        for value in payload.values():
            found = find_json_key(value, key_names)
            if found not in (None, ""):
                return found
    elif isinstance(payload, list):
        for value in payload:
            found = find_json_key(value, key_names)
            if found not in (None, ""):
                return found
    return None


def parse_nonnegative_integer(value: Any) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    cleaned = re.sub(r"[^0-9]", "", str(value))
    return int(cleaned) if cleaned else None


def parse_rating(value: Any) -> float | None:
    if value is None:
        return None
    match = re.search(r"[0-9]+(?:[.,][0-9]+)?", str(value))
    if not match:
        return None
    parsed = float(match.group(0).replace(",", "."))
    return parsed if 0 <= parsed <= 5 else None


def extract_fields(page_html: str, package_id: str) -> dict[str, Any]:
    soup = BeautifulSoup(page_html, "html.parser")
    visible_text = soup.get_text(" ", strip=True)
    app_title: str | None = None
    rating_score: float | None = None
    rating_count: int | None = None
    review_count: int | None = None

    json_objects = list(iter_json_objects(soup))
    for payload in json_objects:
        if app_title is None:
            raw_title = find_json_key(payload, {"name"})
            if raw_title:
                app_title = str(raw_title).strip()
        aggregate = find_json_key(payload, {"aggregaterating"})
        if isinstance(aggregate, dict):
            rating_score = rating_score or parse_rating(
                find_json_key(aggregate, {"ratingvalue"})
            )
            rating_count = rating_count or parse_nonnegative_integer(
                find_json_key(aggregate, {"ratingcount"})
            )
            review_count = review_count or parse_nonnegative_integer(
                find_json_key(aggregate, {"reviewcount"})
            )

    if app_title is None:
        og_title = soup.find("meta", attrs={"property": "og:title"})
        if og_title and og_title.get("content"):
            app_title = str(og_title["content"]).strip()
        elif soup.title and soup.title.string:
            app_title = re.sub(
                r"\s*-\s*Apps on Google Play\s*$", "", soup.title.string.strip()
            )

    candidates: list[tuple[str, str, str]] = []
    candidates.extend(contextual_install_candidates(visible_text))
    if not candidates:
        candidates.extend(contextual_install_candidates(page_html))

    parsed_candidates: list[tuple[int, str, str, str]] = []
    for token, method, context in candidates:
        value = normalize_install_token(token)
        if value is not None and value >= 0:
            parsed_candidates.append((value, token.strip(), method, context))

    installs_text: str | None = None
    install_lower: int | None = None
    extraction_method = "NONE"
    confidence = "LOW"
    notes: list[str] = []

    if parsed_candidates:
        distinct_values = sorted({candidate[0] for candidate in parsed_candidates})
        if len(distinct_values) == 1:
            install_lower, installs_text, extraction_method, context = parsed_candidates[0]
            extraction_method = (
                "VISIBLE_TEXT_CONTEXT"
                if installs_text in visible_text
                else "HTML_SCRIPT_CONTEXT"
            )
            confidence = "HIGH" if extraction_method == "VISIBLE_TEXT_CONTEXT" else "MEDIUM"
            notes.append(f"Install token found next to an install/download label: {context}")
        else:
            notes.append(
                "Conflicting context-qualified install tokens found: "
                + ", ".join(str(value) for value in distinct_values)
            )

    package_present = package_id in page_html
    if not package_present:
        notes.append("Expected package ID was not found in archived HTML.")

    return {
        "app_title": app_title,
        "installs_text": installs_text,
        "min_installs": install_lower,
        "install_band_lower": install_lower,
        "install_band_upper": None,
        "rating_score": rating_score,
        "rating_count": rating_count,
        "review_count": review_count,
        "extraction_method": extraction_method,
        "extraction_confidence": confidence,
        "package_present": package_present,
        "notes": " ".join(notes),
    }


def empty_row(month: pd.Period, package_id: str) -> dict[str, Any]:
    month_end = month.end_time.date()
    return {
        "target_month": str(month),
        "target_month_end": month_end.isoformat(),
        "snapshot_timestamp": None,
        "snapshot_date": None,
        "days_from_target_month_end": None,
        "app_id": package_id,
        "app_title": None,
        "installs_text": None,
        "min_installs": None,
        "install_band_lower": None,
        "install_band_upper": None,
        "rating_score": None,
        "rating_count": None,
        "review_count": None,
        "archive_url": None,
        "source_url": None,
        "extraction_method": "NONE",
        "extraction_confidence": "LOW",
        "status": "NO_SNAPSHOT",
        "notes": None,
    }


def safe_join_notes(*parts: str | None) -> str:
    return " ".join(str(part).strip() for part in parts if part and str(part).strip())


def build_change_table(results: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    previous: pd.Series | None = None
    caveat = (
        "Google Play public install bands are coarse cumulative thresholds. "
        "An unchanged band does not imply zero new downloads."
    )
    for _, row in results.sort_values("target_month").iterrows():
        current = row["install_band_lower"]
        output = {
            "month": row["target_month"],
            "current_observed_install_lower": current,
            "previous_observed_install_lower": None,
            "observed_lower_bound_change": None,
            "days_between_observations": None,
            "comparable": False,
            "notes": "No usable cumulative install-band observation for this month.",
        }
        if pd.notna(current):
            if previous is None:
                output["notes"] = "First usable observation; no prior observation to compare."
            else:
                prior = previous["install_band_lower"]
                current_date = pd.to_datetime(row["snapshot_date"])
                prior_date = pd.to_datetime(previous["snapshot_date"])
                change = int(current) - int(prior)
                output.update(
                    {
                        "previous_observed_install_lower": prior,
                        "observed_lower_bound_change": change,
                        "days_between_observations": int((current_date - prior_date).days),
                    }
                )
                if change == 0:
                    output["notes"] = caveat
                else:
                    output["comparable"] = True
                    output["notes"] = (
                        "Observed cumulative public install lower-bound change between "
                        "archived observations; this is not official monthly downloads."
                    )
            previous = row
        rows.append(output)
    return pd.DataFrame(rows)


def write_template() -> None:
    TEMPLATE_CSV.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "month",
        "similarweb_estimated_downloads",
        "google_play_archived_install_band",
        "google_play_install_band_lower",
        "rating_count",
        "review_count",
        "validation_comment",
    ]
    pd.DataFrame(columns=columns).to_csv(TEMPLATE_CSV, index=False)


def write_methodology(
    package_id: str,
    snapshot_count: int,
    cdx_notes: list[str],
    results: pd.DataFrame,
) -> None:
    usable = results[results["install_band_lower"].notna()]
    usable_months = ", ".join(usable["target_month"].astype(str)) or "None"
    missing_months = ", ".join(
        results.loc[results["install_band_lower"].isna(), "target_month"].astype(str)
    ) or "None"
    bands = ", ".join(
        sorted({str(value) for value in usable["installs_text"].dropna()})
    ) or "None"
    raw_html_count = len(list(RAW_HTML_DIR.glob("*.html")))
    overall = (
        "USABLE"
        if len(usable) == 12
        else "PARTIALLY_USABLE"
        if len(usable) > 0
        else "NOT_USABLE"
    )
    cdx_detail = "\n".join(f"- {note}" for note in cdx_notes) or "- No CDX errors."
    content = f"""# Google Play Historical Install Validation

## Research purpose

Attempt to obtain historical public Google Play cumulative install signals for TCInvest from archived store pages between Sep 2024 and Aug 2025.

## Data source

Wayback Machine archived copies of the public Google Play listing for package `{package_id}`. The collector queried both the Vietnam-localized URL (`hl=vi&gl=VN`) and the canonical listing URL. It found {snapshot_count} unique CDX snapshot records in the diagnostic query window.

CDX/query notes:

{cdx_detail}

## Snapshot selection

For each target month, the collector selected the latest available snapshot within that month. When a month had no snapshot, it considered the closest snapshot within 15 days of that month-end. It did not carry observations forward and did not interpolate missing values.

## What the metric means

Historical installs extracted from archived Google Play pages are cumulative public install bands/signals.

They are **not**:

- exact monthly downloads;
- Google Play Console first-party acquisition data;
- App Store downloads;
- TCBS internal analytics.

## Extraction and QA result

- Target months: 12
- Months with a usable install signal: {len(usable)}
- Usable months: {usable_months}
- Months without an extracted install signal: {missing_months}
- Extracted public install bands: {bands}
- Archived HTML files downloaded and inspectable: {raw_html_count}
- Overall usability: **{overall}**

Extraction required an install-like numeric token to occur near an explicit Google Play install/download label. Ambiguous or context-free numbers were not assigned to install fields. Raw archived HTML was retained for every successfully downloaded selected snapshot.

The requested inspection of at least two archived HTML snapshots could not be performed because Wayback returned no captures for the tested exact, prefix, wildcard, or month-end availability queries. No placeholder HTML was created.

## Why it is useful

When observations exist, archived cumulative public install bands can be used as an independent, coarse sanity check for third-party estimated downloads such as Similarweb. A change between observations is reported only as an **observed cumulative install lower-bound change**, never as official monthly downloads.

## Important limitation

Google Play public install counts are usually coarse thresholds, so they may remain unchanged despite substantial new downloads. An unchanged band does not imply zero new downloads.

Wayback coverage may also be incomplete or inconsistent. Archived pages can contain consent/interstitial responses, dynamically rendered content, or incomplete replay assets. Missing extraction therefore does not establish that the live listing lacked an install signal at that time.
"""
    METHODOLOGY_FILE.parent.mkdir(parents=True, exist_ok=True)
    METHODOLOGY_FILE.write_text(content, encoding="utf-8")


def validate_results(results: pd.DataFrame) -> None:
    errors: list[str] = []
    if len(results) != 12:
        errors.append(f"expected 12 target rows, found {len(results)}")
    if results["target_month"].duplicated().any():
        errors.append("duplicate target_month values")
    expected_months = {str(month) for month in TARGET_MONTHS}
    if set(results["target_month"].astype(str)) != expected_months:
        errors.append("target-month set does not match Sep 2024 through Aug 2025")

    for column in ("install_band_lower", "rating_count", "review_count"):
        values = pd.to_numeric(results[column], errors="coerce")
        if (values.dropna() < 0).any():
            errors.append(f"negative values found in {column}")
    ratings = pd.to_numeric(results["rating_score"], errors="coerce")
    if ((ratings.dropna() < 0) | (ratings.dropna() > 5)).any():
        errors.append("rating_score outside [0, 5]")
    ok_rows = results[results["status"].isin(["OK", "MONOTONICITY_WARNING"])]
    if not ok_rows["archive_url"].fillna("").str.startswith(
        "https://web.archive.org/"
    ).all():
        errors.append("an OK row has a non-Wayback archive URL")
    if errors:
        raise RuntimeError("QA failed: " + "; ".join(errors))


def main() -> None:
    package_id = load_package_id()
    print(f"Package ID: {package_id}")

    localized_url = (
        "https://play.google.com/store/apps/details?"
        + urlencode({"id": package_id, "hl": "vi", "gl": "VN"})
    )
    canonical_url = "https://play.google.com/store/apps/details?" + urlencode(
        {"id": package_id}
    )
    source_urls = [(localized_url, 0), (canonical_url, 1)]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_HTML_DIR.mkdir(parents=True, exist_ok=True)
    CHANGE_CSV.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    all_snapshots: list[Snapshot] = []
    cdx_notes: list[str] = []
    cdx_queries = [
        (localized_url, 0, None, "localized exact"),
        (canonical_url, 1, None, "canonical exact"),
        (canonical_url, 1, "prefix", "canonical prefix"),
        (
            f"play.google.com/store/apps/details?id={package_id}*",
            1,
            None,
            "package wildcard",
        ),
    ]
    for source_url, priority, match_type, query_label in cdx_queries:
        print(f"Querying CDX ({query_label}): {source_url}")
        snapshots, error = query_cdx(
            session, source_url, priority, match_type=match_type
        )
        all_snapshots.extend(snapshots)
        cdx_notes.append(
            f"{query_label} — {source_url}: {len(snapshots)} snapshots"
            + (f"; {error}" if error else "")
        )
        time.sleep(REQUEST_DELAY_SECONDS)

    if not all_snapshots:
        print("CDX found no snapshots; trying Wayback Availability API fallback")
        fallback_snapshots, fallback_notes = query_availability_fallback(
            session, source_urls
        )
        all_snapshots.extend(fallback_snapshots)
        cdx_notes.extend(fallback_notes)

    unique_snapshots: dict[tuple[str, str], Snapshot] = {}
    for snapshot in all_snapshots:
        unique_snapshots[(snapshot.timestamp, snapshot.original)] = snapshot
    snapshots = sorted(unique_snapshots.values(), key=lambda item: item.instant)
    print(f"Unique CDX snapshots found: {len(snapshots)}")

    download_cache: dict[tuple[str, str], tuple[str | None, str, str, int]] = {}
    rows: list[dict[str, Any]] = []
    for month in TARGET_MONTHS:
        row = empty_row(month, package_id)
        snapshot, selection_note = select_snapshot(month, snapshots)
        if snapshot is None:
            row["notes"] = selection_note
            rows.append(row)
            print(f"[{month}] NO_SNAPSHOT")
            continue

        key = (snapshot.timestamp, snapshot.original)
        if key not in download_cache:
            try:
                response = request_with_retry(session, snapshot.archive_url)
                content_type = response.headers.get("content-type", "")
                size = len(response.content)
                if response.status_code == 200:
                    response.encoding = response.encoding or "utf-8"
                    page_html = response.text
                    download_error = ""
                else:
                    page_html = None
                    download_error = f"archive HTTP {response.status_code}"
                download_cache[key] = (page_html, download_error, content_type, size)
            except RuntimeError as exc:
                download_cache[key] = (None, str(exc), "", 0)
            time.sleep(REQUEST_DELAY_SECONDS)

        page_html, download_error, content_type, response_size = download_cache[key]
        days_from_end = (snapshot.snapshot_date - month.end_time.date()).days
        row.update(
            {
                "snapshot_timestamp": snapshot.timestamp,
                "snapshot_date": snapshot.snapshot_date.isoformat(),
                "days_from_target_month_end": days_from_end,
                "archive_url": snapshot.archive_url,
                "source_url": snapshot.original,
            }
        )

        response_note = (
            f"Selection: {selection_note}. Response content-type={content_type or 'unknown'}; "
            f"size={response_size} bytes."
        )
        if page_html is None:
            row["status"] = "DOWNLOAD_FAILED"
            row["notes"] = safe_join_notes(selection_note, response_note, download_error)
            rows.append(row)
            print(f"[{month}] DOWNLOAD_FAILED: {download_error}")
            continue

        raw_name = (
            f"{snapshot.snapshot_date.isoformat()}_{snapshot.timestamp}_"
            "tcinvest_google_play.html"
        )
        raw_path = RAW_HTML_DIR / raw_name
        if not raw_path.exists():
            raw_path.write_text(page_html, encoding="utf-8")

        extracted = extract_fields(page_html, package_id)
        for field in (
            "app_title",
            "installs_text",
            "min_installs",
            "install_band_lower",
            "install_band_upper",
            "rating_score",
            "rating_count",
            "review_count",
            "extraction_method",
            "extraction_confidence",
        ):
            row[field] = extracted[field]
        row["status"] = (
            "OK" if extracted["install_band_lower"] is not None else "EXTRACTION_FAILED"
        )
        row["notes"] = safe_join_notes(
            selection_note,
            response_note,
            f"Raw HTML: {raw_path.relative_to(ROOT)}.",
            extracted["notes"],
        )
        rows.append(row)
        print(
            f"[{month}] {row['status']}: snapshot={snapshot.timestamp}, "
            f"installs={row['installs_text']}"
        )

    results = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)

    # Flag, but never alter, a decrease in chronological cumulative lower bands.
    last_lower: int | None = None
    for index in results.sort_values("target_month").index:
        lower = results.at[index, "install_band_lower"]
        if pd.isna(lower):
            continue
        current_lower = int(lower)
        if last_lower is not None and current_lower < last_lower:
            results.at[index, "status"] = "MONOTONICITY_WARNING"
            results.at[index, "notes"] = safe_join_notes(
                results.at[index, "notes"],
                f"Install lower band decreased from {last_lower} to {current_lower}; "
                "verify extraction and snapshot content.",
            )
        last_lower = current_lower

    validate_results(results)
    results.to_csv(OUTPUT_CSV, index=False, quoting=csv.QUOTE_MINIMAL)

    changes = build_change_table(results)
    changes.to_csv(CHANGE_CSV, index=False)
    write_template()
    write_methodology(package_id, len(snapshots), cdx_notes, results)

    print("\nHistorical install audit complete")
    print(f"Target rows: {len(results)}")
    print(f"Usable install observations: {results['install_band_lower'].notna().sum()}")
    print(f"Output: {OUTPUT_CSV.relative_to(ROOT)}")
    print(f"Change validation: {CHANGE_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
