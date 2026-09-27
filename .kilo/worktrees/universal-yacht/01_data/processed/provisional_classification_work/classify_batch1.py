"""Classify Batch 1 (reviews 0-79) of remaining 636 reviews semantically."""
import csv
import json
from pathlib import Path

WORK = Path("01_data/processed/provisional_classification_work")

# Read remaining reviews
with open(WORK / "remaining_reviews_sorted.csv", encoding="utf-8-sig") as f:
    remaining = list(csv.DictReader(f))

batch = remaining[0:80]

# Classification decisions for each review (semantic, evidence-based)
# Format: list of incident dicts per review; empty list = no incident
# Each incident: {incident_type, family, subtype, journey, severity, evidence_span, confidence, new_theme_flag, needs_human_review}

CLASSIFICATIONS = {
    # [0] App Store 11752256565 - rating 5 - "App tốt" + "105CO89678 sử dụng ổn" - generic praise + referral
    "11752256565": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [1] Google Play e75d95f1 - rating 5 - "Ứng dụng đầy đủ truy cập thông minh nhanh dễ sử dụng" - generic praise
    "e75d95f1-2837-488e-85ec-c20bba821bb3": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [2] Google Play 0dcd9a0e - rating 5 - "105CC02656 tôi thích bảng giá" - praise + referral
    "0dcd9a0e-9301-48c4-81f3-090673b9eec6": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [3] Google Play 6bf6cb60 - rating 5 - "App dùng ok nhé" - generic praise
    "6bf6cb60-e329-43d4-bb87-121838ade2d8": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [4] App Store 11761949465 - rating 5 - "Tuyệt vời" + praise + referral
    "11761949465": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [5] Google Play 4b71fea7 - rating 1 - Techcombank app comparison complaint
    "4b71fea7-84a2-4154-8d2d-5c42a17b0c85": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Cùng một ngân hàng (Techcom), nhưng app ngân hàng và app chứng khoán đúng là một trời một vực. Bao nhiêu năm chả cải thiện gì.",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [6] Google Play 802d4076 - rating 1 - face auth lighting bug + WebView quality
    "802d4076-b5c5-4e2d-948f-29e654c7b257": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "AUTHENTICATION_IOTP",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "Chụp ảnh xác thực khuôn mặt cứ yêu cầu chụp chỗ sáng trong khi đang bật cả 10 bóng đèn.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Ứng dụng kiểu đơn giản là nhúng cái WebView để sử dụng, đem lại trải nghiệm TỒI TỆ cho người dùng.",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [7] Google Play 2b3ebee6 - rating 5 - "Dễ sử dụng" - generic praise
    "2b3ebee6-b34e-4e99-9fd6-46bbf8ea3e47": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [8] App Store 11767116568 - rating 5 - referral code only
    "11767116568": {
        "incidents": [],
        "sentiment": "NEUTRAL",
        "complaint_present": False,
        "product_related": "NO",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [9] App Store 11769185523 - rating 5 - "Tôi yêu việt nam" + referral - off-topic
    "11769185523": {
        "incidents": [],
        "sentiment": "NEUTRAL",
        "complaint_present": False,
        "product_related": "NO",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [10] Google Play 95d102f4 - rating 1 - CCCD update failure
    "95d102f4-de7e-4a0d-aaea-c51a4fcb0255": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Có mỗi cái cập nhật cccd mà làm đi làm lại ko được.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [11] App Store 11777958926 - rating 5 - referral only
    "11777958926": {
        "incidents": [],
        "sentiment": "NEUTRAL",
        "complaint_present": False,
        "product_related": "NO",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [12] App Store 11779920813 - rating 2 - login freeze
    "11779920813": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "Sáng nay đăng nhập đơ, không vào được.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [13] Google Play 7cdcafac - rating 5 - referral + praise
    "7cdcafac-2e0c-4302-8d73-c246fc2323a9": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [14] App Store 11787725265 - rating 1 - update breaks app
    "11787725265": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Update xong không vào được app, mấy lần trước cũng vậy, update xong là lỗi",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [15] Google Play a4f73b4f - rating 5 - spam referral + CCCD update slow
    "a4f73b4f-11b7-42b5-93f1-87783249b116": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Dịch vụ đăng ký dữ liệu căn cước online quá chậm, làm cả tháng chả xong",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "MIXED",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [16] App Store 11800367652 - rating 1 - auto logout
    "11800367652": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "Giờ cứ vào là văng ra",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [17] Google Play 7de5b0e6 - rating 5 - referral + praise
    "7de5b0e6-2b87-438f-9d13-2d193d871ce2": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [18] App Store 11805859173 - rating 1 - slow transactions
    "11805859173": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "TRADING_ORDER_MANAGEMENT",
                "severity": "MEDIUM",
                "evidence_span": "giao dịch lâu mà đợi như chờ chồng chiến tranh về",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [19] Google Play 45435afe - rating 1 - camera error CCCD update
    "45435afe-152e-4913-bdee-e39eb1804c0a": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Không thể bật máy ảnh để thay đổi thông tin cccd, luôn báo lỗi và yêu cầu khởi động lại app",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [20] App Store 11809107324 - rating 5 - "OK" + "Được" - generic praise
    "11809107324": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [21] Google Play d6b5be90 - rating 1 - CCCD update failure + CSKH comparison
    "d6b5be90-d178-452d-8396-ef0be44bab81": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "tôi đã yêu cầu cập nhật cccd mới của tôi trên app mà không được",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "nhân viên CSKH của CTY chứng khoán FPTS chỉ gọi điện thoại & hướng dẫn tôi trong vòng 5 phút thì đã cập nhật cccd mới của tôi rồi",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [22] Google Play 797721a8 - rating 1 - camera conflict CCCD
    "797721a8-d105-4218-ac7a-51cd1a22f9cf": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "app mở camera chụp hình xác nhận tài khoảng ko đc yêu câu khởi động lại.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [23] App Store 11813796447 - rating 1 - security: no password/face ID required
    "11813796447": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "SECURITY_ACCOUNT_PROTECTION",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "Version hiện tại có thể đăng nhập tự do, không cần nhập mật khẩu hoặc face ID - trong cả 2 trường hợp cài đặt dùng face ID để đăng nhập và không dùng.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "SECURITY_ACCOUNT_PROTECTION",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [24] Google Play a6034dee - rating 1 - review reward scam
    "a6034dee-e8e0-402f-ac3b-e4cebefc1248": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "TCBS lừa đảo kêu đánh giá App trả 30k, rồi không trả.",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [25] App Store 11820582267 - rating 1 - auto deduct margin
    "11820582267": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "NOTIFICATION_COMMUNICATION",
                "subtype": "",
                "journey": "FUNDING_CASH_TRANSFER",
                "severity": "HIGH",
                "evidence_span": "Tự động trừ tiền đã nạp vào ký quỹ mà không thông báo",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION",
        "primary_subtype": "",
        "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [26] Google Play bad1a7a5 - rating 1 - OTP slow
    "bad1a7a5-44f2-46eb-aa33-77442bd0448d": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "AUTHENTICATION_IOTP",
                "subtype": "",
                "journey": "AUTHENTICATION_IOTP" if False else "TRADING_ORDER_MANAGEMENT",
                "severity": "HIGH",
                "evidence_span": "mã otp gửi chậm là lỡ thời gian giao dịch",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP",
        "primary_subtype": "",
        "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [27] App Store 11836640608 - rating 1 - referral program non-payment
    "11836640608": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Tcbs đảo các chương trình Review/Giới thiệu, xong không thanh toán.",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [28] Google Play 5da9ec21 - rating 1 - app slow + auto support poor
    "5da9ec21-517e-459b-b34d-8661408fc812": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "App rất nặng, tốc độ xử lý chậm và thường xuyên phải Load lại.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Hỗ trợ xử lý tự động cho khách hàng kém.",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [29] App Store 11839386523 - rating 1 - macOS M3 not working
    "11839386523": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "may mac m3 khong hien thi duoc thong tin dang nhap",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [30] Google Play c9e1400e - rating 5 - "Rõ ràng chi tiết" - generic praise
    "c9e1400e-730c-4c4e-9202-a599402aa609": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [31] Google Play 4e83db00 - rating 5 - "Ok" - generic praise
    "4e83db00-f249-4eed-aa42-7c066be696aa": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [32] Google Play cbbc87cf - rating 1 - "Tệ" - vague negative
    "cbbc87cf-77ee-4fec-931e-ea3e9a56ba2a": {
        "incidents": [
            {
                "incident_type": "unclear",
                "family": "OTHER",
                "subtype": "",
                "journey": "UNKNOWN",
                "severity": "LOW",
                "evidence_span": "Tệ",
                "confidence": "LOW",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "UNCLEAR",
        "primary_family": "OTHER",
        "primary_subtype": "",
        "primary_journey": "UNKNOWN",
        "max_severity": "LOW",
        "confidence": "LOW",
        "needs_human_review": True,
    },
    # [33] App Store 11864397009 - rating 1 - OTP not sent + CSKH unreachable
    "11864397009": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "AUTHENTICATION_IOTP",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "App khônh gửi otp về. Không vào được tài khoảng.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "HIGH",
                "evidence_span": "Tìm bên hỗ trợ không ra. Số điện thoại cskh gọi cũng như không",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [34] Google Play e3f5cf46 - rating 1 - review reward not paid
    "e3f5cf46-2491-45ef-9268-c516fff48ea3": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Bảo đánh giá dc ixu, vài tháng chả thấy đâu",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [35] App Store 11871877953 - rating 1 - AI CSKH complaint
    "11871877953": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Liên quan tới tài chính mà đem Ai ra chăm sóc và nói chuyện với khách hàng. Rất bực mình",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [36] App Store 11871881939 - rating 1 - AI hotline complaint
    "11871881939": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Tổng đài hết sức coi thường khách hàng khi lôi Ai ra hỗ trợ khách hàng",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [37] Google Play 9e4da7e2 - rating 5 - spam referral only
    "9e4da7e2-5d72-4512-8797-ab7151a2c624": {
        "incidents": [],
        "sentiment": "NEUTRAL",
        "complaint_present": False,
        "product_related": "NO",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [38] Google Play 4277ac82 - rating 1 - iChat locked without reason
    "4277ac82-b4c7-48b8-a1c3-18f4164e9ff0": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "HIGH",
                "evidence_span": "Tự nhiên khóa ichat của khách không lý do, lạm quyền chèn ép người dùng",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [39] App Store 11894826169 - rating 1 - hard to use + freeze
    "11894826169": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Khó dùng và hay treo",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [40] App Store 11902304773 - rating 5 - praise Power BI feature
    "11902304773": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [41] Google Play 4bf366e1 - rating 1 - customer info update slow
    "4bf366e1-0727-40b7-bff3-aa519707fdf1": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Cập nhật thay đổi thông tin KH quá lâu, đã lập lệnh điều chỉnh từ 11.10, hẹn dự kiến hoàn tất 21.10 nhưng đến giờ 5.11 vẫn chưa xong",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [42] Google Play 20eca2ba - rating 1 - policy complaint vague
    "20eca2ba-c0a0-449e-ba64-0e62611515ff": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Chính sách hút máu giải quyết vô lý, giải quyết cho khách hàng cứ như không giải quyết",
                "confidence": "LOW",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "LOW",
        "needs_human_review": True,
    },
    # [43] App Store 11940079131 - rating 1 - realtime chart broken + data not auto-refresh
    "11940079131": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MARKET_DATA_STALENESS_ACCURACY",
                "subtype": "",
                "journey": "PRODUCT_DISCOVERY_MARKET_DATA",
                "severity": "HIGH",
                "evidence_span": "Bấm vào chi tiết realtime toàn hiện bảng chữ cái lên, dữ liệu mỗi lần vào app đều không tự cập nhật. Toàn phải tắt hẳn mở lại mới có data",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY",
        "primary_subtype": "",
        "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [44] Google Play fc45dc94 - rating 2 - CCCD update slow + bot CSKH
    "fc45dc94-05b8-4eb1-ba80-35472fdb61bd": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Cập nhật cccd từ 22/10 đến nay chưa xong.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Zalo/FB/ tổng đài toàn nói chuyện với bot.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [45] App Store 11947847736 - rating 1 - rotation broken on price chart
    "11947847736": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "PRODUCT_DISCOVERY_MARKET_DATA",
                "severity": "MEDIUM",
                "evidence_span": "App không xoay ngay được khi xem bảng giá và đồ thị. Xoá app cài lại vẫn bị",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS",
        "primary_subtype": "",
        "primary_journey": "PRODUCT_DISCOVERY_MARKET_DATA",
        "max_severity": "MEDIUM",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [46] Google Play 6b3b31df - rating 1 - iOTP registration fails + AI CSKH poor
    "6b3b31df-5713-450f-80fb-32ef3ce8c5c5": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "AUTHENTICATION_IOTP",
                "subtype": "",
                "journey": "LOGIN_AUTHENTICATION",
                "severity": "HIGH",
                "evidence_span": "Không thể đăng ký iOTP để giao dịch.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Chăm sóc khách hàng A.I ko hỗ trợ được. Còn nhân viên thì quá hời hợt",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AUTHENTICATION_IOTP",
        "primary_subtype": "",
        "primary_journey": "LOGIN_AUTHENTICATION",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [47] Google Play 54721d43 - rating 1 - CCCD verification incomplete
    "54721d43-fdc9-44d4-8e09-ae6f201e72a7": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "ONBOARDING_KYC",
                "subtype": "",
                "journey": "ACCOUNT_OPENING_KYC",
                "severity": "HIGH",
                "evidence_span": "nội xác minh cccd mà còn làm ko xong thì làm gì ăn",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ONBOARDING_KYC",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [48] Google Play de1bacde - rating 1 - spam calls complaint
    "de1bacde-5a2d-4fa0-a39c-2f1c03f716cd": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "NOTIFICATION_COMMUNICATION",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "MEDIUM",
                "evidence_span": "Bọn này gọi điện làm phiền liên tục mọi người nên né bọn này ra!",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "NOTIFICATION_COMMUNICATION",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [49] Google Play c3bb50f4 - rating 5 - "Ok hay đấy" - generic praise
    "c3bb50f4-57ac-4536-8287-4101d6754c58": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [50] Google Play a7799e9c - rating 1 - lag on flagship phone + features not useful
    "a7799e9c-cd03-481b-a4d6-edcdabdb4f2f": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Giật, lag, mặc dù dùng điện thoại cấu hình cao (flagship).",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "unmet_need",
                "family": "MARKET_RESEARCH_RECOMMENDATION_UTILITY",
                "subtype": "",
                "journey": "PRODUCT_DISCOVERY_MARKET_DATA",
                "severity": "MEDIUM",
                "evidence_span": "Nhiều tính năng nhưng chưa hữu dụng với người dùng",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [51] Google Play 6025ead0 - rating 2 - "Ứng dụng hay lỗi" - vague
    "6025ead0-ff94-4e25-a54e-954e4535bed5": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Ứng dụng hay lỗi",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [52] Google Play 7f810ad3 - rating 1 - no human support, AI can't solve
    "7f810ad3-3cf2-482f-a672-724c4708c9ff": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "AI_SUPPORT_CONTEXT_QUALITY",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "HIGH",
                "evidence_span": "Ko có nhân viên hỗ trợ, AI ko giải quyết được vấn đề!!",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "AI_SUPPORT_CONTEXT_QUALITY",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [53] App Store 11989241555 - rating 1 - sell order fails despite balance
    "11989241555": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "TRADING_ORDER_EXECUTION",
                "subtype": "",
                "journey": "TRADING_ORDER_MANAGEMENT",
                "severity": "HIGH",
                "evidence_span": "Mua được nhưng lệnh bán không được. Trong khi mục tài sản vẫn hiện số dư, mà lúc đặt lệnh bán lại hiện lỗi không đủ số dư",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION",
        "primary_subtype": "",
        "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [54] Google Play 29d490fd - rating 5 - spam referral + CCCD update slow (duplicate of 41)
    "29d490fd-c15d-4be9-99d5-10022d6c23de": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Cập nhật thay đổi thông tin KH quá lâu, đã lập lệnh điều chỉnh từ 11.10, hẹn dự kiến hoàn tất 21.10 nhưng đến giờ 5.11 vẫn chưa xong",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "MIXED",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [55] App Store 11996760927 - rating 1 - hard to use UI
    "11996760927": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "App có giao diện khó sử dụng",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [56] App Store 12004038909 - rating 1 - "Lỗi liên tục" + "1 sao" - vague
    "12004038909": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Lỗi liên tục",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [57] App Store 12004133798 - rating 1 - afternoon session can't access
    "12004133798": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "29/11 nguyên phiên chiều không vào được app.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [58] Google Play 052e8a5a - rating 1 - app error, can't trade
    "052e8a5a-ce1f-4184-b7b6-0daa2af90d13": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "TRADING_ORDER_MANAGEMENT",
                "severity": "HIGH",
                "evidence_span": "App lỗi, k giao dịch đc",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [59] Google Play c3f153ed - rating 1 - super slow + registration never completes
    "c3f153ed-ae52-44b1-a794-96f8f5f7ff2b": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "App siêu chậm. Siêu lag.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "failure",
                "family": "ONBOARDING_KYC",
                "subtype": "",
                "journey": "ACCOUNT_OPENING_KYC",
                "severity": "HIGH",
                "evidence_span": "Đăng kí mãi không xong",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [60] Google Play 446d8547 - rating 5 - "Good" - generic praise
    "446d8547-093a-4cc5-ae1d-66fb292eb06b": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [61] Google Play 56c6cec9 - rating 2 - slow matching + UI errors
    "56c6cec9-3a65-4190-82eb-bca71203b087": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "TRADING_ORDER_EXECUTION",
                "subtype": "",
                "journey": "TRADING_ORDER_MANAGEMENT",
                "severity": "MEDIUM",
                "evidence_span": "Khớp lệnh lâu",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "giao diện người dùng hay lỗi",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "TRADING_ORDER_EXECUTION",
        "primary_subtype": "",
        "primary_journey": "TRADING_ORDER_MANAGEMENT",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [62] Google Play 4ffa38c7 - rating 1 - hard to contact advisor
    "4ffa38c7-3d75-4382-bda6-a59c38a086c5": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "CUSTOMER_SUPPORT",
                "subtype": "",
                "journey": "CUSTOMER_SUPPORT",
                "severity": "HIGH",
                "evidence_span": "Liên hệ vs tư vấn viên khó hơn gọi cho tổng thống",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "CUSTOMER_SUPPORT",
        "primary_subtype": "",
        "primary_journey": "CUSTOMER_SUPPORT",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [63] Google Play afc773f6 - rating 1 - update breaks app
    "afc773f6-3f0d-4521-b3d9-b4cb65b7a359": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Mỗi lần hệ thống cập nhật là bị lỗi không sử dụng được.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [64] Google Play e122e8d9 - rating 2 - UI comparison complaint
    "e122e8d9-d3dd-4724-9d97-68a12f9d7cfb": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Thực sự các bạn nên học giao diện của mbs ! Nhìn các bạn rất khó và ko tiện ích",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [65] Google Play 4d26c12f - rating 1 - Android 8.1 install fails
    "4d26c12f-b791-4ea2-8aef-733060a10ec0": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Android 8.1 không cài được",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [66] Google Play 12b10ee3 - rating 1 - forced FPT digital signature
    "12b10ee3-52df-494b-b46c-547c6b279a3c": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "DIGITAL_SIGNATURE_FLOW",
                "subtype": "",
                "journey": "ACCOUNT_OPENING_KYC",
                "severity": "HIGH",
                "evidence_span": "Sau khi đăng ký và kích hoạt tài khoản, app yêu cầu đăng ký chữ ký số cá nhân của FPT để ký HĐ. Không thể thoát khỏi màn hình đăng ký này để sử dụng chức năng khác.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "DIGITAL_SIGNATURE_FLOW",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_OPENING_KYC",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [67] App Store 12084617137 - rating 5 - "Không chê điểm gì" + "6 sao" - praise
    "12084617137": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [68] Google Play 52d4ce83 - rating 1 - CCCD update fails
    "52d4ce83-3408-4752-9713-0b6523a58a86": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
                "subtype": "",
                "journey": "ACCOUNT_PROFILE_MAINTENANCE",
                "severity": "HIGH",
                "evidence_span": "Không cập nhật được căn cước",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "ACCOUNT_RECOVERY_PROFILE_CHANGE",
        "primary_subtype": "",
        "primary_journey": "ACCOUNT_PROFILE_MAINTENANCE",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [69] App Store 12098535718 - rating 1 - lag/freeze
    "12098535718": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "3 ngày lag 7 ngày đơ",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "PERFORMANCE_RELIABILITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [70] Google Play 402640bc - rating 1 - withdrawal blocked 48h
    "402640bc-cfa8-409e-95c8-fecd62daaa30": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "DEPOSIT_WITHDRAWAL_TRANSFER",
                "subtype": "",
                "journey": "FUNDING_CASH_TRANSFER",
                "severity": "HIGH",
                "evidence_span": "Cứ lâu lâu thích là khóa tính năng rút tiền (khóa 48h lun mới chịu) của người ta, làm nhỡ bao nhiêu việc.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER",
        "primary_subtype": "",
        "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [71] App Store 12126154861 - rating 1 - MacBook Air M1 can't open
    "12126154861": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Không mở được app trên MacBook Air M1",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [72] Google Play 4e53832e - rating 1 - VSD balance not shown + ghost order
    "4e53832e-1fa8-4c1d-b05f-19a3ea2c0afb": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "PORTFOLIO_TRACKING" if False else "MARKET_DATA_STALENESS_ACCURACY",
                "subtype": "",
                "journey": "PORTFOLIO_TRACKING",
                "severity": "HIGH",
                "evidence_span": "sáng 9h10 tiền cọc vẫn còn trong VSD nhưng trên app không hiện làm tôi không đặt được lệnh.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "failure",
                "family": "TRADING_ORDER_EXECUTION",
                "subtype": "",
                "journey": "TRADING_ORDER_MANAGEMENT",
                "severity": "HIGH",
                "evidence_span": "Trưa 11h bấm hủy hết lệnh, rõ ràng ngón tay tôi không đưa lên ô đặt lệnh nhưng vẫn lag và vào Long. Chưa kể có những lúc lag k đặt được lệnh.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MARKET_DATA_STALENESS_ACCURACY",
        "primary_subtype": "",
        "primary_journey": "PORTFOLIO_TRACKING",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [73] Google Play abff860a - rating 1 - messy, lag, errors
    "abff860a-3329-408e-a188-cf64dac8a665": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "UX_NAVIGATION_COMPLEXITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "Ứng dụng rối nuồi khó sử dụng",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            },
            {
                "incident_type": "friction",
                "family": "PERFORMANCE_RELIABILITY",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "MEDIUM",
                "evidence_span": "lag, lỗi",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "UX_NAVIGATION_COMPLEXITY",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "MEDIUM",
        "confidence": "MEDIUM",
        "needs_human_review": False,
    },
    # [74] Google Play 033b8a01 - rating 2 - icon color request
    "033b8a01-f565-4002-a7dc-d7432622c677": {
        "incidents": [
            {
                "incident_type": "feature_request",
                "family": "OTHER",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "LOW",
                "evidence_span": "Cập nhật lên Icon màu xanh cho phong thủy đi ad ak",
                "confidence": "HIGH",
                "new_theme_flag": True,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEUTRAL",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "OTHER",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "LOW",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [75] Google Play 0e006d81 - rating 5 - "Tốt" - generic praise
    "0e006d81-5f56-4aa0-a8c0-74344ace1672": {
        "incidents": [],
        "sentiment": "POSITIVE",
        "complaint_present": False,
        "product_related": "YES",
        "primary_family": "",
        "primary_subtype": "",
        "primary_journey": "",
        "max_severity": "NONE",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [76] Google Play c795a0ec - rating 1 - update breaks compatibility
    "c795a0ec-2772-46c0-9315-375ef7f4d185": {
        "incidents": [
            {
                "incident_type": "failure",
                "family": "MOBILE_TABLET_RESPONSIVENESS",
                "subtype": "",
                "journey": "GENERAL_CROSS_JOURNEY",
                "severity": "HIGH",
                "evidence_span": "Đang dùng bình thường tự nhiên nâng cấp ứng dụng làm cho ko tương thích với máy.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "MOBILE_TABLET_RESPONSIVENESS",
        "primary_subtype": "",
        "primary_journey": "GENERAL_CROSS_JOURNEY",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [77] App Store 12161401216 - rating 1 - high fees/tax
    "12161401216": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "FEE_PRICING",
                "subtype": "",
                "journey": "FUNDING_CASH_TRANSFER",
                "severity": "HIGH",
                "evidence_span": "Lãi 3 triệu trừ thuế phí hết còn vài trăm nghìn.",
                "confidence": "HIGH",
                "new_theme_flag": False,
                "needs_human_review": False,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "FEE_PRICING",
        "primary_subtype": "",
        "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH",
        "confidence": "HIGH",
        "needs_human_review": False,
    },
    # [78] App Store 12166129599 - rating 1 - scam accusation
    "12166129599": {
        "incidents": [
            {
                "incident_type": "friction",
                "family": "DEPOSIT_WITHDRAWAL_TRANSFER",
                "subtype": "",
                "journey": "FUNDING_CASH_TRANSFER",
                "severity": "HIGH",
                "evidence_span": "Lừa đảo giam tiền của người dùng sau khi nhận chuyển khoản",
                "confidence": "MEDIUM",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "YES",
        "primary_family": "DEPOSIT_WITHDRAWAL_TRANSFER",
        "primary_subtype": "",
        "primary_journey": "FUNDING_CASH_TRANSFER",
        "max_severity": "HIGH",
        "confidence": "MEDIUM",
        "needs_human_review": True,
    },
    # [79] App Store 12166276133 - rating 1 - "app ngu như đầu cu" - vague insult
    "12166276133": {
        "incidents": [
            {
                "incident_type": "unclear",
                "family": "OTHER",
                "subtype": "",
                "journey": "UNKNOWN",
                "severity": "LOW",
                "evidence_span": "app ngu như đầu cu",
                "confidence": "LOW",
                "new_theme_flag": False,
                "needs_human_review": True,
            }
        ],
        "sentiment": "NEGATIVE",
        "complaint_present": True,
        "product_related": "UNCLEAR",
        "primary_family": "OTHER",
        "primary_subtype": "",
        "primary_journey": "UNKNOWN",
        "max_severity": "LOW",
        "confidence": "LOW",
        "needs_human_review": True,
    },
}

# Build review-level and incident-level rows
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

# Append to checkpoint files
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

# Update progress
with open(WORK / "classification_progress.json") as f:
    prog = json.load(f)
prog["new_semantically_classified_reviews"] += len(completed_keys)
prog["completed_total"] = prog["phase_b_reused_reviews"] + prog["new_semantically_classified_reviews"]
prog["remaining_reviews"] = prog["total_target_reviews"] - prog["completed_total"]
prog["current_batch"] = "Batch 1 (reviews 0-79)"
prog["last_completed_review_key"] = completed_keys[-1]
prog["updated_at"] = "2026-09-23T11:55:00"
with open(WORK / "classification_progress.json", "w") as f:
    json.dump(prog, f, indent=2)

print(f"Batch 1 done: {len(completed_keys)} reviews, {len(incident_rows)} incidents")
print(f"Progress: {prog['completed_total']}/{prog['total_target_reviews']} ({prog['remaining_reviews']} remaining)")
