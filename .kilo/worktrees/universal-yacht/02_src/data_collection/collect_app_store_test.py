import json
import time
from pathlib import Path
import xml.etree.ElementTree as ET

import pandas as pd
import requests


APP_ID = "1037255487"

# Các storefront cần thu thập (vn -> tiếng Việt, us -> tiếng Anh)
STOREFRONTS = [
    {"country": "vn", "lang": "vi_vn"},
    {"country": "us", "lang": "en_us"},
]

MAX_PAGES = 10

# Retry cho HTTP/network
MAX_REQUEST_RETRIES = 3
REQUEST_DELAY = 1.0


ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "01_data" / "raw" / "app_store"
RAW_DATA_DIR = OUTPUT_DIR / "raw_responses"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "app_store_test.csv"
SUMMARY_FILE = OUTPUT_DIR / "app_store_summary.json"


session = requests.Session()
session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, application/xml, text/xml, */*",
    }
)


def parse_json_entries(data, endpoint_label):
    entries = data.get("feed", {}).get("entry", [])
    if isinstance(entries, dict):
        entries = [entries]
    if not isinstance(entries, list):
        return []

    reviews = []
    for entry in entries:
        if "im:rating" not in entry:
            continue

        reviews.append(
            {
                "review_id": entry.get("id", {}).get("label"),
                "user_name": entry.get("author", {}).get("name", {}).get("label"),
                "rating": entry.get("im:rating", {}).get("label"),
                "title": entry.get("title", {}).get("label"),
                "content": entry.get("content", {}).get("label"),
                "app_version": entry.get("im:version", {}).get("label"),
                "updated_at": entry.get("updated", {}).get("label"),
                "vote_sum": entry.get("im:voteSum", {}).get("label"),
                "vote_count": entry.get("im:voteCount", {}).get("label"),
                "source": "App Store",
                "endpoint": endpoint_label,
            }
        )
    return reviews


def parse_xml_entries(xml_content, endpoint_label):
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError:
        return []

    ns = {
        "feed": "http://www.w3.org/2005/Atom",
        "im": "http://itunes.apple.com/rss",
    }
    entries = root.findall("feed:entry", ns)
    reviews = []

    for entry in entries:
        rating_el = entry.find("im:rating", ns)
        if rating_el is None:
            continue

        id_el = entry.find("feed:id", ns)
        author_el = entry.find("feed:author/feed:name", ns)
        title_el = entry.find("feed:title", ns)
        content_el = entry.find("feed:content", ns)
        version_el = entry.find("im:version", ns)
        updated_el = entry.find("feed:updated", ns)
        votesum_el = entry.find("im:voteSum", ns)
        votecount_el = entry.find("im:voteCount", ns)

        reviews.append(
            {
                "review_id": id_el.text if id_el is not None else None,
                "user_name": author_el.text if author_el is not None else None,
                "rating": rating_el.text if rating_el is not None else None,
                "title": title_el.text if title_el is not None else None,
                "content": content_el.text if content_el is not None else None,
                "app_version": version_el.text if version_el is not None else None,
                "updated_at": updated_el.text if updated_el is not None else None,
                "vote_sum": votesum_el.text if votesum_el is not None else None,
                "vote_count": votecount_el.text if votecount_el is not None else None,
                "source": "App Store",
                "endpoint": endpoint_label,
            }
        )
    return reviews


VIETNAMESE_MARKS = (
    "àáảãạăắằẳẵặâấầẩẫậ"
    "èéẻẽẹêếềểễệ"
    "ìíỉĩị"
    "òóỏõọôốồổỗộơớờởỡợ"
    "ùúủũụưứừửữự"
    "ỳýỷỹỵđ"
)


def detect_review_lang(content):
    if not isinstance(content, str) or not content.strip():
        return None

    text = content.lower()

    has_vietnamese_marks = any(
        ch in VIETNAMESE_MARKS for ch in text
    )

    latin_letters = sum(ch.isascii() and ch.isalpha() for ch in text)

    if has_vietnamese_marks:
        return "vi"

    return "en" if latin_letters > 0 else "vi"


def fetch_endpoint(url, fmt, label, filename_prefix):
    for attempt in range(1, MAX_REQUEST_RETRIES + 1):
        try:
            response = session.get(url, timeout=30)
            if response.status_code != 200:
                print(f"[{label}] Attempt {attempt}: HTTP {response.status_code}")
                time.sleep(1)
                continue

            if fmt == "json":
                data = response.json()
                raw_file = RAW_DATA_DIR / f"{filename_prefix}.json"
                with open(raw_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                reviews = parse_json_entries(data, label)
            else:
                raw_file = RAW_DATA_DIR / f"{filename_prefix}.xml"
                with open(raw_file, "wb") as f:
                    f.write(response.content)
                reviews = parse_xml_entries(response.content, label)

            return reviews

        except (requests.RequestException, ValueError) as e:
            print(f"[{label}] Attempt {attempt} error: {e}")
            if attempt < MAX_REQUEST_RETRIES:
                time.sleep(2 ** (attempt - 1))

    return []


def collect_all_app_store_reviews():
    endpoints = []

    base_variants = [
        ("", "default"),
        ("/sortby=mostrecent", "mostrecent"),
        ("/sortby=mostHelpful", "mostHelpful"),
    ]

    # Xây dựng danh sách endpoint cho từng storefront (vn, us)
    for storefront in STOREFRONTS:
        country = storefront["country"]
        lang_label = storefront["lang"]

        for sort_path, sort_name in base_variants:
            endpoints.append(
                {
                    "url": f"https://itunes.apple.com/{country}/rss/customerreviews/id={APP_ID}{sort_path}/json",
                    "fmt": "json",
                    "label": f"{lang_label}_top_{sort_name}_json",
                    "file": f"{country}_top_{sort_name}",
                    "lang": lang_label,
                    "country": country,
                }
            )
            endpoints.append(
                {
                    "url": f"https://itunes.apple.com/{country}/rss/customerreviews/id={APP_ID}{sort_path}/xml",
                    "fmt": "xml",
                    "label": f"{lang_label}_top_{sort_name}_xml",
                    "file": f"{country}_top_{sort_name}",
                    "lang": lang_label,
                    "country": country,
                }
            )

        for page in range(1, MAX_PAGES + 1):
            for sort_path, sort_name in base_variants:
                endpoints.append(
                    {
                        "url": f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={APP_ID}{sort_path}/json",
                        "fmt": "json",
                        "label": f"{lang_label}_page_{page}_{sort_name}_json",
                        "file": f"{country}_page_{page:02d}_{sort_name}",
                        "lang": lang_label,
                        "country": country,
                    }
                )
                endpoints.append(
                    {
                        "url": f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={APP_ID}{sort_path}/xml",
                        "fmt": "xml",
                        "label": f"{lang_label}_page_{page}_{sort_name}_xml",
                        "file": f"{country}_page_{page:02d}_{sort_name}",
                        "lang": lang_label,
                        "country": country,
                    }
                )

    all_reviews = []
    endpoint_stats = {}

    print(f"Starting collection across {len(endpoints)} endpoint combinations...")

    for idx, ep in enumerate(endpoints, 1):
        reviews = fetch_endpoint(
            url=ep["url"],
            fmt=ep["fmt"],
            label=ep["label"],
            filename_prefix=ep["file"],
        )
        endpoint_stats[ep["label"]] = len(reviews)
        if reviews:
            print(f"[{idx}/{len(endpoints)}] {ep['label']}: found {len(reviews)} reviews")
            for review in reviews:
                review["lang"] = ep["lang"]
                review["storefront"] = ep["country"]
            all_reviews.extend(reviews)

        time.sleep(REQUEST_DELAY)

    df = pd.DataFrame(all_reviews)

    print("\n======================")
    print("COLLECTION RESULTS")
    print("======================")
    print(f"Total reviews retrieved (raw): {len(df)}")

    if not df.empty:
        df = df.drop_duplicates(subset=["review_id"], keep="first")
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
        df["updated_at"] = pd.to_datetime(df["updated_at"], errors="coerce", utc=True)

        # Gán nhãn ngôn ngữ thực tế dựa trên nội dung review
        df["lang"] = df["content"].map(detect_review_lang)

        df = df.sort_values("updated_at", ascending=False).reset_index(drop=True)

    print(f"Total unique reviews after deduplication: {len(df)}")
    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== COLUMNS ===")
    print(df.columns.tolist())

    print("\n=== LANG DISTRIBUTION ===")
    if not df.empty:
        print(df["lang"].value_counts())

    print("\n=== RATING DISTRIBUTION ===")
    if not df.empty:
        print(df["rating"].value_counts().sort_index())

    print("\n=== FIRST 5 ROWS ===")
    print(df.head())

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    summary = {
        "app_id": APP_ID,
        "storefronts": [
            {"country": s["country"], "lang": s["lang"]}
            for s in STOREFRONTS
        ],
        "max_pages": MAX_PAGES,
        "total_unique_reviews": len(df),
        "endpoint_stats": {k: v for k, v in endpoint_stats.items() if v > 0},
    }

    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\nSaved reviews to: {OUTPUT_FILE}")
    print(f"Saved summary to: {SUMMARY_FILE}")


if __name__ == "__main__":
    collect_all_app_store_reviews()
