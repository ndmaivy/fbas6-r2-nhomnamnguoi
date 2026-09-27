"""Classify Batch 7 (reviews 480-559) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[480:560]

CLASSIFICATIONS = {
    # [480] Google Play 62c0e271 - rating 1 - "app siêu tệ"
    "62c0e271-0108-42d1-b984-d8d269e8da8c": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app siêu tệ ,phí thời gian ,tiền bạc ,...",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [481] Google Play e848fbee - rating 1 - 10/02/2026 login fails
    "e848fbee-1472-45b5-a050-7ebe95952516": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "ngày 10.02.2026 lỗi không đăng nhập được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [482] Google Play 119065d9 - rating 5 - "ok Tôi ưu lợi nhuận" - praise
    "119065d9-99bc-49a2-a9c7-60b5364fa4ea": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [483] App Store 13757354364 - rating 5 - praise
    "13757354364": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [484] Google Play 729f405c - rating 5 - "ok" - praise
    "729f405c-971f-47b7-803d-ed285f1e2299": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [485] App Store 13779252669 - rating 1 - price board reloads
    "13779252669": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "App lỗi, khi đang xem bảng giá rất hay bị tải lại",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [486] App Store 13781072372 - rating 1 - face ID fails + bad UI
    "13781072372": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Không nhận diện được mặt.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện tệ",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [487] App Store 13782975799 - rating 5 - praise
    "13782975799": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [488] Google Play bd9c1fa8 - rating 1 - can't login since Tet
    "bd9c1fa8-0b6c-4eca-a793-693a8fe25c9a": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "ứng dụng tồi. từ tết đến giờ k đăng nhập nổi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [489] App Store 13785895204 - rating 1 - CSKH bot
    "13785895204": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Khi gặp vấn đề cần hỗ trợ, gọi điện toàn gặp mấy con bot tự động rất mất thời gian và không giải quyết được vấn đề.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [490] App Store 13785950483 - rating 1 - "App ép người dùng"
    "13785950483": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "MEDIUM",
             "evidence_span": "Mới khai thông tin đã bắt gán ghép người dùng có số tài khoản.",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [491] Google Play 13e0c0e6 - rating 2 - "Dăng ký ol mà lâu vl"
    "13e0c0e6-6e6c-4bdb-b12e-8fedf3068801": {
        "incidents": [
            {"incident_type": "friction", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "MEDIUM",
             "evidence_span": "Dăng ký ol mà lâu vl",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [492] App Store 13790529670 - rating 1 - "Chương trình khuyến mãi lừa đảo"
    "13790529670": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Làm gami mà mở hết 26 bao toàn lời chúc, thà không làm còn hơn",
             "confidence": "MEDIUM", "new_theme_flag": True, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [493] Google Play ee6e4be6 - rating 1 - face recognition fails
    "ee6e4be6-1988-40be-881d-d7ea9b5bab8d": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "phần nhận diện khuôn mặt mãi không nhận diện đc.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [494] App Store 13800783800 - rating 1 - iPad Pro M4 can't open
    "13800783800": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Ứng dụng không thể mở được trên ipad pro m4, mỗi lần muốn mở thì phải cài đặt lại, nhưng các lần tiếp theo lại không mở được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [495] Google Play eddf39d9 - rating 1 - "ap lỏ vl" - vague
    "eddf39d9-bd84-4593-8b55-0d8756ca835e": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "ap lỏ vl",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [496] App Store 13804511641 - rating 1 - registration kicks out
    "13804511641": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "App ko cần người dùng hả ta, đăng ký mấy hôm rồi mà đang xác thực cứ bị văng ra ngoài là thế nào nhỉ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [497] App Store 13805123311 - rating 1 - CCCD update rejected + 2 days
    "13805123311": {
        "incidents": [
            {"incident_type": "failure", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Cập nhật căn cước bị từ chối, không xử lí cho nhà đầu tư, duyệt căn cước phải mất 2 ngày giao dịch. Lúc tải app thì bình thường, nạp tiền vào mới bắt cập nhật.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [498] App Store 13807938938 - rating 3 - update without notice causes lag
    "13807938938": {
        "incidents": [
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Cập nhật cũng ko thông báo với user làm app lag lag",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [499] App Store 13807943183 - rating 1 - can't enter when need to trade
    "13807943183": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lúc cần vào giao dịch đặt lệnh thì không vào được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [500] App Store 13807955502 - rating 1 - password error unclear
    "13807955502": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "nhập mk không vào được, app cũng không thông báo do sai mk hay lỗi app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [501] App Store 13807964744 - rating 1 - error when need to sell
    "13807964744": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Lúc cần vào bán thì lỗi. Thiệt hại lớn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [502] Google Play d04467b7 - rating 1 - 3 days registration not approved
    "d04467b7-c165-407c-842a-05c55fccf017": {
        "incidents": [
            {"incident_type": "friction", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "sau trải nghiệm dki 3 ngày vẫn chưa dc duyệt, ban đầu thích bao nhiêu thì bây giờ thất vọng bấy nhiêu. chưa dùng đã ức chế như này rồi. TCBS mất uy tín",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [503] Google Play 14df952c - rating 1 - app slow at 11h, worse at 14h15
    "14df952c-2772-4273-b198-3e86db37e3ad": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App chậm, load lâu, 11h mà chạy ko nổi chứ nói gì thời điểm 14h15 trở đi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [504] Google Play b18d976a - rating 1 - derivatives margin withdrawal 2h
    "b18d976a-6d3f-4198-b4cd-5820f3c8abee": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Rút ký quỹ phái sinh mà hơn cả gần 2 tiếng tiền chưa về. Sợ hãi thật",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [505] Google Play 6641bc0e - rating 1 - many errors + slow CSKH
    "6641bc0e-8cf4-4608-ad69-285df0b314be": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Cùng cổ phiếu phát hành thêm, FPTS, VCI đã cho giao dịch thì TBCS vẫn khóa. Chậm hơn vài tiếng mới giao dịch dc. Cổ phiếu mua 5.300 cổ đến T+2 chỉ được giao dịch 100 cổ, phần còn lại ko thấy hiển thị ở đâu luôn.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Liên hệ trợ giúp thì cực kỳ lâu mới phản hồi và phản hồi cũng chẳng giúp dc gì. Chỉ đổ cho lý do này kia bla bla bla.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [506] App Store 13818840202 - rating 1 - can't edit/cancel order
    "13818840202": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Không sửa và huỷ lệnh được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [507] Google Play d8a64903 - rating 1 - "dịch vụ bố mẹ khách hàng" - vague insult
    "d8a64903-58c4-4159-884f-be5a0131e94f": {
        "incidents": [
            {"incident_type": "unclear", "family": "OTHER", "subtype": "",
             "journey": "UNKNOWN", "severity": "LOW",
             "evidence_span": "dịch vụ bố mẹ khách hàng",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "UNCLEAR",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "UNKNOWN",
        "max_severity": "LOW", "confidence": "LOW", "needs_human_review": True,
    },
    # [508] Google Play 59a17ffa - rating 1 - registration fails all morning
    "59a17ffa-0cab-481a-8e5c-46a6c7f81924": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "đăng ký cả buổi chả được. quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [509] Google Play e4d92484 - rating 1 - "không mua được mã"
    "e4d92484-359e-4a4c-a6d6-a3dacbde2a76": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "không mua được mã",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [510] App Store 13836082606 - rating 1 - phone change takes 1 week
    "13836082606": {
        "incidents": [
            {"incident_type": "friction", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "thay đổi số điện thoại thôi mà bắt đợi 1 tuần, support nhắn tin tiếng rep 1 lần",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [511] Google Play 0a5262e3 - rating 1 - withdrawal requires iTOP change + 24h
    "0a5262e3-0527-40a6-9611-44eb3b1d1c7f": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Rút có 1đ để test mà còn rườm rà bảo đổi iTOP gì đó rồi thì sau 24h mới cho rút, vãi thật",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [512] Google Play 19822191 - rating 1 - face update 30s limit
    "19822191-5066-4695-b3cb-6420cd103f97": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Cập nhật khuôn mặt không được. Bắt làm trong 30s rất dốt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [513] App Store 13838846691 - rating 1 - eKYC QR scan fails
    "13838846691": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "App bắt ekyc nhưng đến bước quét qr ở cccd thì k thể quét được. Team dev check lại vì nó block luồng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [514] Google Play 26405e29 - rating 4 - feature request: child account for funds
    "26405e29-6e00-44eb-8547-08c38fa7beca": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "phần tài khoản cho con nên thêm vào mua quỹ thay vì chứng khoán vì an toàn và ổn định hơn.",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [515] App Store 13846427918 - rating 5 - praise
    "13846427918": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [516] App Store 13852640366 - rating 1 - fast deposit, 3-day withdrawal
    "13852640366": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Nạp tiền thì nhanh, rút tiền thì 3 ngày chưa về lần đầu cũng là lần cuối sd ap",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [517] App Store 13853301981 - rating 1 - notification popup harassment
    "13853301981": {
        "incidents": [
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Người dùng đã cố ý tắt thông báo rồi cứ bật popup bảo mở thông báo. Quá phiền",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [518] Google Play 15b38521 - rating 1 - no updates, network error
    "15b38521-f61d-4553-8c4f-b5b50af77862": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App cc gì nửa năm rồi ko thèm cập nhật. báo lỗi kết lỗi mạng cứ bắt tải lại trong khi đt vẫn vào mạng bình thường",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [519] App Store 13857042814 - rating 4 - English: notes only in Vietnamese
    "13857042814": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App notes are all in Vietnamese and updates only in Vietnamese even though app is multilingual. Many app notifications and critical password and login screens are in Vietnamese even in the english version",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [520] Google Play 93b32545 - rating 1 - periodic order broken + ghost CSKH
    "93b32545-25cd-443c-8eca-c05809363539": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Chức năng cơ bản (đặt lệnh định kỳ) còn lỗi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Báo customer support thì bảo ghi nhận rồi ghost.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [521] Google Play 93bd1c81 - rating 1 - frequent freeze, lag
    "93bd1c81-35e4-4c3a-8a28-17d936daca9c": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app thường xuyên đứng, giật lag",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [522] App Store 13867043839 - rating 1 - "Xử lý chậm chạm thời bao cấp"
    "13867043839": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Xử lý chậm chạm thời bao cấp",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [523] App Store 13867670560 - rating 1 - notification always asks to enable
    "13867670560": {
        "incidents": [
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Tôi tắt thông báo trong cài đặt nhưng App luôn yêu cầu bật thông báo.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [524] Google Play ba7b917f - rating 1 - OTP never sent + no CSKH
    "ba7b917f-dc3a-47e8-9671-2590c822472b": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "chờ mòn mỏi không gửi OTP để đặt lệnh mua.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Gọi tổng đài hỗ trợ thì không liên hệ được, mọi người nên gỡ app không nên dùng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [525] Google Play bc3089a0 - rating 3 - deposit slow + no security + index scroll
    "bc3089a0-7e6a-4841-b345-f751fd12f23d": {
        "incidents": [
            {"incident_type": "friction", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "MEDIUM",
             "evidence_span": "Nạp tiền thì trừ trong ngân hàng liền, mà tiền thì vô chậm, mấy tiếng sau mới vào",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "SECURITY_ACCOUNT_PROTECTION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "Mỗi lần vô app đều vô thẳng ko có bảo mật gì, hình như 1 ngày thì mới tái khởi động lại vân tay.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Bảng tab các chỉ số thì ko kéo đc, chỉ hiện có vài chỉ số rồi đứng ngang",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "giao diện khó hiểu, ko trực quan",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [526] App Store 13884487026 - rating 1 - widget session expired + crash
    "13884487026": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Widget bị lỗi phiên đăng nhập đã hết hạn dù đã đăng nhập rồi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Thường xuyên bị lỗi vừa mở app đã bị dừng đột ngột",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [527] App Store 13898550807 - rating 5 - praise
    "13898550807": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [528] App Store 13902315721 - rating 1 - info change 2 weeks
    "13902315721": {
        "incidents": [
            {"incident_type": "friction", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "Mình không hiểu sao xử lý thay đổi thông tin khách hàng kiểu gì mà 2 tuần rồi mà không được. Hỗ trợ khách hàng thì trả lời rất mượt mà xử lý giải quyết cho khác hàng thì rất kém. Sau lần này mình sẽ chuyển hết sang sàn khác dùng. Có thay đổi mỗi thông tin khách hàng mà chính chủ khách hàng đi thay đổi mà còn xử lý hết lần này lần khác. Nhiều quan chức để xét duyệt quá…",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [529] Google Play 04d4c814 - rating 2 - black screen on open
    "04d4c814-7047-419f-9f32-0b9a404a62ae": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "nay mở app không được, bấm vào sau 1 lát bị màn hình đen, đã xóa và tải lại nhưng vẫn không được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [530] App Store 13910455012 - rating 1 - 600k fee on 500k purchase
    "13910455012": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Bị trừ tiền nghĩa vụ chứng khoáng gần 600k trong khi mới mua được 500k thử chơi ?????",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [531] App Store 13912796083 - rating 1 - bad support + AI bot
    "13912796083": {
        "incidents": [
            {"incident_type": "friction", "family": "NOTIFICATION_COMMUNICATION", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "giao dịch bên này thông báo dao dịch trừ tiền không rõ ràng, trừ tiền mà không thấy thông báo trong mail hay mục thông báo.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Khi liên hệ hỗ trợ thì cho robot nói chuyện hỏi một hồi cảm thấy tức điên vì robot không hiểu vấn đề mình cần hỗ trợ, toàn lặp đi lặp lại cái gì đâu không. Liên hệ qua Zalo thì chờ nhắn tin trả lời rất lâu, rất mất thời gian. Bên này không có chuyên viên hỗ trợ.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [532] Google Play 35551fc6 - rating 5 - "đang dùng bt, chưa thấy lỗi" - praise
    "35551fc6-f964-4261-93a1-b06b1d12f38a": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [533] Google Play 7e63a66f - rating 1 - bad UI + feature errors
    "7e63a66f-18e9-445a-8348-dbcf097c4fc9": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Cũng của techcombank mà app này giao diện dở tệ quá, lỗi tính năng nữa",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [534] App Store 13934417294 - rating 1 - hotline busy, AI support
    "13934417294": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Gọi tổng đài báo bận đá sang chát zalo, face... ko giải quyết đc vấn đề",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [535] Google Play 419c55b8 - rating 1 - "app lỗi quá nhiều"
    "419c55b8-4ad2-4635-86f5-ae0c0f00c000": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app lỗi quá nhiều, quá tệ, khả năng quý 2 quý 3 thị phần đi xuống",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [536] App Store 13952806460 - rating 1 - AI overuse + OTP delay + KYC broken
    "13952806460": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Dùng Ai nhiều quá mà không kiểm tra xem ai có chạy được hay không. Tuy áp nhiều tính năng hay nhưng nhân viên hoạt động rất lười làm việc.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "ONBOARDING_KYC", "severity": "HIGH",
             "evidence_span": "Đăng ký không gửi được otp. Delay lâu rồi gửi 1 đống. Nhận xác thực chậm. Kyc không hoạt động được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [537] App Store 13953085318 - rating 4 - periodic order bugs
    "13953085318": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Phần đặt lệnh định kỳ đang có khá nhiều lỗi, giá trị ước tính vượt xa giá trị hiện tại của cổ phiếu, 1000 E1VFVN30 mà ước tính trên 200 triệu??. Khi đặt lệnh xong và xem chi tiết lệnh thì hiển thị \"Ngày undefined hàng tháng\".",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [538] App Store 13953572832 - rating 2 - bad UX/UI + lag
    "13953572832": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "UX của app không thân thiện UI cũng không hiện đại, FE code chưa tốt app lag hoạt ảnh giữa màn hình không mượt.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [539] Google Play 6e6df48f - rating 1 - "tính thuế bán cao vcl"
    "6e6df48f-c089-4136-aba5-3b9c5dce6ae6": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "tính thuế bán cao vcl",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [540] Google Play 424f7be0 - rating 4 - "cập nhật giá nav chậm"
    "424f7be0-92d0-4639-b484-7a74e7874cce": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "cập nhật giá nav chậm",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [541] Google Play 12a15533 - rating 5 - "ok" - praise
    "12a15533-34a5-4b70-8535-3bee8c3a3f30": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [542] Google Play 4f426382 - rating 2 - can't open app since 15/4
    "4f426382-5cd0-4c4f-8ec6-7b3912930e9a": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "từ 15/4/2026 đến nay tôi không mở được ứng dụng này trên điện thoại để xác nhận giao dịch, đang cảm thấy lo lắng và bực mình đây",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [543] Google Play c5d09130 - rating 2 - "lỗi ko đăng nhập dc"
    "c5d09130-930e-454b-9af7-fda1b6a1da19": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "lỗi ko đăng nhập dc.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [544] Google Play 8601f3eb - rating 1 - 16/04 login fails + AI bot
    "8601f3eb-e66c-468b-a6cc-f536335533e3": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "16.04.2026 đăng nhập liên tục mà không vào được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "gọi điện thoạ gần 10 cuộc cũng không được nhắn tin thì cho con AI ngoo ngốc trả lời.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [545] Google Play 8c8bebe4 - rating 5 - feature request: tablet landscape
    "8c8bebe4-06ea-4546-9533-66d3e4d79109": {
        "incidents": [
            {"incident_type": "feature_request", "family": "OTHER", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "nếu có bản tối ưu cho table màn hình ngang thì tốt quá, dễ theo dõi biểu đồ hơn",
             "confidence": "HIGH", "new_theme_flag": True, "needs_human_review": False}
        ],
        "sentiment": "NEUTRAL", "complaint_present": False, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [546] Google Play a709540e - rating 1 - many errors + AI bot
    "a709540e-8ccf-43a1-9967-bd19a5bf834b": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "phần mềm quá tệ không vào được lỗi tùm lum.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "liên hệ thì cho con robot trả lời có âm sao chắc cho luôn âm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [547] Google Play aed07819 - rating 1 - S24 Ultra app kicks out
    "aed07819-1561-4bc9-8bc2-d91999923cd1": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App vô bị đá ra liên tục s24ultra chứ phải đt dỏm đâu mà vậy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [548] Google Play 0396520b - rating 1 - continuous crash
    "0396520b-fad4-4f75-b547-c52217fa760a": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App cùi bắp văng app lỗi liên tục cả ngày ko ai fix",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [549] Google Play 03428347 - rating 1 - "IT team poor"
    "03428347-9975-4510-a132-6bdefbeee40f": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Đội ngũ IT quản trị app quá kém, nếu sử dụng thường xuyên thì sẽ có ngày mất tiền oan",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [550] Google Play ffb1654a - rating 1 - crash >1 day
    "ffb1654a-5c14-4fd1-adc2-fd6153767ac3": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "app crash liên tục hơn 1 ngày trời. xóa đi cài lại vẫn crash không vào được.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [551] Google Play 9affbb8e - rating 1 - 2 days can't login
    "9affbb8e-9af2-4acd-945b-ddcac4ea8907": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "2 hôm nay ko thể vào đc, cứ bị văng ra ko cho đăng nhập",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [552] Google Play 5b3cf01d - rating 1 - crash on entry + AI CSKH
    "5b3cf01d-5edb-4091-b0b1-76781aed1b30": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "App quá tệ vừa vào là văng ra, mấy ngày liền ko làm được gì",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "tổng đài AI như đấm vào mõm khách hàng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [553] Google Play 8832565b - rating 5 - "dễ dùng đó" - praise
    "8832565b-75c1-45d2-8fc2-a846e4f983be": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [554] Google Play 52a1c486 - rating 1 - 17/04 day 2 app crashes + AI CSKH
    "52a1c486-e460-4653-804b-f0536d6c44b9": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "17/4/2026 Là ngày thứ 2 app văng liên tục, không thể truy cập để giao dịch. Truy cập vào web cũng không được, vì cần xác thực Otp bằng app.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Gọi tổng đài thì không có nhân viên, chỉ có AI trả lời. Gọi tổng đài Techcombank thì nhân viên báo không liên quan.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [555] Google Play 769d1499 - rating 5 - praise
    "769d1499-6547-4aec-a09c-b7618009c23b": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [556] Google Play 1e1b223f - rating 5 - praise
    "1e1b223f-d11d-444b-a45b-43d096278d3a": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [557] Google Play 81dc8f57 - rating 1 - can't enter app
    "81dc8f57-6659-4387-85ae-e2e77d05cb26": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "không thể vào đc app, thế tiền của t định giải quyết như thế nào đấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [558] App Store 13987803897 - rating 1 - login keeps spinning
    "13987803897": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "Đăng nhập toàn quay. Không vào được app",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [559] App Store 13991870835 - rating 1 - bad UX
    "13991870835": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "T dùng ssi 2 năm mở thêm tcbs dùng mà ux tệ kinh khủng, những flow cơ bản rất loàng ngoằng ko hiểu sd kiểu gì, thông tin qtrong cứ dấu đi đâu á. Rất tệ, nào bán cp xong chắc ko bh dùng lại app này, cũng hệ sinh thái Tech mà ux app tệ quá",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
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
prog["current_batch"] = "Batch 7 (reviews 480-559)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:25:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 7 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
