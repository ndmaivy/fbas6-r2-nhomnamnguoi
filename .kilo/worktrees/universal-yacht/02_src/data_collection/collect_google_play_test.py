from google_play_scraper import reviews, Sort
import pandas as pd
from pathlib import Path

APP_ID = "com.fss.tcbs.mobiletrading"

# Project root
ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = ROOT / "01_data" / "raw" / "google_play"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "google_play_test.csv"

# Các nhóm ngôn ngữ cần thu thập (cả tiếng Việt và tiếng Anh)
LOCALES = [
    {"lang": "vi", "country": "vn", "label": "vi_vn"},
    {"lang": "en", "country": "us", "label": "en_us"},
]

COUNT_PER_LOCALE = 50


def fetch_reviews(lang, country, label):
    result, _ = reviews(
        APP_ID,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=COUNT_PER_LOCALE,
    )

    df = pd.DataFrame(result)

    if df.empty:
        return df

    df["lang"] = label
    df["source"] = "Google Play"

    return df


all_dfs = []

for locale in LOCALES:
    print(f"\n=== Fetching {locale['label']} ===")
    df_locale = fetch_reviews(
        lang=locale["lang"],
        country=locale["country"],
        label=locale["label"],
    )

    print(f"Retrieved: {len(df_locale)} reviews")

    if not df_locale.empty:
        all_dfs.append(df_locale)


if all_dfs:
    df = pd.concat(all_dfs, ignore_index=True)

    df = df.drop_duplicates(subset=["reviewId"], keep="first")

    print("\n=== SHAPE ===")
    print(df.shape)

    print("\n=== COLUMNS ===")
    print(df.columns.tolist())

    print("\n=== LANG DISTRIBUTION ===")
    print(df["lang"].value_counts())

    print("\n=== FIRST 5 ROWS ===")
    print(df.head())

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nSaved to: {OUTPUT_FILE}")

else:
    print("No reviews collected.")
