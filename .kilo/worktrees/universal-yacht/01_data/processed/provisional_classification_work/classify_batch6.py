"""Classify Batch 6 (reviews 400-479) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[400:480]

CLASSIFICATIONS = {
    # [400] App Store 13411715829 - rating 1 - "App tài chính mà văng miết"
    "13411715829": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App tài chính mà văng miết",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },  # noqa
    # [401] Google Play 7a4db707 - rating 1 - app incompatible with phone
    "7a4db707-140f-4bb4-b0fe-78ae4d28947d": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Ứng dụng không tương thích với điện thoại. Trong khi ứng dụng của các công ty khác thì cài đặt bình thường.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [402] Google Play ba264218 - rating 1 - too many features, lag
    "ba264218-c50e-4782-8d78-0f45dfcdb703": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App quá nhiều thứ không cần thiết, nên làm đơn giản lại, nếu muốn ôm đòm thì tách ra từng mô đun ai cần thì tải thêm về không cần thì thôi, làm cho gọn nhẹ lại. làm cho chạy nhanh hơn được k. cứ lag lag sao đó.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [403] App Store 13416185136 - rating 1 - "Lừa đảo" + "Cẩn thận mất tiền"
    "13416185136": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "MEDIUM",
             "evidence_span": "Lừa đảo. Cẩn thận mất tiền nhé mn",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [404] Google Play c4dd35a4 - rating 1 - slow + complex UI/UX
    "c4dd35a4-3571-4934-ac95-83360c34caad": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App tệ hại vô cùng. Load chậm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "UI/UX phức tạp.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [405] App Store 13445903889 - rating 1 - AI support ineffective
    "13445903889": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Bộ phận hỗ trợ là AI hoạt động không hiệu quả. Chỉ dẫn theo các link có sẵn nhưng vẫn không giải quyết được vấn đề.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [406] Google Play 2515d2e9 - rating 1 - margin money deducted to 0 + AI CSKH
    "2515d2e9-0d05-4861-9ad3-f5421f64e9af": {
        "incidents": [
            {"incident_type": "failure", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Tiền bán cổ phiếu trong tài khoản ký quỹ bị trừ về 0 mà không có bất kỳ thông báo nào. Không biết tiền bị hạch toán vào đâu?",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Liên hệ thì tổng đài toàn tự động trả lời, không giải quyết được vấn đề, kêu tổng đài viên đều bận qua Zalo, FB chat toàn gặp AI cũng không giải quyết được vấn đề KH gặp phải.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [407] Google Play a335448b - rating 1 - identity verify fails
    "a335448b-6d67-4c3f-a486-5443d514c972": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "chụp ảnh xác minh danh tính hoài mà không được, hoàn thành rồi xong lại báo lỗi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [408] Google Play 52ce58b5 - rating 1 - lag, can't enter
    "52ce58b5-e1df-4171-8943-832ed805219a": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "lag k vào dc app để giao dịch",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [409] App Store 13476352525 - rating 2 - freeze when need to sell + AI CSKH
    "13476352525": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "khi nào cần bán là nó đơ và k vào đc app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "trừ tiền ko minh bạch",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "gọi tổng đài thì toàn Ai nói chuyện, đẩy sang chát zalo face cũng dí AI trả lời",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": True,
    },
    # [410] Google Play e1c2a515 - rating 1 - "app toàn bị đơ"
    "e1c2a515-9df2-4f7e-acc6-3ae5e2f83ffa": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "app toàn bị đơ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [411] App Store 13500073382 - rating 2 - chart not fullscreen
    "13500073382": {
        "incidents": [
            {"incident_type": "friction", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Biểu đồ kỹ thuật chỉ cho xem theo hình dọc hoặc quay ngang thì không được full màn xem rất khó chịu.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [412] App Store 13503906778 - rating 1 - messy, complex, lag
    "13503906778": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App rối mắt, phức tạp, lag, khó sử dụng, ngu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [413] Google Play 19c34675 - rating 5 - praise
    "19c34675-e704-4e7f-8680-1de52c8c668a": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [414] Google Play dc63badd - rating 1 - end-of-day data delayed
    "dc63badd-1778-4fcf-b23d-17caddbd2e1b": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "HIGH",
             "evidence_span": "dữ liệu cuối ngày lúc nào cũng trễ, ảnh hưởng công việc của nhà đầu tư..bực lắm luôn!!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [415] App Store 13534569635 - rating 5 - praise free trading
    "13534569635": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [416] App Store 13541334311 - rating 2 - hard to use, no floor/ceiling
    "13541334311": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "App siêu khó dùng so với các app chứng khoán khác. Giao diện chán không thuận tiện. Lúc đặt lệnh mua cổ phiếu không nhìn được giá trần và giá sàn ở đâu!!!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [417] App Store 13549003693 - rating 3 - all-in-one but lag
    "13549003693": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App kiểu all in one, giao dịch cổ phiếu, trái phiếu, chứng chỉ quỹ.. đầy đủ nhưng khá là lag, khiến người dùng đôi lúc khá bực mình",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [418] App Store 13572114993 - rating 1 - strict deposit verification
    "13572114993": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "Phần nộp tiền vào mà khắt khe việc xác minh, ko hiểu lí do để làm gì",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [419] App Store 13572173414 - rating 1 - bad CSKH attitude
    "13572173414": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Thái độ nhân viên chăm sóc khách hàng quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [420] App Store 13593563203 - rating 1 - production performance issue
    "13593563203": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "2025 rồi mà còn để performance issue xảy ra ngay trên production khiến bao nhiêu khách ko đặt lệnh mua hay bán gì được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [421] Google Play 76d860a2 - rating 1 - disgusting app, AI support
    "76d860a2-c516-4fa6-94b3-ef2c7a2daed5": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "thật là 1 ứng dụng kinh tởm. Ba bữa lại lỗi, hỗ trợ thì dùng AI giao dịch, xử lý chậm chạp. Giao dịch CK mà chờ sửa lỗi vài ngày.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [422] App Store 13612239839 - rating 1 - errors, freeze
    "13612239839": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lỗi , đơ giật khi sử dụng rất nhiều. Toàn lỗi không giao dịch được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [423] App Store 13628373156 - rating 1 - ugly UI, complex login
    "13628373156": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "App giao diện xấu, rất khó hiểu, quy trình đăng nhập rườm rà gây trải nghiệm người dùng ko tốt. Nên thuê UX designer xây lại app giống app Techcombank",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [424] Google Play ae9cebc0 - rating 1 - "giao diện, chức năng loạn cào cào"
    "ae9cebc0-a50c-4564-9ac3-44f281f31e39": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "giao diện, chức năng loạn cào cào",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [425] App Store 13630861870 - rating 3 - lag + can't cancel order
    "13630861870": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "App hay đơ lag",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Nhiều lúc đặt lệnh xong k huỷ được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [426] App Store 13630882706 - rating 1 - errors during important sessions
    "13630882706": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "lúc quan trọng hay có biến là nó lỗi đúng lúc, làm thiệt hại bao nhiêu tiền của khách",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [427] App Store 13630917569 - rating 1 - order freeze, can't sell
    "13630917569": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Ứng dụng tệ hại, cứ treo lệnh không bán được gây thiệt hại lớn cho nđt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [428] App Store 13630935825 - rating 1 - 14/1 9h30 freeze
    "13630935825": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "9h30 ngày 14/1 đơ lag đặt lệnh ko mua ko được, huỷ ko được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [429] App Store 13630942957 - rating 1 - order placed but not matched, can't edit
    "13630942957": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App lỗi, từ sáng tới giờ đặt xong không khớp cũng không sửa được lệnh",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [430] App Store 13630943735 - rating 1 - update during session breaks trading
    "13630943735": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đặt lệnh mua bán trong phiên nhưng trạng thái giao dịch chỉ là \"đã đặt\", không chuyển qua \"chờ khớp\"? Không sửa, huỷ lệnh được!?!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [431] App Store 13630945627 - rating 2 - update during trading hours
    "13630945627": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đến giờ giao dịch thì lỗi ko đặt lệnh hay xoá sửa được. Hệ thống thì nói cập nhật dữ liệu nên bị lỗi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [432] App Store 13630947432 - rating 1 - order edit fails all morning
    "13630947432": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App lỗi sửa lệnh cả buổi sáng mãi không xong, ảnh hưởng tới giao dịch của khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [433] App Store 13630948771 - rating 1 - 1+ hour error, no response
    "13630948771": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đang lỗi không giao dịch được, hãy sử lý và có lời giải thích thoả đáng. Lỗi hơn 1 tiếng chưa có trả lời khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [434] App Store 13630951162 - rating 1 - can't cancel/edit during volatility
    "13630951162": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App rất hay lỗi nhé. Lúc cần huỷ lệnh sửa giá là không làm được. Hỏi nhân viên báo là hệ thống đang cập nhật gì đó. Lỡ giờ để mua bán khi giá tăng hay tụt đột ngột.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [435] App Store 13630959017 - rating 1 - 10am can't match/edit/cancel
    "13630959017": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Nghĩ sao 10h sáng đặt lệnh ko cho khớp ko cho sửa ko cho huỷ? App lớn mà lỗi vậy?",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [436] App Store 13630959308 - rating 1 - English: orders not reaching exchange
    "13630959308": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Orders not reaching the Exchange. Please inspect, fix, and upgrade the App immediately",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [437] App Store 13630970402 - rating 1 - order system often freezes
    "13630970402": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Hệ thống đặt lệnh hay bị đơ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [438] App Store 13631009444 - rating 1 - high risk, AI support
    "13631009444": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "lỗi app thì liên tục mà xử lí lỗi thì lâu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "gọi điện AI trả lời, hậu quả thì ndt chịu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [439] App Store 13631386662 - rating 3 - freeze + chart load fails on volatile days
    "13631386662": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "trong những ngày biến động thường treo lệnh, biểu đồ load không nổi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [440] Google Play 9860f804 - rating 1 - can't buy when stock rises
    "9860f804-3c41-4833-8e96-6b2549b7a919": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lúc cp tăng thì đặt lệnh mua ko đc. Không cho hủy.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [441] Google Play 3d2ccb13 - rating 1 - "app chuyên lỗi k đặt đc lệnh"
    "3d2ccb13-239e-46a6-9f78-90021bbeeeed": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "app chuyên lỗi k đặt đc lệnh k nên dùng công ty này",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [442] Google Play 6ea0461e - rating 1 - frequent errors
    "6ea0461e-6beb-4da6-b23b-5e93231b3c15": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App thường xuyên lỗi không giao dịch được, không bao giờ dùng app này nữa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [443] Google Play cd546886 - rating 1 - update during trading
    "cd546886-d870-42ac-b667-23f16adc7038": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Apps chuyên đơ và lỗi. Hỏi thì được trả lời là cập nhật hệ thống, mà toàn canh lúc đang giao dịch thì cập nhật.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [444] Google Play 547f969e - rating 1 - "quá tệ mất rất nhiều tiền"
    "547f969e-0676-4e7d-a158-d1c32569d075": {
        "incidents": [
            {"incident_type": "friction", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "quá tệ mất rất nhiều tiền của khách hàng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [445] Google Play 29e01899 - rating 1 - can't place/cancel + no CSKH + high margin
    "29e01899-efa2-4546-8421-6b2abf4bf775": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "không đặt lệnh hủy lệnh dc.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Không có cshk xử lý lỗi, không thông báo coi thường kh.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Mg cao ngất, thích call là call, phí có rẻ cũng tẩy chay",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": True,
    },
    # [446] Google Play 50c59532 - rating 1 - "Lệnh đặt xong, không thể sửa/hủy"
    "50c59532-84b0-4a83-ae32-6b8b631fa0a0": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lệnh đặt xong, không thể sửa/hủy.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [447] Google Play 91221ee6 - rating 1 - order stuck + AI support
    "91221ee6-f61c-4e82-8ec2-7ed2075267f6": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "đặt lệnh k khớp, hủy sửa cũng k được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "hỗ trợ thì AI trả lời lung tung. k có ng hỗ trợ bỏ mặc khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [448] Google Play 7994ad3a - rating 1 - "Lỗi không giao dịch được gì cả"
    "7994ad3a-fbe8-4921-a0e9-8fd062219660": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lỗi không giao dịch được gì cả",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [449] Google Play 10715b55 - rating 1 - frequent freeze, lost money
    "10715b55-e2ae-4183-9526-13ee6745d20a": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "thường xuyên treo lỗi làm mất tiền, làm thiệt hại khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [450] Google Play e278b975 - rating 1 - desktop QR login fails + bad CSKH
    "e278b975-7183-4b48-b291-1aae830dc27c": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "App desktop không xài đc chứng năng quét QR để đăng nhập.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "HỆ THỐNG CHĂM SÓC KHÁCH HÀNG CỰC TỆ. Công ty quảng cáo làm ăn tốt lắm và hệ thống chăm sóc khách hàng không thể chấp nhận được. Dịch vụ tệ nhất mà tôi từng trải qua.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [451] Google Play 5da43298 - rating 1 - 14/01/2026 system error
    "5da43298-166d-490c-b83b-8c5c144606e5": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "14.01.2026, từ 9h sáng, hệ thống lỗi không đặt đc lệnh. Với 1 công ty chứng khoán, TCBS đã rất không ổn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [452] Google Play fd2c190b - rating 1 - no notification when system recovers
    "fd2c190b-db45-422b-8174-630c33973175": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lúc cần thì lỗi. Không gửi thông báo kịp thời khi hệ thống bị lỗi hay sử dụng được trở lại. Ít nhất khi sử dụng được lại thì thông báo khách có nhu cầu sửa hay hủy lệnh không.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [453] Google Play 6e30c2fa - rating 1 - "Tệ" - vague
    "6e30c2fa-02e6-43ad-818c-1dae839ff8d8": {
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
    # [454] Google Play afb2af61 - rating 1 - many errors, lost 179M
    "afb2af61-25eb-4b6c-b38c-cf8fa5771bee": {
        "incidents": [
            {"incident_type": "friction", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "một ứng dụng, lỗi thì nhiều mà tận tâm thì ít , khuyên không nên sử dụng, lỗi rất nhiều tôi mất 179 triệu vì lỗi của nó",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [455] Google Play bc8d4d54 - rating 3 - app load slow
    "bc8d4d54-f2c0-49a0-b6e7-55fac5b11c5f": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "tốc độ load app cần cải thiện nhanh tối đa, hiện tại quá chậm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [456] App Store 13634622324 - rating 1 - frequent freeze during volatility
    "13634622324": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App thường xuyên treo, lag đặc biệt khi thị trường biến động. Anh em xài sẽ thấy cảnh muốn mua ko được, muốn bán không xong. Khi hết lag thì mọi chuyện đã qua, thiệt hại lớn lắm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [457] Google Play 2e5b19b6 - rating 1 - login errors
    "2e5b19b6-95a6-4096-a902-97b2962bf652": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "đăng nhập gì mà lỗi riết à",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [458] App Store 13681511706 - rating 1 - face verify fails
    "13681511706": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Cả buổi tối k xác nhận được khuôn mặt bực cả mình. Người ta canh góc nhìn thẳng vào cam rồi. Chỉnh rất nhiều lần vẫn k xác nhận đc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [459] Google Play 0eeeb54d - rating 3 - index scroll broken
    "0eeeb54d-31ef-476a-8384-c82d9b67a24d": {
        "incidents": [
            {"incident_type": "failure", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "2 hôm nay ở mục chỉ số mình không kéo xem được là sao ... các mục chỉ số phái sinh ở phía dưới không kéo xuống xem được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [460] App Store 13683768965 - rating 1 - CCCD update 3x fails + no support
    "13683768965": {
        "incidents": [
            {"incident_type": "failure", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "cập nhật CCCD 3 lần không được và không hề có nhân sự hỗ trợ, sử dụng chức năng Hỗ trợ trong App cũng không được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [461] App Store 13684259604 - rating 2 - app crash on iOS 15.8.5
    "13684259604": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App bị crash trên ios 15.8.5",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [462] Google Play 4969ce69 - rating 1 - random crashes
    "4969ce69-82b9-43de-833a-e3fb4173cb95": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App hay crash một cách vô cớ, bật không lên, dù đã gỡ đi và cài lại.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [463] Google Play a8c833fb - rating 1 - "nhân viên tcbs có biết đọc không" - vague insult
    "a8c833fb-d991-4ed4-8ec3-eac4602bb61f": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "tôi thắc mắc nhân viên tcbs có biết đọc không",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [464] App Store 13692057749 - rating 1 - can't trade odd-lot on mobile
    "13692057749": {
        "incidents": [
            {"incident_type": "unmet_need", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Tôi đã từng sử dụng VPS và VND giao dịch lô lẻ rất đơn giản, còn bên công ty này giao dịch lô lẻ phải lên máy tính. Mà đặt lệnh xong vẫn không giao dịch được, công nghệ kém",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [465] Google Play bd4b1420 - rating 2 - lag + order delay + index scroll
    "bd4b1420-3cb0-4f0f-90c0-9c91f9b63898": {
        "incidents": [
            {"incident_type": "friction", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "lag, lệnh đặt không được có độ trễ khớp lệnh trên bảng điện.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "phần chỉ số không kéo xuống coi tổng quan được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [466] App Store 13703439891 - rating 1 - "Thời gian xác thực lâu"
    "13703439891": {
        "incidents": [
            {"incident_type": "friction", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "MEDIUM",
             "evidence_span": "Thời gian xác thực lâu",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [467] Google Play 905e75f6 - rating 1 - need SSI for prices, Excel for tracking
    "905e75f6-8a68-4b8a-8766-a64ee3e0b043": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "phí giao dịch 0.03, nhưng app tệ, giao diện khó sử dụng. giao dịch trên TCBS mà phải xem bảng giá bằng SSI, theo dõi danh mục bằng Excel thủ công. thực sự TCBS ngoài phí rẻ ra thì app quá tệ luôn.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [468] App Store 13709946802 - rating 2 - "Cskh AI quá tệ"
    "13709946802": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Cskh AI quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [469] Google Play 9e7a5f33 - rating 1 - asset chart broken
    "9e7a5f33-408c-4d29-8a47-600164f61346": {
        "incidents": [
            {"incident_type": "failure", "family": "PORTFOLIO_TRACKING", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "Làm cái biểu đồ \"Tài sản\" hiện được mỗi Tổng quan. còn Tab Tiền, IPower,Cổ phiếu, Trái phiếu... lại không hiển thì dc biểu đồ tỷ lệ % danh mục.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PORTFOLIO_TRACKING", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [470] App Store 13710503150 - rating 1 - bad UX design
    "13710503150": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Cái cần thiết là thao tác trên app nhanh, tiện, chính xác chứ không phải nhét cả đống thứ vô làm rối rắm và thao tác chậm, không chính xác.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [471] App Store 13711043247 - rating 1 - community toxic
    "13711043247": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "cộng đồng trên ứng dụng TCBS này thì 1 sao vì đầu tư dưới 3 triệu,mà những người đó chửi những lời thô tục và kinh bỉ,sỉ nhục và lăng mạ tôi.",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [472] Google Play 21087ebd - rating 1 - re-login + frozen board + no auto-withdraw
    "21087ebd-11dc-4cb5-932b-a6f23c675263": {
        "incidents": [
            {"incident_type": "friction", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "lúc nào cũng đòi đăng nhập lại.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "mà thoát ra thoát vào cái bảng giá đứng im luôn ko có cập nhật.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "lúc mà thiếu tiền thi ko báo tự động rút tài khoản ngân hàng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [473] App Store 13714566655 - rating 1 - new phone login requires old phone
    "13714566655": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Mua điện thoại mới đăng nhập không được mặc dù có số tk và mật khẩu và Sdt chính chủ rồi. Bắt xác nhận điện thoại cũ (đã cho và đã cài lại máy và người nhận cũng đã đi xa) rất bất tiện. Vậy trường hợp mất máy thì làm sao xác nhận được. Cần cải cách lại có số tk, mk, sdt để xác nhận otp là đc rồi. Bảo mật là rất tốt nhưng bảo mật như này là quá cứng nhắc gây phiền hà mất thời gian của nđt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [474] Google Play 5e88b23d - rating 1 - bad UI/UX + slow info change
    "5e88b23d-0167-4f32-ae50-15e89a350a98": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "trải nghiệm ui/ux quá tệ , thay đổi thông tin thì lâu , hộ trợ cũng lơ Nga lơ ngơ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [475] App Store 13729429377 - rating 4 - iPad crashes
    "13729429377": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "mình vào bằng iPad không vào được toàn bị văng ra.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [476] App Store 13729660566 - rating 1 - "Trải nghiệm rất tệ, xử lý lâu"
    "13729660566": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Trải nghiệm rất tệ, xử lý lâu. Khuyên ko nên dùng",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [477] Google Play 9515fe76 - rating 1 - password reset fails many times
    "9515fe76-2a00-494d-aa0a-79d882d1665b": {
        "incidents": [
            {"incident_type": "failure", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Bắt khách cài lại mk đến chục lần chưa xong",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [478] App Store 13732547803 - rating 1 - bad buy/sell design
    "13732547803": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Công ty lớn mà thiết kế chức năng mua bán ngu k thể tả nôi",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [479] App Store 13733141742 - rating 1 - deposit takes all day
    "13733141742": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Nộp tiền vào tài khoản chứng khoán từ ngân hàng khác cả ngày mới nổi tiền. Rất bất tiện khi viết sai nội dung chuyển khoản.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
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
prog["current_batch"] = "Batch 6 (reviews 400-479)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:20:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 6 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
