"""Classify Batch 8 (reviews 560-635) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[560:636]

CLASSIFICATIONS = {
    # [560] App Store 13994219702 - rating 1 - vague advisory + support hours
    "13994219702": {
        "incidents": [
            {"incident_type": "confusion", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "tư vấn và hợp đồng về vấn đề chuyển tiền ngân hàng và chuyển tiền bên app chứng khoán rất mập mờ nước đôi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "nhân viên chỉ làm việc trong giờ hành chính, ngoài giờ hành chính thì ko xử lý",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [561] Google Play ee06b54b - rating 1 - face scan bad
    "ee06b54b-4a02-491e-aa9d-e8d0e432e0b6": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "cái hệ thống quét khuôn mặt nguuu lôl, ko có báo động là quét dc hay chưa, quét thì 60s 4 bức",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [562] App Store 14005255766 - rating 5 - app not in user's region (content is complaint despite rating)
    "14005255766": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "APP_STORE_REGION_AVAILABILITY",
             "journey": "OTHER", "severity": "LOW",
             "evidence_span": "Phải chuyển vùng trên App Store mới tìm đc app này",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "APP_STORE_REGION_AVAILABILITY", "primary_journey": "OTHER",
        "max_severity": "LOW", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [563] App Store 14007792218 - rating 1 - app errors prevent trading
    "14007792218": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Áp rác hay lỗi đơ ko mua bán được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [564] App Store 14007797037 - rating 1 - data updates at market open
    "14007797037": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App cập nhật dữ liệu lúc thị trường mở cửa, không giao dịch được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [565] App Store 14007807831 - rating 1 - app errors frequently
    "14007807831": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App lỗi thường xuyên. Gần nhất là sáng 29/4/2026",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [566] App Store 14007814276 - rating 1 - app errors + no response
    "14007814276": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App hay bị lỗi không giao dịch được. 29/4/2026 là một ví dụ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Công ty không xin lỗi, không phản hồi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [567] App Store 14007817541 - rating 1 - trading day update causes freeze
    "14007817541": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Vào ngày giao dịch lại đi cập nhật, đơ ra, làm người ta không giao dịch gì được. Thiệt hại tính bằng tiền đó!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [568] App Store 14007818169 - rating 1 - app not updating, logs out
    "14007818169": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Sàn gì mà 29/4/26 k cập nhập, k làm việc. App hay out ra load lại",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [569] App Store 14007819853 - rating 1 - app continuously errors
    "14007819853": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App lỗi liên tục",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [570] App Store 14007820003 - rating 1 - app errors all day
    "14007820003": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App suốt ngày lỗi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [571] App Store 14007820033 - rating 1 - "lởm vl" vague insult, no specific issue
    "14007820033": {
        "incidents": [],
        "sentiment": "NEGATIVE", "complaint_present": False, "product_related": "UNCLEAR",
        "primary_family": "UNCLEAR", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "NONE", "confidence": "LOW", "needs_human_review": True,
    },
    # [572] App Store 14007823992 - rating 1 - app errors no resolution
    "14007823992": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App tệ, lỗi ko có hướng xử ly",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [573] App Store 14007825034 - rating 1 - price board errors all day
    "14007825034": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "App lỗi bảng điện suốt ngày",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [574] App Store 14007825045 - rating 2 - many errors cause trading delays
    "14007825045": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lỗi khá nhiều nhiều khi làm trễ giao dịch không đáng có",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [575] App Store 14007830108 - rating 1 - app lag affects investors
    "14007830108": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App lag , hay bị lỗi làm ảnh hưởng đến nhà đầu tư",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [576] App Store 14007834537 - rating 1 - vague insult
    "14007834537": {
        "incidents": [],
        "sentiment": "NEGATIVE", "complaint_present": False, "product_related": "UNCLEAR",
        "primary_family": "UNCLEAR", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "NONE", "confidence": "LOW", "needs_human_review": True,
    },
    # [577] App Store 14007840671 - rating 1 - maintenance during trading + app broken
    "14007840671": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Giờ giao dịch đi bảo trì Bị nhốt sàn mấy hôm, nay thoát sàn được thì app ko hoạt động",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [578] App Store 14007842869 - rating 1 - can't sell at peak
    "14007842869": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Mất tiền nhiều quá ko bán dc giá đỉnh",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [579] App Store 14007846536 - rating 1 - price board frozen + no compensation
    "14007846536": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "Bảng điện đứng im app hiện toàn bộ dữ liệu của 28/04",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Liệu TCBS sẽ có bồi hoàn gì hay chỉ là Xin Lỗi khi tiền NĐT bay theo lỗi app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [580] App Store 14007848369 - rating 1 - app and web frozen
    "14007848369": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App đơ, web đơ, rất rất tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [581] App Store 14007849446 - rating 1 - app updates at 9:15
    "14007849446": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Cập nhật gì vào lúc 9h15. Chốt lời k được luôn. Thiệt hại vậy ai chịu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [582] App Store 14007852344 - rating 1 - app crashes
    "14007852344": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App sập, đơ, k giao dịch đc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [583] App Store 14008131020 - rating 1 - app paralyzed at session open
    "14008131020": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App lỗi tê liệt ngay đầu phiên giao dịch. Bảng điện không cập nhật, không mua bán được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [584] Google Play c1af46c5 - rating 2 - app frozen at 9:20
    "c1af46c5-504f-442f-8e2c-4f62e309903d": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "9h20 rồi mà app đơ, ko làm được gì",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [585] Google Play 8a0f1c49 - rating 1 - too many errors, can't trade
    "8a0f1c49-39c8-4c33-ab1f-4df63b71e08d": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "app lởm. lỗi quá nhiều. Thậm chí ko giao dịch được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [586] Google Play 2317f654 - rating 2 - app errors cause losses + only apology
    "2317f654-d45b-4ffc-ae69-596d9a42b82a": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "app lỗi, làm thiệt hại cho nhà đầu tư, chỉ biết xin lỗi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [587] Google Play 1bf3d4bf - rating 1 - app doesn't run, not fixed
    "1bf3d4bf-56fc-4ad5-970f-221bb689be89": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "lỗi không chạy không khắc phục làm mất tiền nhà đầu tư",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [588] Google Play 1c1c432b - rating 1 - terrible app, investors locked in
    "1c1c432b-7a3e-453e-ace3-ac2044b26b70": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App tệ hại không giao dịch được, nhốt NĐT",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [589] Google Play eb3e3875 - rating 1 - app frequently errors (typo "hãy" for "hay")
    "eb3e3875-2bc9-4ce9-9808-9f937dd15a69": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "app hãy lỗi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [590] Google Play 81783439 - rating 2 - app frozen + not user-friendly
    "81783439-6012-4996-b8a6-98c18b6ab261": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "29/4 đơ luôn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "tcb nên làm lại app cho nó thân thiện, hiện đại mới mẻ chút",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [591] Google Play 560dd4ae - rating 1 - can't load data at market open
    "560dd4ae-f20b-4e06-9737-d980c73e5885": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "Không load được data khi thị trường mở cửa giao dịch",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [592] App Store 14009628721 - rating 1 - wrong price display
    "14009628721": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lỗi hiển thị sai giá ko thể mua bán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [593] Google Play 92b45d0c - rating 1 - hard to use + service delay
    "92b45d0c-73a1-46bf-9bb5-6218ab82e507": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "quả app k thể thẩm đc, khó dùng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "dịch vụ delay quá lâu",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [594] App Store 14033216115 - rating 1 - app frozen + wrong info
    "14033216115": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App bị đơ, hiển thị thông tin sai, không có ai thấy bug để fix hết hay sao ấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [595] App Store 14034900836 - rating 5 - praise for low fees
    "14034900836": {
        "incidents": [
            {"incident_type": "praise", "family": "FEE_PRICING", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "NONE",
             "evidence_span": "Phí giao dịch khi mua bán chỉ 0,03% thì quá ok rồi, ssi phí tận 0,15%",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [596] App Store 14040031598 - rating 1 - cash advance fail + transfer fail + support fail
    "14040031598": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "nđt bán cp ko ứng tiền được và lỗi chuyển tiền ra ngoài ko vào tk kh",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "khách hàng phải chat với tư vấn viên nhưng chả giải quyết đc vấn đề",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [597] App Store 14045600270 - rating 5 - "lỗi rồi" very brief (rating-content mismatch)
    "14045600270": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "lỗi 2 ngày rồi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [598] Google Play 1dbfd40c - rating 5 - vague praise
    "1dbfd40c-06ac-4217-a552-6b7b70e93f14": {
        "incidents": [
            {"incident_type": "praise", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "NONE",
             "evidence_span": "nhiều dịch vụ tiện ích cho nhà đầu tư",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "NONE", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [599] App Store 14051715882 - rating 1 - money frozen slowly after cancel
    "14051715882": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tiền phong tỏa khi hủy lệnh rất chậm trong khi lệnh hủy từ 3 4 tiếng trước",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [600] Google Play f012fc92 - rating 1 - transfer out feature error
    "f012fc92-838e-4a15-88a0-ad3ea45fe72c": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "tính năng chuyển tiền ra ngoài bị lỗi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [601] Google Play 8d63919e - rating 1 - UX extremely bad
    "8d63919e-1d1f-4fec-bd8b-be215087e6b5": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "không thể tin được 1 tập đoàn như techcom mà làm ra cái app Ux cực kì tệ",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [602] App Store 14141897416 - rating 5 - praise for good app and support
    "14141897416": {
        "incidents": [
            {"incident_type": "praise", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "NONE",
             "evidence_span": "App tốt, cskh tuyệt vời và kịp thời",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [603] Google Play 54304acd - rating 2 - UI/UX bad + server lag + notification
    "54304acd-204a-4e82-a3f2-99700570633a": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "UI/UX kém quá khó dùng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "rất nhiều lần server lag không cập nhật đúng thông tin",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "thông báo thiết bị không có internet không ẩn được, cả chục giây không đổi tab được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [604] App Store 14142865973 - rating 1 - "Chắn" single word, unclear
    "14142865973": {
        "incidents": [],
        "sentiment": "UNCLEAR", "complaint_present": False, "product_related": "UNCLEAR",
        "primary_family": "UNCLEAR", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "NONE", "confidence": "LOW", "needs_human_review": True,
    },
    # [605] App Store 14147186413 - rating 1 - advance cash limits + custody fee interest
    "14147186413": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "Chức năng \"ứng tiền trước\" giờ có giới hạn dù mình không dùng chức năng này đã lâu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "nợ phí lưu ký thì không tự động trừ tiền dù có liên kết tài khoản hay đã nạp tiền. Nợ đó cứ bị tính lãi cao lên",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [606] App Store 14149839961 - rating 1 - iPower feature disappears
    "14149839961": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Lúc cần rút tiền thì tính năng ipower bị biến mất không rút tiền được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [607] App Store 14162695649 - rating 2 - financial data inaccurate + total capital jumps
    "14162695649": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Sáng nạp 10tr, chưa mua bán gì mà tối vào không thấy tiền đâu nữa. F5 thì thấy nháy 10tr rồi biến mất",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Đến tổng số vốn cũng nhảy loạn lên, không track được lỗ lãi gì hết",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [608] App Store 14223394760 - rating 1 - app complicated, too many items
    "14223394760": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App rắc rối. Rất khó dùng. Nhiều mục không cần thiết cho nđt mà cũng chưng hết ra, rối rắm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [609] Google Play 57315b59 - rating 1 - face recognition very bad
    "57315b59-768e-4a86-bb54-4dca2ff232e6": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "Nhận diện khuôn mặt quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [610] App Store 14280577109 - rating 3 - feature request crypto deposit
    "14280577109": {
        "incidents": [
            {"incident_type": "feature_request", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "CRYPTO_DEPOSIT",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "LOW",
             "evidence_span": "có một số bitcoin nhưng app hk có tính năng nạp trực tiếp, mong là sẽ có thêm tính năng này sớm",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEUTRAL", "complaint_present": False, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "CRYPTO_DEPOSIT", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "LOW", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [611] App Store 14296658625 - rating 1 - frequent login errors
    "14296658625": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Rất thường gặp lỗi đăng nhập",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [612] Google Play ecc8fa90 - rating 4 - price board lost auto-rotate
    "ecc8fa90-86b6-40a9-9c90-a7385d972c5b": {
        "incidents": [
            {"incident_type": "friction", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "bảng giá mất tính năng tự xoay ngược khi chuyển sang dạng ngang",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [613] App Store 14313162800 - rating 1 - dividend money held until end of day
    "14313162800": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "App này chuyên giam Tiền cổ tức đợi cuối ngày hết giao dịch mới nhả Tiền ra trong khi công ty chứng khoán khác Tiền đã về để cho giao dịch trong phiên",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [614] App Store 14341132155 - rating 5 - praise for fees and widget
    "14341132155": {
        "incidents": [
            {"incident_type": "praise", "family": "FEE_PRICING", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "NONE",
             "evidence_span": "phí giao dịch ổn không quá đắt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "praise", "family": "OTHER", "subtype": "WIDGET_FEATURE",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "NONE",
             "evidence_span": "lại thêm cái widget nữa tiện quá muốn xem giá không cần vào app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [615] App Store 14352633073 - rating 1 - vague "Dịch vụ kém"
    "14352633073": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Không có nhân viên hỗ trợ. Dịch vụ kém",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [616] App Store 14352635121 - rating 1 - app errors + order placement fails
    "14352635121": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App hay bị lỗi quay vòng vòng chờ dữ liệu, rồi lâu lâu đặt lệnh thì không được rất bực mình, tỷ lệ lỗi rất nhiều",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [617] App Store 14354074084 - rating 1 - iOTP required after reinstall on same device
    "14354074084": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "xoá đi tải lại thì bắt xác nhận đăng nhập iotp trên máy đã đăng kí trc đó trong khi dùng đúng máy đó nhưng lại k cho đăng nhập vào",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [618] Google Play d372596f - rating 2 - can't access price board + wrong color
    "d372596f-4533-497c-9bb3-f0c9a37ae542": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "Tcbs đang bị lỗi, k vào dc bảng giá",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "hiển thị sai màu trong mục tài sản",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [619] App Store 14381104681 - rating 1 - can't login to withdraw
    "14381104681": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Ko đăng nhập được để rút tiền, lúc cần thì ko rút tiền được phải đi vay tiền nóng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [620] App Store 14409630266 - rating 1 - money held for closed positions
    "14409630266": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Tại sao lại giam tiền 2 hợp đồng, trong khi đã đóng vị thế trong cùng 1 ngày, các ngày khác không giam vẫn rút được bình thường chỉ trừ thuế phí",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [621] App Store 14414751396 - rating 1 - auth form doesn't display
    "14414751396": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "mỗi vào để điền thông tin xác thực thôi mà đen xì ko hiện ra 1 cái gì",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [622] App Store 14418152911 - rating 1 - rigid phone number change requires bank card
    "14418152911": {
        "incidents": [
            {"incident_type": "friction", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Phục vụ quá cứng nhắc thay số điện thoại, cccd bắt yêu cầu mở thẻ ngân hàng để xác minh thông tin",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [623] App Store 14420925724 - rating 2 - order UI messy
    "14420925724": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Nhiều tính năng mà đặt lệnh cổ phiếu rối quá, cần xem danh mục thì phải bấm tab khác",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [624] App Store 14425846977 - rating 1 - delisted companies removed from list
    "14425846977": {
        "incidents": [
            {"incident_type": "friction", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Các công ty đã rời sàn như HLG thì bị tcinvest loại luôn khỏi list, làm nhà đầu tư mất luôn thông tin số lượng cổ phiếu đang sở hữu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [625] App Store 14439296592 - rating 1 - websocket auth requires daily OTP + OTP API 500
    "14439296592": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Cứ 24 tiếng lại phải chạy vô app lấy cái OTP bằng tay xong đi cập nhật biến môi trường trước giờ giao dịch để k bị miss data. Đều đặn hằng ngày",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "tài liệu ghi cho nhận OTP qua email bằng gaia/v1/oauth2/openapi/request-otp nhưng luôn trả ra lỗi 500",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [626] Google Play ef99efd2 - rating 1 - transfer message required + 7 day hold + bot support
    "ef99efd2-9f92-42ab-8b4c-3c4e41370ef3": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "It required users to input a certain message in each transfer (your full name and account in TCBS). Even if you transfer money from your Techcombank app, but forgot to input that abovementioned info, your money goes to vague. It doesn't return to your bank account immediately, but they hold it for up to 7 working days",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "No live support, only chat (with bots), I got issue, the support in this app told me to call the bank. Me being ping-pong",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [627] App Store 14445501649 - rating 1 - iPad UI bad
    "14445501649": {
        "incidents": [
            {"incident_type": "friction", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "UI UX này hoàn toàn ko phù hợp với iPad, chắc dev lười nên bê nguyên web sang. App chạy rất bất tiện, thao tác hoàn toàn lệch, ko hề chính xác",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [628] App Store 14465018475 - rating 1 - "Nói chung quá tệ" vague
    "14465018475": {
        "incidents": [],
        "sentiment": "NEGATIVE", "complaint_present": False, "product_related": "UNCLEAR",
        "primary_family": "UNCLEAR", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "NONE", "confidence": "LOW", "needs_human_review": True,
    },
    # [629] App Store 14465859621 - rating 1 - UI/UX + hotline + no CSKH staff
    "14465859621": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "UI UX kém, dễ bị bấm nhầm mua và bán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "hotline chỉ để làm cảnh, AI trả lời tự động không giải quyết được vấn đề",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "không gọi được nv cskh, email không trả lời",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [630] App Store 14468902446 - rating 1 - data selling suspicion
    "14468902446": {
        "incidents": [
            {"incident_type": "other", "family": "SECURITY_ACCOUNT_PROTECTION", "subtype": "DATA_SELLING_SUSPICION",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Nghi vấn bán dữ liệu cho lái. Tôi cầm cổ phiếu DBC 4 tháng... Không thể có sự trùng hợp như vậy được",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "SECURITY_ACCOUNT_PROTECTION", "primary_subtype": "DATA_SELLING_SUSPICION", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [631] App Store 14504211053 - rating 3 - app very slow
    "14504211053": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Áp giao dịch gì mà chậm như rùa,mong bqt cải tiến",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [632] Google Play 7fd64ff8 - rating 1 - support slow + account unlock cumbersome
    "7fd64ff8-fbd4-4520-a656-c439f9e4443d": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Đội ngũ hỗ trợ xử lý chậm chạp, lề mề",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Tài khoản khách hàng cần mở khóa, phải chạy lên chi nhánh TCB kí giấy. Rùi phải đợi 2-3 ngày vận chuyển giấy tờ từ TCB ra TCBS chi nhánh HN. Sau đó phải đợi xử lý tờ giấy, rùi đợi 24 giờ để mở khóa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [633] App Store 14520054584 - rating 2 - app laggy
    "14520054584": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App rất lag, đôi khi còn không vào được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [634] App Store 14520064997 - rating 1 - errors showing no money/no stocks
    "14520064997": {
        "incidents": [
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Rất hay bị lỗi báo k có tiền k có cổ phiếu nào trong tài khoản",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [635] App Store 14548034358 - rating 1 - login slow + errors + IPO ads
    "14548034358": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "chỉ đăng nhập có lúc đợi cả 5p vẫn chưa đăng nhập vào trang chủ được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "vài tháng trở lại đây app lỗi rất nhiều",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "EXCESSIVE_ADS",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "quảng cáo nhiều, truy cập vào được tài khoản thì phải tắt 7749 cái quảng cáo IPO của một vài doanh nghiệp",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
}

REVIEW_COLS = [
    "source", "review_id", "review_date", "rating", "title", "review_text_raw",
    "incident_present", "incident_count", "sentiment", "complaint_present",
    "product_related", "primary_pain_point_family", "primary_pain_point_subtype",
    "primary_journey", "max_severity", "classification_confidence",
    "needs_human_review", "classification_status",
]
INCIDENT_COLS = [
    "incident_id", "source", "review_id", "incident_type", "pain_point_family",
    "pain_point_subtype", "journey", "severity", "evidence_span", "confidence",
    "new_theme_flag", "needs_human_review", "classification_status",
]

review_rows = []
incident_rows = []
completed_keys = []

for r in batch:
    rid = r["review_id"]
    src = r["source"]
    key = f"{src}|{rid}"
    cls = CLASSIFICATIONS.get(rid)
    if cls is None:
        print(f"MISSING CLASSIFICATION: {key}")
        continue
    incidents = cls["incidents"]
    incident_count = len(incidents)
    incident_present = incident_count > 0
    review_rows.append({
        "source": src,
        "review_id": rid,
        "review_date": r["review_date"],
        "rating": r["rating"],
        "title": r["title"],
        "review_text_raw": r["review_text_raw"],
        "incident_present": incident_present,
        "incident_count": incident_count,
        "sentiment": cls["sentiment"],
        "complaint_present": cls["complaint_present"],
        "product_related": cls["product_related"],
        "primary_pain_point_family": cls["primary_family"],
        "primary_pain_point_subtype": cls["primary_subtype"],
        "primary_journey": cls["primary_journey"],
        "max_severity": cls["max_severity"],
        "classification_confidence": cls["confidence"],
        "needs_human_review": cls["needs_human_review"],
        "classification_status": "PROVISIONAL",
    })
    for idx, inc in enumerate(incidents, start=1):
        safe_rid = rid.replace("/", "_").replace(" ", "_")
        incident_rows.append({
            "incident_id": f"{src.replace(' ', '_')}-{safe_rid}-{idx:02d}",
            "source": src,
            "review_id": rid,
            "incident_type": inc["incident_type"],
            "pain_point_family": inc["family"],
            "pain_point_subtype": inc["subtype"],
            "journey": inc["journey"],
            "severity": inc["severity"],
            "evidence_span": inc["evidence_span"],
            "confidence": inc["confidence"],
            "new_theme_flag": inc["new_theme_flag"],
            "needs_human_review": inc["needs_human_review"],
            "classification_status": "PROVISIONAL",
        })
    completed_keys.append(key)

with open(WORK / "reviews_classified_checkpoint.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=REVIEW_COLS)
    for row in review_rows:
        w.writerow(row)

with open(WORK / "incidents_classified_checkpoint.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=INCIDENT_COLS)
    for row in incident_rows:
        w.writerow(row)

with open(WORK / "completed_review_keys.csv", "a", encoding="utf-8") as f:
    for k in completed_keys:
        f.write(k + "\n")

with open(WORK / "classification_progress.json") as f:
    prog = json.load(f)
prog["new_semantically_classified_reviews"] += len(completed_keys)
prog["completed_total"] = prog["phase_b_reused_reviews"] + prog["new_semantically_classified_reviews"]
prog["remaining_reviews"] = prog["total_target_reviews"] - prog["completed_total"]
prog["current_batch"] = "Batch 8 (reviews 560-635)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:30:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 8 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
