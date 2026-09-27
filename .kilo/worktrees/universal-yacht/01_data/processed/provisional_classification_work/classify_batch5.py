"""Classify Batch 5 (reviews 320-399) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[320:400]

CLASSIFICATIONS = {
    # [320] Google Play 644c82c5 - rating 2 - home page balance not syncing
    "644c82c5-37af-489d-81a2-3ef8bb4c2281": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PORTFOLIO_TRACKING", "severity": "MEDIUM",
             "evidence_span": "ở Trang Chủ, tiền nhảy không kịp với bên trong. Trước đây nhấp nháy theo liên tục, giờ thì đơ ra, rút tiền về rồi vẫn không thấy thay đổi.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [321] App Store 13101805426 - rating 3 - feature request: CW in watchlist
    "13101805426": {
        "incidents": [
            {"incident_type": "feature_request", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "LOW",
             "evidence_span": "Muốn thêm vài mã chứng quyền trong danh mục để theo dõi bảng giá mà không có, chỉ thêm được mã cổ phiếu mà ko thêm được mã CW.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [322] Google Play a604cb52 - rating 5 - "rất ok" - praise
    "a604cb52-b613-43b7-98e2-58a855dd280c": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [323] Google Play f3f3993b - rating 3 - UI request redesign
    "f3f3993b-daf2-40fe-9dd2-1267f9eec14e": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App có thể làm lại giao diện không, giao dịch mà nó phế quá, nhìn rối như tơ vò, ssi dùng xong đây phí thấp mà chán thật",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [324] Google Play d7ede0cd - rating 2 - UI ugly
    "d7ede0cd-d945-4a41-93ab-543f21a3177e": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "cái app giao diện cùi nhất từng dùng, giao diện gì nhìn đau cả mắt vs rối mù. Nên qua bên mấy app chứng khoán khác học hỏi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [325] App Store 13112614932 - rating 1 - "Không thể hiểu dc cách sử dụng"
    "13112614932": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Không thể hiểu dc cách sử dụng app này luôn",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [326] Google Play 9a01a340 - rating 5 - "quá oki" - praise
    "9a01a340-159c-426d-b9bd-b9ccd87b423d": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [327] Google Play 6876f8dc - rating 2 - UI ugly + hard to use
    "6876f8dc-735e-4f4e-a57d-c79023bddbc0": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện app quá tệ, khó sử dụng, quá nhiều thứ thừa thãi gây rối mắt, những cái cần thiết thì không có, cả phiên bản web cũng tệ. Quá bất tiện",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [328] Google Play 92efdfc6 - rating 1 - CCCD update fails
    "92efdfc6-cc34-4c87-b6da-92cfcb0c08cf": {
        "incidents": [
            {"incident_type": "failure", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "cập nhật căn cước miết ko đc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [329] Google Play abd0bdab - rating 1 - face verify failure
    "abd0bdab-c53b-4138-adfa-4b4f95d9a19b": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "làm cái xác thực khuôn mặt",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [330] Google Play cfaa3b16 - rating 1 - password change broken
    "cfaa3b16-cfa8-409b-a7bb-00088b9bb1e0": {
        "incidents": [
            {"incident_type": "failure", "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "subtype": "",
             "journey": "ACCOUNT_PROFILE_MAINTENANCE", "severity": "HIGH",
             "evidence_span": "thay đổi mật khẩu mà rất khó quên mất mật khẩu mà không làm được gì nó cứ bảo không tìm thấy profile",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE", "primary_subtype": "", "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [331] Google Play e17a1244 - rating 1 - "ko vào dc"
    "e17a1244-02e2-46a7-b4e8-ef5e21919c2c": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "ko vào dc",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [332] Google Play acc7e061 - rating 1 - lag/freeze
    "acc7e061-b997-4518-87e5-8b1f6c77638a": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "lag giật, đơ liên tục, dùng tikop finhay anfin chả app nào lag như này",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [333] Google Play c83bd478 - rating 1 - chatbot unhelpful
    "c83bd478-c994-4862-897c-24c7830933e1": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "hỏi chatbot chỉ thêm bực mình mà lại ko có nhân viên tư vấn",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [334] App Store 13146645363 - rating 2 - many bugs
    "13146645363": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "đây là cái app nhiều bugs nhất mà tôi từng sử dụng, cảm giác như chạm vào đâu cũng có thể bugs vậy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [335] App Store 13151606169 - rating 3 - app freeze, hard to trade
    "13151606169": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "App đơ đơ giao dịch rất khó chịu",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [336] Google Play 566474d5 - rating 1 - widget doesn't run
    "566474d5-d547-4245-a66f-048a69f2a45c": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "widget ko chạy hoặc ko cập nhật khi đưa ra màn hình chính",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [337] Google Play f1abd52a - rating 1 - many features but hard to use
    "f1abd52a-0825-4c19-98ca-a772b551d34a": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "nhiều chức năng nhưng khó dùng",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "MEDIUM", "needs_human_review": True,
    },
    # [338] Google Play ae4b7932 - rating 5 - praise
    "ae4b7932-0aa0-4495-9757-103a20a1c6a7": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [339] Google Play 296ce42b - rating 1 - CCCD verification 1 day, blurry rejection
    "296ce42b-807e-4283-b87e-38ee37ed117f": {
        "incidents": [
            {"incident_type": "friction", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "Chờ xác thực tài khoản rất lâu, chờ suốt 1 ngày rồi báo cc chụp mờ trong khi rất rõ nét",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [340] Google Play 6913b500 - rating 1 - OTP not sent from FPT
    "6913b500-e1af-4fa6-99be-e1f2fdaf457f": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "mãi chẳng gửi otp từ fpt is, đúng số đt r mà hk gửi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [341] App Store 13172558353 - rating 1 - high margin + AI CSKH + overnight fee
    "13172558353": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "có sự cố kg thể gọi cho nhân viên cskh mà chỉ qua con nhỏ Ai nói khùng điên",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "tính tiền qua đêm lừa đảo gian dối",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": True,
    },
    # [342] Google Play d0280c39 - rating 1 - messy UI, order not intuitive
    "d0280c39-1b13-4185-a404-945577140335": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Giao diện rườm rà. Nhìn rối mù, các mục cần quan sát thì nhỏ xíu, danh mục quản lý đặt lệnh không trực quan cụ thể. Các mục sắp xếp rối.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [343] Google Play 7094986b - rating 1 - bad CSKH + ugly app
    "7094986b-7428-4c44-b0bf-eb13f87c8776": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "cskh rất tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app xấu kinh khủng",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [344] Google Play e770901a - rating 3 - lag on phone, OK on laptop
    "e770901a-c03f-45ee-a57d-c6a03958960b": {
        "incidents": [
            {"incident_type": "friction", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app này mình thấy dùng trên dt rất lag nhưng dùng trên laptop thì ổn áp, nhưng đa phần mình toàn dùng đt để giao dịch thôi ạ .",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [345] Google Play 4a46f453 - rating 2 - too many ads + slow order placement
    "4a46f453-d5ba-48e9-981d-f934c875aab4": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Quảng cáo quá nhiều, app đầu tư chứng khoán mà mất rất nhiều thời gian mới đặt lệnh được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [346] Google Play 767df8de - rating 1 - can't open account, no email reply
    "767df8de-ec05-43b8-b669-dad98e8cf886": {
        "incidents": [
            {"incident_type": "failure", "family": "ONBOARDING_KYC", "subtype": "",
             "journey": "ACCOUNT_OPENING_KYC", "severity": "HIGH",
             "evidence_span": "không mở được tài khoản, kêu gửi mail mà không thấy trả lời ngta",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "ONBOARDING_KYC", "primary_subtype": "", "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [347] Google Play 8f924c68 - rating 3 - UI ugly, learn from Techcombank
    "8f924c68-ce05-49e6-866a-1dee63fcc932": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện xấu quá, nhìn là không muốn dùng rồi, sao không nâng cấp giao diện lên cùng một style như app techcombank ấy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [348] App Store 13230058357 - rating 1 - hotline never picks up
    "13230058357": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Có vấn đề cần tư vấn gọi tổng đài ko bao giờ có ai nhấc máy và tư vấn . Toàn máy bận",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [349] Google Play 1b27da5e - rating 2 - bad experience + widget
    "1b27da5e-f655-44d8-b692-dab5a410c5d5": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Trải nghiệm app rất tệ. Widget cũng rất tệ. Không chỉnh được danh mục mã CP quan tâm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [350] Google Play 7b5cc2e8 - rating 2 - features OK but CSKH bad
    "7b5cc2e8-4b1c-400a-92d8-4d8b1af22dc1": {
        "incidents": [
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Gọi tổng đài thì toàn mấy con AI tiếp chuyện, nhắn tin thì nhân viên ko giải quyết được gì.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [351] Google Play c9f422d0 - rating 1 - white font order screen ugly
    "c9f422d0-2417-41ae-bb5e-c108733cf939": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "ứng dụng thay đổi phông đặt lệnh màu trắng thật tởm lợm, yêu cầu khôi phục như cũ, app để phông lệnh thế này xứng đáng 1 sao",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [352] App Store 13243002599 - rating 1 - messy, no % change, no 3 price levels
    "13243002599": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "K có % tăng giảm các mã ở bảng giá",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Hiển thị nhiều thông tin k cần thiết, khi mua bán cp k hiển thị 3 mức giá mua bán gần nhất rất khó mua bán được giá tốt",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [353] Google Play 3e926cdf - rating 1 - bloated + slow + AI useless
    "3e926cdf-ee8f-49c3-b9e1-994ed59b9965": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "app dở nhất trong các app chứng khoán, nhồi nhét chức năng. load chậm xử lý chậm.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "AI_SUPPORT_CONTEXT_QUALITY", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "nhét AI vào làm gì trong khi load cái bảng không xong???",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [354] App Store 13247396302 - rating 1 - "Cskh tệ"
    "13247396302": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Dịch vụ hỗ trợ khách hàng tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [355] App Store 13272131452 - rating 1 - black screen during trading
    "13272131452": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đến giờ giao dịch, app lag ko xem được gì. Đen thui.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [356] Google Play 9f588cc7 - rating 1 - old phone can't install
    "9f588cc7-247f-45c6-ab01-a1d11bb9616a": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Điện thoại đời cũ ko tải đc",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [357] App Store 13276981462 - rating 1 - freeze when need to sell
    "13276981462": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "App thường xuyên treo lúc cần bán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [358] Google Play 5e10e799 - rating 1 - login error, unusable
    "5e10e799-e923-496b-818d-fb89540ed690": {
        "incidents": [
            {"incident_type": "failure", "family": "LOGIN_AUTHENTICATION", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "đăng nhập rồi lỗi, không dùng được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "LOGIN_AUTHENTICATION", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [359] App Store 13280235898 - rating 1 - price load super slow
    "13280235898": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Load giá quá chậm đáng 1 sao.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [360] Google Play 91e69385 - rating 4 - feature request: periodic orders
    "91e69385-a626-4090-8830-153d29d88107": {
        "incidents": [
            {"incident_type": "feature_request", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "LOW",
             "evidence_span": "nếu có lệnh mua định kì cổ phiếu lô lẻ hay mua hàng ngày số tiền xác định 50-100k thì tuyệt nhất. đỡ hàng ngày nhìn biểu đồ, đầu tư thụ động tối ưu.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": False, "product_related": "YES",
        "primary_family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "LOW", "confidence": "HIGH", "needs_human_review": False,
    },
    # [361] App Store 13289538564 - rating 1 - 20/10 system delay
    "13289538564": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Ngày 20/10 hệ thống trễ quá lớn. Ảnh hưởng nghiêm trong trong giao dịch phái Sinh",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [362] App Store 13290030950 - rating 1 - market event = app dies
    "13290030950": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Cứ khi nào thị trường có biến lớn là app bị ngu ko load đc. Mấy lần r chứ ko phải một lần. Mất tiền oan mất lần chỉ vì cái app.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [363] App Store 13290082792 - rating 1 - super lag during wealth tech
    "13290082792": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App quá lagg, ko chấp nhận nổi, bày đặt đòi wealth tech nhưng app lag lòi mà bày đặt, xem lại căn bản đã",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [364] Google Play 353e3c17 - rating 1 - update worse, chart wrong
    "353e3c17-d9a3-4543-be66-696313163b77": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "up date xong tệ hơn, đồ thị 1 đường giá 1 kiểu, thông tin lệnh thì không có, yêu cầu về lại bản cũ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [365] App Store 13290348242 - rating 1 - can't buy/sell on 20/10 market crash
    "13290348242": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Ngày 20/10/2025 thị trường có phiên giảm sâu kỷ lục hơn 94 điểm, nhưng tôi không thể mua bán cổ phiếu trên app làm danh mục của tôi lỗ nặng do không thể mua để DCA",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [366] Google Play 87d4ca9a - rating 1 - IPO day lag, can't trade
    "87d4ca9a-c274-4324-9b5c-890fe0d01b82": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Mai ipo TCX rồi mà nay lag app ko mua bán gì được. đề nghị admin xem lại hạ tầng của app.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [367] Google Play 71b9c261 - rating 1 - lag when need to buy
    "71b9c261-395d-4f67-b3b2-dcdc357d8ea2": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "app cực kém, lúc cần mua thì bị lagg nhất định không cho mua, mất nhiều cơ hội vàng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [368] Google Play 6891cb2b - rating 1 - market crash = app freeze
    "6891cb2b-a3b4-4a98-97ee-37f8db6689d2": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Quá tệ, thị trường sập app đơ lag ko cho mua bán",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [369] Google Play 604a520a - rating 1 - market volatility = app freeze
    "604a520a-018e-40f2-aa15-078d7fec8eda": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Đúng lúc thị trường biến động thì app đơ ko thể giao dịch được!",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [370] Google Play 787e16ff - rating 1 - bad experience + no CSKH
    "787e16ff-0622-4417-af39-14326011d974": {
        "incidents": [
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "cskh không ai phản hồi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT", "primary_subtype": "", "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [371] Google Play 6611ff7b - rating 1 - easy deposit, hard withdrawal
    "6611ff7b-7235-46ef-8c16-98055bfdf73c": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "nạp 500k vào thì mau còn rút ra thì ko đc giống lừa đảo ghê rút thì nó bảo dịch vụ chuyển tiền tạm ngưng chán thật",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [372] Google Play 9559d520 - rating 1 - listing day lag
    "9559d520-4c18-439a-a87c-c604836aa0e5": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Nhân ngày lên sàn app lag như koz",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [373] App Store 13295667287 - rating 3 - too complex, redundant
    "13295667287": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "App nhiều tính năng, tốt, nhưng sắp xếp quá phức tạp một cách không cần thiết, rối. Cần làm cho đơn giản bớt. Một chức năng không cần phải xuất hiện ở nhiều nơi khác nhau.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "MIXED", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [374] Google Play c0f59e03 - rating 1 - OTP issue + banner ad
    "c0f59e03-37c1-419f-98bf-f58d4d03b89f": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "đặt lệnh trên web mà mãi ko có otp gửi điện thoại.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "đặt lệnh app thì số lượng với giá cổ phiếu nhảy loạn xạ, bảng giá thì load chậm. Vừa vào đã hiện cái banner quảng cáo, bộ nghĩ nđt người ta xem cái đấy à.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [375] App Store 13301878527 - rating 5 - "Mac !!!!!!!!!!!!!!!!" - sarcasm; Mac can't open
    "13301878527": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "Máy mac app vào không được nhé !",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [376] Google Play 6d68116a - rating 1 - "Làm app với web như này" - vague
    "6d68116a-74e9-4e8e-be7c-43b6078415c3": {
        "incidents": [
            {"incident_type": "friction", "family": "OTHER", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Làm app với web như này đòi người ta đầu tư.",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "OTHER", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [377] App Store 13306623450 - rating 1 - messy + can't create periodic order
    "13306623450": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "càng ngày càng rối. rối rắm khó khăn",
             "confidence": "MEDIUM", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "unmet_need", "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "tạo cái lệnh định kỳ quỹ cũng không cho",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [378] Google Play 16952e31 - rating 1 - can't withdraw
    "16952e31-0146-4d80-bae8-0d1304a0d6ea": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "sao rút tiền không được vậy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [379] Google Play 2d332b92 - rating 1 - Diamond customer benefits missing + high margin fee
    "2d332b92-4e4e-4c12-9526-daf360cd5d1e": {
        "incidents": [
            {"incident_type": "friction", "family": "FEE_PRICING", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "khách hàng Diamond mà không có các quyền lợi đầy đủ như trong mục ghi, phí vay margin quá cao",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "dvcskh quá tệ",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "FEE_PRICING", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [380] Google Play 0ffd0f52 - rating 1 - fingerprint requires iOTP cancel + messy UI
    "0ffd0f52-46ad-4c3b-a711-c3eea379055e": {
        "incidents": [
            {"incident_type": "friction", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "MEDIUM",
             "evidence_span": "Bật tính năng đăng nhập bằng vân tay mà bắt phải hủy iotp ở thiết bị cũ? không hiểu kiểu gì. Giờ có 2 đt mà chỉ 1 chiếc phải đăng nhập = mật khẩu rất phiền.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "Giao diện quá nhiều thứ phức tạp, khó sử dụng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [381] Google Play 8c23f05e - rating 2 - OTP never received
    "8c23f05e-9945-4cd9-b130-b91b7b0eaef2": {
        "incidents": [
            {"incident_type": "failure", "family": "AUTHENTICATION_IOTP", "subtype": "",
             "journey": "LOGIN_AUTHENTICATION", "severity": "HIGH",
             "evidence_span": "gửi mã cả ngày mà không thấy về vậy",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP", "primary_subtype": "", "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [382] Google Play 1f919269 - rating 2 - can't enter + no CSKH
    "1f919269-cdd5-413a-a84b-73f1b44a2b11": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "ko vào dc app, bực kinh khủng.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "HIGH",
             "evidence_span": "Nhắn vào page thì chỉ thấy để nội dung chi tiết cho Mập, ko thấy chuyên viên đâu.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [383] App Store 13332105950 - rating 1 - chart gets deleted
    "13332105950": {
        "incidents": [
            {"incident_type": "failure", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Lỗi bị xoá chart. Vẽ 1 2 hôm là bị xoá.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False},
            {"incident_type": "friction", "family": "CUSTOMER_SUPPORT", "subtype": "",
             "journey": "CUSTOMER_SUPPORT", "severity": "MEDIUM",
             "evidence_span": "Nhắn hỗ trợ r mà chưa dc.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [384] Google Play 7a5988b3 - rating 3 - "hôm nay bị lỗi à" - vague
    "7a5988b3-cc5f-4f88-b009-631bee990259": {
        "incidents": [
            {"incident_type": "friction", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "hôm nay bị lỗi à",
             "confidence": "LOW", "new_theme_flag": False, "needs_human_review": True}
        ],
        "sentiment": "UNCLEAR", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "LOW", "needs_human_review": True,
    },
    # [385] Google Play 73f6154c - rating 1 - continuous crash
    "73f6154c-9e9f-4c5e-8df2-5f3c1cccf794": {
        "incidents": [
            {"incident_type": "failure", "family": "PERFORMANCE_RELIABILITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "HIGH",
             "evidence_span": "crash liên tục, cty 3-4 tỷ đô làm cái app éo xong",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [386] Google Play 8b23d558 - rating 3 - widget can't be installed
    "8b23d558-1a64-4037-9d25-b39ed5540df3": {
        "incidents": [
            {"incident_type": "failure", "family": "MOBILE_TABLET_RESPONSIVENESS", "subtype": "",
             "journey": "PRODUCT_DISCOVERY_MARKET_DATA", "severity": "MEDIUM",
             "evidence_span": "Widget không dùng cài được trên màn hình :(",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS", "primary_subtype": "", "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [387] Google Play 6ab18151 - rating 2 - unfriendly UI
    "6ab18151-d19b-4dc0-a392-e336feb03958": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "GENERAL_CROSS_JOURNEY", "severity": "MEDIUM",
             "evidence_span": "giao diện không thân thiện, quá nhiều thứ rắc rối không cần thiết",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [388] App Store 13358137009 - rating 1 - transfer fails multiple times
    "13358137009": {
        "incidents": [
            {"incident_type": "failure", "family": "DEPOSIT_WITHDRAWAL_TRANSFER", "subtype": "",
             "journey": "FUNDING_CASH_TRANSFER", "severity": "HIGH",
             "evidence_span": "Chuyển tiền nhìu lần không được",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER", "primary_subtype": "", "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [389] App Store 13358337331 - rating 5 - praise
    "13358337331": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [390] App Store 13362364103 - rating 5 - English praise
    "13362364103": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [391] Google Play a85de5db - rating 1 - need computer to see prices
    "a85de5db-c6e5-46c7-aa43-4e5a2044648c": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "muốn mua cổ phiếu cần bật máy tính xem đang khớp giá nào",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [392] Google Play f08b2a0d - rating 1 - freeze + buy switches to sell
    "f08b2a0d-fcab-499b-bc86-431d3fa06e91": {
        "incidents": [
            {"incident_type": "failure", "family": "TRADING_ORDER_EXECUTION", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "HIGH",
             "evidence_span": "Áp hay đơ, lặng. Đặt lệnh rất khó. Lệnh mua lại chuyển sang bán.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH", "confidence": "HIGH", "needs_human_review": False,
    },
    # [393] App Store 13379249960 - rating 1 - UI/UX bad
    "13379249960": {
        "incidents": [
            {"incident_type": "friction", "family": "UX_NAVIGATION_COMPLEXITY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "Giao diện rất khó sử dụng, đặt lệnh mất nhiều bước hơn các app khác. Nên học theo giao diện tối giản như ssi",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [394] App Store 13379715404 - rating 5 - praise
    "13379715404": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [395] App Store 13387339116 - rating 5 - praise
    "13387339116": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [396] App Store 13388783260 - rating 5 - praise
    "13388783260": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [397] Google Play 4281fc08 - rating 2 - slow price update
    "4281fc08-f004-4bae-a092-6956ed9eb624": {
        "incidents": [
            {"incident_type": "friction", "family": "MARKET_DATA_STALENESS_ACCURACY", "subtype": "",
             "journey": "TRADING_ORDER_MANAGEMENT", "severity": "MEDIUM",
             "evidence_span": "cập nhật giá chậm so với thị trường, app đúng chán giao dịch rất khó nhìn, tệ nhất là cập nhật giá đúng chậm hơn rùa.",
             "confidence": "HIGH", "new_theme_flag": False, "needs_human_review": False}
        ],
        "sentiment": "NEGATIVE", "complaint_present": True, "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY", "primary_subtype": "", "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM", "confidence": "HIGH", "needs_human_review": False,
    },
    # [398] Google Play 400da6fc - rating 5 - praise
    "400da6fc-3a5f-4c8d-83a4-1acd8a8c4888": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
    },
    # [399] Google Play 3805ef77 - rating 5 - praise
    "3805ef77-5c86-4bf9-b253-8970db98ba67": {
        "incidents": [],
        "sentiment": "POSITIVE", "complaint_present": False, "product_related": "YES",
        "primary_family": "", "primary_subtype": "", "primary_journey": "",
        "max_severity": "NONE", "confidence": "HIGH", "needs_human_review": False,
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
prog["current_batch"] = "Batch 5 (reviews 320-399)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T12:15:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 5 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
