"""Classify Batch 4 (reviews 240-319) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[240:320]

CLASSIFICATIONS = {
    # [240] App Store 12780082897 - rating 5 - "Rất thân thiện" - praise
    "12780082897": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [241] App Store 12780083215 - rating 5 - praise
    "12780083215": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [242] App Store 12780083348 - rating 5 - praise
    "12780083348": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [243] Google Play 65a7938b - rating 1 - super slow money transfer
    "65a7938b-91e7-49c4-9586-4b7dd16fb679": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Giao dịch tiền siêu chậm, cho dù sử dụng tài khoản định danh của BIDV.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [244] App Store 12783588457 - rating 3 - colorful but not useful
    "12783588457": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện như bức tranh nhiều màu nhưng ít hữu dụng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [245] Google Play c61b6588 - rating 3 - phone number leak
    "c61b6588-4baa-4af9-aab9-46fb38bcaa87": {
        "incidents": [
            {"incident_type": "friction", "family": "SECURITY_ACCOUNT_PROTECTION", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "App rò rỉ sdt của mình cho các công ty chứng khoán liên quan. Từ khi mình tham gia TCBS, rất nhiều số từ cty chứng khoán gọi cho mình",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "SECURITY_ACCOUNT_PROTECTION", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [246] Google Play b48ac628 - rating 3 - good analysis but hard to trade
    "b48ac628-36a7-45dc-965d-11cb4bb71440": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Phân tích khá tốt nhưng quá khó quá bất tiện khi giao dịch. So với những app khác",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [247] App Store 12794841521 - rating 1 - 7 referral notifications in 1h
    "12794841521": {
        "incidents": [
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Sáng nay trong vòng 1h tôi nhận 7 thông báo giới thiệu bạn bè từ app. Quá phiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [248] App Store 12794864716 - rating 1 - popup harassment
    "12794864716": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Cho pop up hiện lên quấy rối người dùng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [249] App Store 12794936243 - rating 1 - ad popup blocks trading
    "12794936243": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Bó tay cái quảng cáo chèn giữa màn hình. Ko tắt đc đi để vào giao dịch",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [250] Google Play 5977fcfd - rating 1 - freeze, system errors, lost money
    "5977fcfd-e3c1-42ce-8d7b-886da40ed0b2": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "hay đơ, lỗi hệ thống... làm mất tiền của nhà đầu tư",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [251] Google Play ee25f9c0 - rating 5 - "ok tốt" - praise
    "ee25f9c0-a463-4ec0-aaf4-e7e420f53c2d": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [252] Google Play e581e069 - rating 5 - "tốt" - praise
    "e581e069-2b70-4946-b0d8-c5f81860acb0": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [253] Google Play 54676c15 - rating 1 - dividend price/PnL wrong
    "54676c15-70f9-4712-b75c-d2c578ffd7c4": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "Mỗi lần nhận cổ tức bằng cổ phiếu là cập nhật giá và lời/lỗ bị sai...cần cập nhật cho đúng...các app khác có bị vậy đâu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [254] App Store 12822763302 - rating 1 - can't sell + load fails
    "12822763302": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Ko bán đc cổ phiếu lại còn hay không load đc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [255] Google Play 147b3c4a - rating 5 - praise
    "147b3c4a-91a4-4f19-ae45-bafa16749e5a": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [256] Google Play 46fa6425 - rating 1 - OTP error
    "46fa6425-0a0f-4955-adfb-882bf8b4a5b5": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "cái app lỗi cài lại otp xuất ngày",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [257] App Store 12841961278 - rating 2 - crashes + transfer fails + trading errors
    "12841961278": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App thường xuyên sập, thường xuyên không chuyển được tiền đi, giao dịch thường xuyên lỗi, đầu tư thua lỗ một phần lớn do app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [258] App Store 12845724145 - rating 1 - order placement fails
    "12845724145": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tới giờ giao dịch mà ko đặt lệnh dc, chức năng đặt lệnh thường xuyên lỗi, cần fix gấp",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [259] Google Play 9539f50f - rating 1 - can't modify/cancel pending sell
    "9539f50f-8674-4e59-b83c-8fc781d9ae7f": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Tại sao lệnh đặt bán mặc dù chưa khớp nhưng không chỉnh giá hoặc hủy lệnh được ?",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [260] App Store 12850138790 - rating 1 - slow error handling
    "12850138790": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Tệ lỗi app xử lí vấn đề chậm sai hẹn",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [261] Google Play e26e9a86 - rating 5 - "ok" - praise
    "e26e9a86-cd65-4d0a-89c0-1b8c74dea203": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [262] Google Play a922e373 - rating 5 - feature request: more funds
    "a922e373-6084-42f3-913c-8ce9ee95dcc4": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "Nên cập nhật thêm các quỹ mở mới",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "NEUTRAL", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [263] Google Play 5d505db1 - rating 5 - praise
    "5d505db1-86d6-4d32-87bd-9f61744218c3": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [264] App Store 12889467768 - rating 2 - "Hay bị lỗi" - vague
    "12889467768": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Hay bị lỗi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [265] Google Play 8b892343 - rating 5 - Samsung A04s update breaks app
    "8b892343-a679-4ea1-86a3-2ea5826f1d1c": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "samsung a04s hôm nay cập nhật xong mở app lên không được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [266] Google Play ac9e3c09 - rating 2 - Samsung display errors
    "ac9e3c09-5c15-41a7-ad16-0d6870ccc65c": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "làm ơn mau cập nhật lại lỗi hiển thị bên samsung với, dùng bên samsung giật lỗi lung tung cả.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [267] App Store 12906141645 - rating 1 - iPhone 16 CCCD verify fails
    "12906141645": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "Iphone 16 chụp CCCD bổ sung 2-3 lần kêu mờ, không duyệt tài khoản, báo lỗi liên tục. Tạo có cái tài khoản cả tuần ko được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [268] App Store 12906434654 - rating 1 - lag, lost money
    "12906434654": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App hay lag, rất dễ mất tiền oan do giao dịch mà bảng điểm không nhảy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [269] Google Play 999bfe17 - rating 1 - board freezes at 14h
    "999bfe17-1cc0-4af3-9298-0879d22f88aa": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "App lỗi hoài, bảng điện thường xuyên đứng vào lúc 14h ko à. Chả giao dịch được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [270] Google Play 356212c3 - rating 2 - HAG price wrong
    "356212c3-56ae-4e60-8b98-63ef5bbf0d20": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "nay app hiện giá HAG sai, đang trần mà vẫn hiện giá xa bên dưới, ớn thật. may check bên app khác mới biết, haizz, check 1 ng bạn bên cạnh xài tcbs cũng bị k phải mỗi máy này nhé.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [271] Google Play 1c4966fa - rating 1 - errors + slow support
    "1c4966fa-33b1-48e4-8021-19229b4d1b5b": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app hay lỗi. xử lý chậm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "hỏi chuyên viên thì rất lâu mới phản hồi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [272] Google Play ae58a16b - rating 1 - board not viewable
    "ae58a16b-e85d-4e01-a99b-c45db6001b59": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "ngày 18/7/2025 app lỗi không xem được bảng điện",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [273] Google Play 6bcf36b7 - rating 1 - freeze during trading
    "6bcf36b7-dd16-468c-b299-bdfbda20d341": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "lúc đang giao dịch thì đơ. thế mà đòi ipo.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [274] App Store 12917524601 - rating 1 - "Thua vps" - vague
    "12917524601": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Khó dùng, vớ vẩn.",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [275] Google Play 7bd8c236 - rating 1 - bank link fails + deposit error
    "7bd8c236-a3ae-41d2-9378-90699fde22fc": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Liên kết ngân hàng không được, nộp tiền lỗi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [276] Google Play 9711f697 - rating 1 - wrong info + CSKH unreachable
    "9711f697-5d2f-4fcd-9813-75b1260ae8ce": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "thông tin sai lệch",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "cskh không liên hệ được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [277] Google Play b8566b33 - rating 1 - "Toàn lỗi" - vague
    "b8566b33-1451-4fbc-8976-a687b982c667": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Toàn lỗi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [278] Google Play d3aae568 - rating 5 - bug fixed, retract comment
    "d3aae568-9367-4dbf-b496-448046c228bc": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [279] App Store 12949107259 - rating 1 - KRX orders fail
    "12949107259": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "từ ngày có krx tôi dùng lệnh đi không được, lỗ tiền rất nhiều, sàn đi xuống quá",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [280] App Store 12949577008 - rating 1 - market price wrong
    "12949577008": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "Thị trường giảm 70đ trên app vẫn cứ giảm 25đ, làm ăn như l",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [281] Google Play 001ca837 - rating 1 - market price wrong
    "001ca837-4e45-43e9-8d71-2f75daf8c37d": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "sàn giảm 64₫ lỗi hiện giảm 25₫",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [282] Google Play cd1b84a1 - rating 1 - "thường xuyên lỗi nghiêm trọng" - vague
    "cd1b84a1-3d05-4f5c-953e-a15f48882c84": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "thường xuyên lỗi nghiêm trọng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [283] App Store 12956820659 - rating 4 - feature request: font size
    "12956820659": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "LOW",
             "evidence_span": "Cần thêm option điều chỉnh Font Size. Hiện tại mọi thứ hơi nhỏ.",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [284] App Store 12957364236 - rating 1 - "App nhiều lỗi" - vague
    "12957364236": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App nhiều lỗi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [285] Google Play 0c6855fe - rating 3 - no conditional orders + slow update
    "0c6855fe-2291-4f74-a323-1a16437e0ae8": {
        "incidents": [
            {"incident_type": "unmet_need", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Giáo diện Mobile app không có chỗ nào nhập lệnh điều kiện.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Trong phiên thì lệnh mua bán, cập nhật chậm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [286] Google Play d57d25da - rating 1 - board freeze + wrong vnindex
    "d57d25da-c591-41ba-8bb7-404395dba2c6": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "HIGH",
             "evidence_span": "tcbs trước thì bị đơ điểm, hiển thị sai vnindex giờ đơ cả bảng điện.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [287] Google Play 8bbebc69 - rating 1 - Android app crashes
    "8bbebc69-36a2-4b22-8b5c-ad1b33fca58a": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "mình dùng Android mà tự nhiên không vào được app, vào cái là bật ra luôn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [288] App Store 12964759767 - rating 1 - "App gì mà lag lộn lên" - vague
    "12964759767": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App gì mà lag lộn lên",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [289] App Store 12967217625 - rating 5 - feature request: feng shui investing
    "12967217625": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "Mình và bạn hay dùng chức năng này nhưng các bản cập nhật mới mất rồi. App thêm lại được không?",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "NEUTRAL", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [290] App Store 12970234816 - rating 2 - hard to see + CSKH + order stuck
    "12970234816": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Khó nhìn",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "khi xảy ra vấn đề k liên hệ được chăm sóc khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "xong giao dịch 1 cp vẫn ở quyền chờ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [291] App Store 12973916991 - rating 1 - limited funds
    "12973916991": {
        "incidents": [
            {"incident_type": "unmet_need", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "k có quỹ dcds. số lượng quỹ giới hạn.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [292] Google Play b77c30ef - rating 1 - app errors + Zalo support no response
    "b77c30ef-cdf4-446c-8866-f4576b3aa4fb": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App lỗi nặng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "nhắn tin trên Zalo với tài khoản chính thức của TCBS thì chỉ có một câu trả lời duy nhất là \"bọn em sẽ gửi bộ phận kiểm tra ạ\", sau gần 1 tiếng đồng hồ chẳng thấy phản hồi gì khác.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [293] App Store 12976923711 - rating 5 - praise + referral
    "12976923711": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [294] Google Play 83ed0e5c - rating 1 - "app quá tệ" - vague
    "83ed0e5c-2150-41dc-b3fd-c90abf0cb2b5": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app quá tệ. ngân hàng làm lại app đi. mất khách",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [295] Google Play 9d3c4757 - rating 1 - too many features, hard to use
    "9d3c4757-e0dc-4a44-b2db-77d87963438c": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "thêm quá nhiều chức năng nhìn rất dối mắt, khó sử dụng, khó đặt lệnh và tương tác với cổ phiếu về mặt biểu đồ. Nên đặt tối giản như SSI dễ sử dụng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [296] Google Play 502a946d - rating 5 - mixed: past complaints + now stable
    "502a946d-047d-4a91-b6fb-bec5f1702d74": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "tính năng so sánh các cổ phiếu trong chart không chạy hoặc chạy chậm. có lẽ do nhiều băng thông nên hạ tầng chưa đủ mạnh.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [297] App Store 13001326203 - rating 1 - order never matches + lag
    "13001326203": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đặt mãi không khớp lệnh. Tính năng đặt lệnh cổ phiếu không chịu sửa. Lúc nào cũng lag. Load mãi không đc cái màn xác thực otp để mua với bán.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [298] App Store 13014069107 - rating 1 - can't withdraw
    "13014069107": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "k rút tiền dc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [299] Google Play 50a1fcce - rating 1 - bad UI + staff
    "50a1fcce-0d4d-4327-a298-5625037db0c6": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "dao diện và cách làm việc của nhân viên k thể chấp nhận được",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [300] App Store 13019034835 - rating 3 - UI/UX not good
    "13019034835": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện và trải nghiệm chưa tốt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [301] Google Play cae11e9b - rating 1 - can't verify bank + AI CSKH
    "cae11e9b-ac4d-45ab-b66c-d68ac491a2d9": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "cho tiền vào đầu tư đến lúc rút tiền không cho xác thực tài khoản ngân hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "liên hệ support thì toàn chát tự động, ko có nhân viên nào hỗ trợ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [302] Google Play 155d3b62 - rating 1 - app crashes + face scan fails
    "155d3b62-41be-4179-a76e-8f742cbdb485": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Văng ứng dụng liên tục",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "quét khuôn mặt mãi không xong",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [303] App Store 13026595700 - rating 2 - face ID fails
    "13026595700": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Lỗi k xác thực được nhận diện mặt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [304] App Store 13030216864 - rating 1 - "Tắt cái cá mập thông thái đi" - feature request
    "13030216864": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "LOW",
             "evidence_span": "Tắt cái cá mập thông thái đi hộ cái",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "LOW", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [305] App Store 13031609527 - rating 2 - end-of-day summary wrong
    "13031609527": {
        "incidents": [
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "Tổng kết cuối ngày với tiền có thể rút lỗi mãi không về",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [306] Google Play 2b1536a4 - rating 2 - QR scan fails
    "2b1536a4-de79-44b5-b2b4-a217dc6f2f58": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "có cái mã qr quét quài k đc, trong khi dùng cam hay zalo cũng quét rất nhanh",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [307] Google Play f995581a - rating 1 - can't view portfolio at sensitive time
    "f995581a-ff5f-4e8b-9c1b-d4bdb6e4f358": {
        "incidents": [
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "ko xem được danh mục đúng thời điểm nhạy cảm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [308] Google Play 7d080e2e - rating 1 - system slow
    "7d080e2e-d5a0-417d-b55b-4f9983564e1a": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "hệ thống chậm lag, khuyến khích không nên sử dụng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [309] App Store 13042326473 - rating 1 - app freeze, can't enter
    "13042326473": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App bị đơ, chậm, ko vào được, tính năng nào quay tít ko thực hiện được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [310] Google Play b609fa25 - rating 2 - maintenance extends, can't withdraw
    "b609fa25-6d85-46b4-8720-56643d279d58": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "báo thời hạn bảo trì hệ thống từ 4h chiều tới 9h tối nhưng sang tới hôm sau vẫn chưa rút được tiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [311] Google Play 6596fcf6 - rating 1 - no auto-logout (security)
    "6596fcf6-7202-40da-88bf-269137261297": {
        "incidents": [
            {"incident_type": "failure", "family": "SECURITY_ACCOUNT_PROTECTION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "áp không có chức năng tự đăng xuất khi tắt ứng dụng . rất nguy hiểm lần đầu mới thấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "SECURITY_ACCOUNT_PROTECTION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [312] Google Play 07183d25 - rating 1 - CCCD verify 2h fails + AI CSKH
    "07183d25-1b92-47d6-ab32-671c340e631d": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "Bắt khách hàng xác thực cccd, mà mất gần 2h chụp cccd mới, rồi chụp cmnd cũ, vẫn không thành công.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Gọi tổng đài thì gặp AI không trả lời được gì, người bên tcbs chắc bị đuổi hết rồi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [313] App Store 13068775356 - rating 1 - XS Max fingerprint option
    "13068775356": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "Đăng nhập trên XS Max lại hiện option vân tay, nghĩ nó chán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [314] App Store 13070665657 - rating 1 - poor support + money deducted wrong
    "13070665657": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Hỗ trợ kém, nhân viên giải thích lung tung, tiền trừ linh tinh nhân viên không tính ra nổi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [315] App Store 13090389353 - rating 2 - hard to open order book
    "13090389353": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Mỗi lần mở sổ lệnh tôi gặp khó khăn.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [316] Google Play 0c72abc6 - rating 1 - password recovery process too complex
    "0c72abc6-c487-4e1d-9bc8-9d341dfdd982": {
        "incidents": [
            {"incident_type": "friction", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Mình đã có trải nghiệm rất tệ, khi thay đổi mật khẩu và mất máy. quy trình thủ tục cấp lại quá rườm rà, phức tạp. Gọi tổng đài, ko giải quyết được, chỉ ra phòng giao dịch ngân hàng hỗ trợ, ra chi nhánh ngân hàng lại gọi lên tổng đài đề nghị hỗ trợ. 2-3 h đồng hồ ko cấp lại mật khẩu giao dịch cho khách được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [317] App Store 13096390346 - rating 1 - app auto-closes after 10s
    "13096390346": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App bị lỗi mở ra khoảng 10s là app tự đóng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [318] Google Play 28fbcc6b - rating 1 - "lỗi vào k hiện gì cả" - vague
    "28fbcc6b-2251-4028-bdb3-09111f7c0258": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "lỗi vào k hiện gì cả chán",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [319] App Store 13100499865 - rating 3 - Mac Air M1 stuck at splash
    "13100499865": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Mac Air M1 không mở được app, bị đứng ở splash screen",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
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
prog["current_batch"] = "Batch 4 (reviews 240-319)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:10:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 4 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
