"""Classify Batch 2 (reviews 80-159) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[80:160]

CLASSIFICATIONS = {
    # [80] Google Play 7e64ea2c - rating 5 - "Tốt" - generic praise
    "7e64ea2c-b419-4846-adbc-7fb6e7f32d37": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [81] Google Play 87571d07 - rating 1 - slow trading
    "87571d07-a777-45e4-9a77-f0456fb86077": {
        "incidents": [
            {"incident_type": "friction", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App về tài chính mà giao dịch chậm còn lát nữa lỗ với nó biết nhiêu tức nữa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [82] App Store 12189754220 - rating 1 - order errors + balance not shown
    "12189754220": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Toàn lỗi không đặt được lệnh.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Nhiều khi đến tài khoản cũng không hiển thị.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [83] Google Play 0fcb0828 - rating 1 - new UI bad + balance always shown + deep nav
    "0fcb0828-d856-4321-8bc3-2de4dc7e9c97": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện app mới quá tệ, tiền trên app không bật tắt hiện thị được, cứ phô phô ra cho người khác chẳng may thấy được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Để xem cái bảng giá cổ phiếu mà ấn rõ nhiều thao tác để vào: Đầu tư--> Cổ phiếu--> Bảng giá.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [84] Google Play bd974c97 - rating 1 - vague insult
    "bd974c97-210a-4d21-b82a-061dcf6f9d90": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "ANNALEEJ. TƯỞNG HAY NHƯNG CŨNG TẠM ĐƯỢC.RẤT TỆ.",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [85] Google Play f3452f5c - rating 1 - blocks withdrawal
    "f3452f5c-9b63-415a-919b-3b9c959a9a36": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "tự chặn không khách hàng rút tiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [86] Google Play 361acf1b - rating 1 - revert to old version
    "361acf1b-88b1-48b5-bddc-8ad9f98e0eca": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Quá tệ. Làm ơn trở lại phiên bản cũ hoặc mất khách",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [87] Google Play dd9d816b - rating 1 - new version can't see P/L over time
    "dd9d816b-8331-4ba5-94e8-093407351930": {
        "incidents": [
            {"incident_type": "friction", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "Phiên bảng mới không xem được tổng tiền lời lỗ trong thời gian dài",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [88] Google Play 96d7b06e - rating 2 - can't find buy/sell + asset overview
    "96d7b06e-56b8-42af-8a8e-9f3770f1d970": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tìm mãi không thấy phím Mua - Bán.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "Không lên tổng quan tài sản",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [89] App Store 12219869008 - rating 4 - lag near close + asset stats inaccurate
    "12219869008": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Hay bị lag phi đóng phiên",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "thống kê tài sản không chính xác (mấy bản cập nhật gần đây bị)",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [90] Google Play bdc43597 - rating 1 - can't login after signup + CSKH bot
    "bdc43597-7227-4f14-a0f8-c8eba93ef177": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Sau khi tạo tài khoản thì không cho đăng nhập nữa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Liên hệ CSKH thì nói chuyện như bot, không có chuyên môn, qua loa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [91] Google Play 5f211f78 - rating 1 - trading frozen before close
    "5f211f78-6e87-45cf-85b0-37a09898ad22": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "chưa phải ngày cuối mà giao dịch treo không làm gì được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [92] App Store 12223647522 - rating 1 - portfolio prices not updated
    "12223647522": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Hnay là 24 rồi mà giá vẫn lấy ngày 22.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [93] Google Play bafa4c19 - rating 1 - new version worse
    "bafa4c19-4760-4299-b62a-867de951e07e": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "tự nhiên up ver. kém hơn cả ver trước. tệ hại vãi chưởng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [94] Google Play 32e58255 - rating 1 - messy UI, features hidden
    "32e58255-2e2f-4050-b054-13857c73aa95": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giáo diện rối, khó dùng. Dùng mấy năm rồi vẫn chưa quen. Những tính năng hay dùng thì cứ ẩn sâu tít ở đâu.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [95] Google Play 29fe0daf - rating 5 - "Ok" - generic praise
    "29fe0daf-fc2a-41bc-b751-a5e3b93289ce": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [96] Google Play b688ac8c - rating 1 - "Tệ" - vague
    "b688ac8c-082a-4976-8c70-99f9430abc75": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "Tệ",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [97] App Store 12272742831 - rating 1 - prices not updated
    "12272742831": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "app ko cập nhật giá trong danh sách cổ phiếu. đã thử xoá cache, gỡ app cài lại vẫn bị vậy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [98] Google Play eb14734e - rating 2 - new update uses old data for trading
    "eb14734e-ab13-43dd-bb29-ef1dc0fe53b5": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Bản cập nhật mới lỗi khá nhiều việc mua bán mà ở phần cổ phiếu dùng dữ liệu cũ k update việc mua bán giá tb và khối lượng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [99] Google Play 4d999c16 - rating 1 - super slow price/money update
    "4d999c16-c914-4907-9e7a-d026d3bf7959": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "Cập nhật siêu chậm giá & tiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [100] Google Play ad76edd9 - rating 1 - QR login fails + popups
    "ad76edd9-a952-4969-8e45-ef221d81f18b": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Ko quét đc QR để đăng nhập trên máy tính.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Nhiềi popup tắt đi rồi vẫn hiện",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [101] App Store 12276846294 - rating 2 - new UI ugly + too much ads
    "12276846294": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App giao diện mới xấu, không thân thiện, chức năng Trang Chủ quảng cáo Ibond, Trái Phiếu,TCBS nhiều!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [102] Google Play 85397d16 - rating 2 - update lag + sell not reflected + popups
    "85397d16-df0b-4874-8800-0c0ae762fc78": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Cập nhật hồi đầu tuần làm ứng dụng lag giật nhiều hơn, load số tiền trên các trang chậm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "Lệnh bán rồi nhưbg vào danh sách cổ phiếu vẫn chưa cập nhật.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Các popup chồng chéo.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [103] Google Play 01e975f4 - rating 2 - update bad, slow
    "01e975f4-5aa8-4faf-b486-40c742040df8": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Update bản quá tệ, chậm, khó theo dõi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [104] Google Play 1134856f - rating 1 - sell UI made slower
    "1134856f-d768-4db4-bca4-a8c71a18bdc3": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Giao diên đặt bán như shirt. Như cũ đặt nhanh tự nhiên sửa cho chậm, làm lằng nhà lằng nhằng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [105] Google Play 1f9a3b08 - rating 1 - no odd-lot price view
    "1f9a3b08-c3ca-4b1c-aac2-52a4c15b915f": {
        "incidents": [
            {"incident_type": "unmet_need", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "App cập nhật hoài mà không có tính năng xem giá lô lẻ . Thua xa mấy app của yuanta .",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [106] Google Play e775c6ff - rating 1 - face scan camera black
    "e775c6ff-c6da-4115-bf43-72d5e4246237": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Quét khuôn mặt. Camera đen ngòm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [107] Google Play 33532f4d - rating 1 - app error, can't enter
    "33532f4d-bf89-4a0b-9a75-8915051ba05b": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App lỗi , ko vào được nữa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [108] Google Play e782edc9 - rating 1 - Samsung S9+ incompatible
    "e782edc9-35e9-4c3d-a0a1-bd567bac84e4": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Không tương thích samsung s9 plus",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [109] App Store 12301648806 - rating 1 - transfer errors + chat not handled
    "12301648806": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Hay bị lỗi chuyển tiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "nhắn tin không xử lý",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [110] App Store 12308962875 - rating 1 - new UI lag, hard to use
    "12308962875": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "giao diện mới rất lag khó dùng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [111] App Store 12316968970 - rating 4 - Face ID fails on iPhone 11
    "12316968970": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Không đăng nhập được bằng Face ID trên iPhone 11.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [112] App Store 12338671343 - rating 5 - praise + referral
    "12338671343": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [113] Google Play 4b3c680c - rating 1 - English: worst security, bad UI/UX
    "4b3c680c-14f7-44c1-8af3-2e40c1b2080b": {
        "incidents": [
            {"incident_type": "friction", "family": "SECURITY_ACCOUNT_PROTECTION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Worst security app I ever use.",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "The UI an UX terrible, there are many features which unnecessary make it hard to navigate.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "SECURITY_ACCOUNT_PROTECTION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [114] Google Play d4a6fbeb - rating 3 - chart not shown + slow withdrawal
    "d4a6fbeb-f903-4aea-bd78-0ba65cdf6475": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Gần đây có lỗi không hiển thị đồ thị.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "Ngoài ra còn vấn đề rút tiền về ngân hàng rất lâu nếu không phải trong giờ hành chính và trước 3h chiều.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [115] Google Play 5dd0f3f0 - rating 1 - can't login on Note 8
    "5dd0f3f0-4aa9-473c-9c6f-ac1a156c50b6": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "T không đăng nhập được trên note 8",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [116] App Store 12356932020 - rating 1 - vague scam warning
    "12356932020": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "MEDIUM",
             "evidence_span": "Thằng nào viết cái app này vậy, cảnh cáo bà con đừng tham gia vào chứng khoán này, vào là mất tiền oan",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [117] Google Play 76863788 - rating 2 - chart data lost on refresh
    "76863788-9174-44ee-8fe8-58c3a8de568a": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "App thường xuyên mất dữ liệu chart. Đã lưu nhưng khi refresh hoặc mở lại thì các dữ liệu mất sạch.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [118] Google Play 74be1267 - rating 1 - spinning, can't login
    "74be1267-4cc5-42d7-ad3d-6a7fc5212b86": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Quay như chong chóng, k đăng nhập được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [119] App Store 12379946562 - rating 1 - can't place orders
    "12379946562": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Thường xuyên ko bấm đặt đc lệnh",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [120] App Store 12381075336 - rating 1 - new update worse than old
    "12381075336": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App cập nhật xong ko bằng bản cũ",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [121] Google Play 358c0507 - rating 1 - foreign investor discrimination
    "358c0507-777c-44ad-8896-175af5430bef": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "kể cả nộp rút tiền là chuyện cực kỳ phức tạp",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [122] App Store 12383638403 - rating 1 - too many products, messy
    "12383638403": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Quá lằng nhằng. Giao diện quá nhiều sản phẩm. Dùng rất rối",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [123] Google Play 16835a35 - rating 1 - lag
    "16835a35-1489-424d-bcde-3cb4a920437f": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App dùng quá chán, lag kinh hồn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [124] Google Play 026a0327 - rating 1 - black screen on open
    "026a0327-c0c2-4b22-acfe-57fd88cda69c": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Sáng mở ra đen thui",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [125] Google Play 50aa6a09 - rating 3 - widget slower than market
    "50aa6a09-82ff-4319-8fe0-30cb076ef201": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Widget đôi lúc chậm hơn bảng giá thị trường ở đầu ngày",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [126] Google Play 91df02d7 - rating 1 - "Nhiêu đủ hiểu" - vague
    "91df02d7-4a22-4127-b7f6-dcafe29cf228": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "Nhiêu đủ hiểu",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "UNCLEAR", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [127] Google Play c2b39805 - rating 5 - mixed: referral + order UI complaints
    "c2b39805-cd67-4dff-880a-993b55348bc5": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Đặt lệnh không hiện thị bước giá hiện tại mua bán, không có nút mua bán ấn nhanh để đơn giản hóa mà cứ nhập bằng tay, không hiển thị thông tin lượng cp đang nắm giữ khi đặt lệnh bán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [128] App Store 12400663065 - rating 2 - "Ko rút dk" - can't withdraw
    "12400663065": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Ko rút dk",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [129] App Store 12403217122 - rating 1 - auto-selects market + hard to use
    "12403217122": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tự chọn mp khi bán, may mà huỷ lệnh kịp, định lùa gà người mới hay gì",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App khó dùng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [130] Google Play 536055f4 - rating 1 - onboarding stuck at step 2/8
    "536055f4-505e-4ac4-8f4a-72d68e4e34d7": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "Vào đến bước 2/8 bấm tiếp tục không chạy tiếp",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [131] App Store 12406839316 - rating 1 - hard to match orders
    "12406839316": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Chỉnh đủ giá k khớp nổi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [132] Google Play 1fbfc074 - rating 1 - 2.5% fee missing
    "1fbfc074-a707-4bea-bc45-78e494045b90": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Bán cp xong tiền mất 2,5% k bit đi đâu. Ăn cắp tài sản của nđt",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [133] Google Play dbc9e7e8 - rating 1 - need sell confirmation
    "dbc9e7e8-0a13-4b9b-bc58-8d2f8578b336": {
        "incidents": [
            {"incident_type": "feature_request", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Cần thêm câu hỏi xác nhận bán trong phần bán cổ phiếu, lỡ đụng nhầm lại bán mất cp",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [134] Google Play ca0eb48c - rating 1 - "nice" - sarcastic? unclear
    "ca0eb48c-8b0d-4c50-9638-b4ec1a4b3450": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "nice",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "UNCLEAR", "complaint_present": False, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [135] App Store 12434867625 - rating 1 - "Làm ăn ko ra gì" - vague
    "12434867625": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "Làm ăn ko ra gì",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [136] Google Play 0cb89c47 - rating 1 - "Rút tiền văn vở" - withdrawal bureaucratic
    "0cb89c47-1f24-4236-8945-8b3ec3fa48c5": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "Rút tiền văn vở",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [137] Google Play b5e796ac - rating 1 - bloated UX, too many steps
    "b5e796ac-6ba4-4b9f-9274-54fc174ecc1d": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App cồng kềnh, ôm đồm quá, UX quá tệ, cần quá nhiều thao tác để truy cập vào các tính năng thường dùng như bảng giá thị trường, bảng giá từng cổ phiếu.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [138] App Store 12442692786 - rating 4 - new version no floor/ceiling shown
    "12442692786": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Đặt lệnh mà k thấy thấy giá sàn giá trần như version trước đấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [139] App Store 12453957660 - rating 1 - holds money + messy UI
    "12453957660": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Tcbs giam tiền của khách hàng. Rút tiền chiều thứ 6 trong giờ giao dịch mà qua giữa tuần tiền mới về tài khoản.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "giao diện apps rối rắm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [140] App Store 12469670827 - rating 1 - UI issues, can't find cancel order
    "12469670827": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Giao diện khó sử dụng. Không tìm thấy lệnh quỹ để huỷ, lỡ mất cơ hội đầu tư.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Dặt lệnh cũng k có thông báo",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [141] App Store 12472251645 - rating 4 - feature request: margin from stock profit
    "12472251645": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "LOW",
             "evidence_span": "Nên thêm chế độ nở sức mua từ lãi cổ phiếu qua ngày mà không cần bán cổ phiếu đi.",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "NEUTRAL", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [142] Google Play 25873253 - rating 5 - "tốt mua được lô lẻ" - praise
    "25873253-f0a8-4833-b69b-46ae0437edce": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [143] Google Play 69e032e8 - rating 1 - forced digital signature
    "69e032e8-f43d-4833-8705-f22ecd0a5e13": {
        "incidents": [
            {"incident_type": "friction", "family": "DIGITAL_SIGNATURE_FLOW", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "Bắt mau chứ ký số không dùng được chứ số bên khác.",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DIGITAL_SIGNATURE_FLOW", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [144] Google Play c78ae7d3 - rating 1 - chatbot doesn't understand
    "c78ae7d3-8dd7-4bed-9baa-dd43ba572437": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Hỗ trợ bằng Chat bot không hiểu vấn đề !",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [145] App Store 12500908724 - rating 1 - can't find order placement
    "12500908724": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tìm mòn mỏi không biết đặt lệnh, sửa lệnh hay huỷ lệnh ở đâu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [146] App Store 12501658993 - rating 1 - transfer shows money but can't buy
    "12501658993": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Chuyển tức app tech sang xong hiện tiền nhưng không cho mua",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [147] Google Play 141e2e86 - rating 1 - English: too much info, no price history
    "141e2e86-446d-46b8-a5e1-5f7093297698": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Too much unnecessary information and function in app but lack of price information, matched price history. Not well looking. Can't sweep left, right to move",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [148] App Store 12518940042 - rating 1 - high fees, auto-deduct
    "12518940042": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "lãi cao ngất ngửa tự ý trừ tiền tk teck",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [149] App Store 12524144104 - rating 5 - praise + referral
    "12524144104": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [150] App Store 12524834794 - rating 1 - super lag
    "12524834794": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App lag kinh khủng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [151] App Store 12524926430 - rating 1 - unstable, can't access
    "12524926430": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App hoạt động không ổn định, thường xuyên không thể truy cập được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [152] Google Play 68af5174 - rating 1 - app freeze, can't place order
    "68af5174-d1ec-401b-b2bd-d8ce6dd37e63": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "app đơ ko đặt lệnh dc quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [153] Google Play b61f8012 - rating 1 - lag and slow
    "b61f8012-1467-4c37-91ec-91cd2a3f1334": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Ứng dụng cùi bắp, vừa đơ vừa chậm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [154] Google Play 73a77237 - rating 1 - "App dùng khó chịu thật sự" - vague
    "73a77237-f86a-461e-8521-e5fa69cb0f09": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App dùng khó chịu thật sự",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [155] Google Play e401a5a6 - rating 1 - OTP not sent, missed opportunities
    "e401a5a6-315b-4364-9d9d-ec321b9cf6e2": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "không thể giao dịch được trong nhiều ngày liền. mã otp k gửi đến máy. tôi đã lỡ rất nhiều cơ hội chỉ vì chuyện này.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [156] App Store 12526738886 - rating 3 - new version hard to place orders
    "12526738886": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Phiên bản mới khó đặt lệnh , không thuận tiện như phiên bản trước đây",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [157] Google Play 05fd7c56 - rating 1 - new version missing features
    "05fd7c56-b935-45dc-a6ba-b048212f19b4": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "app quá tệ, ko như bản cũ, bước giá, khối lượng giao dịch, mua nhanh ko thấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [158] App Store 12526882408 - rating 4 - Mac M1 broken
    "12526882408": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Không mở được bằng Mac M1 nữa, mở lên chỉ thấy slogan Đầu tư an toàn, Cuộc sống an nhàn, xong đơ.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [159] App Store 12527068142 - rating 1 - hard to track prices when trading
    "12527068142": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Khi muốn mua nhanh từ bảng điện hoặc theo dõi giá và khối lượng khi mua bán khó. Chưa tối ưu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
}

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
    w = csv.DictWriter(f, fieldnames=list(review_rows[0].keys()))
    for row in review_rows:
        w.writerow(row)

with open(WORK / "incidents_classified_checkpoint.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(incident_rows[0].keys()))
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
prog["current_batch"] = "Batch 2 (reviews 80-159)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:00:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 2 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
