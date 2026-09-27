# Manual Review Sample v0.1

## Mục tiêu

Đọc thủ công các mẫu có chủ đích để kiểm tra Pain Point Taxonomy v0, thử Customer Journey labels, xác định nhu cầu multi-label và hiệu chỉnh severity trước khi phân loại toàn bộ dữ liệu.

Kết quả row-level nằm tại `05_outputs/tables/manual_review_sample_v0.csv`. File hiện có 56 review đã đọc và gán nhãn: 24 review initial sample và 32 review follow-up.

## Phạm vi và cách lấy mẫu

- Population: 736 review trong cửa sổ inclusive `2024-09-22` đến `2026-09-22`.
- Initial sample: 24 review, gồm 12 Google Play và 12 App Store.
- Follow-up sample: 32 review, bổ sung các nhánh Authentication/iOTP, Fee/Pricing, Notification, Customer Support, Security, Feature Request, Trading và Funding.
- Rating bands: `low_1_2`, `mid_3`, `high_4_5`; mỗi tổ hợp `source x rating band` có 4 review.
- Trong mỗi tổ hợp, ưu tiên một review ngắn (`<=20` ký tự), hai review trung bình (`21-120`) và một review dài (`>120`), chọn ổn định theo SHA-256 của `review_id`. App Store rating 3 không có review `<=20` ký tự nên dùng thêm một review trung bình.
- Đọc cả `title` và `review_text`; App Store title đôi khi chứa ngữ cảnh quyết định mà phần nội dung không có.

Đây là mẫu hiệu chỉnh taxonomy, không phải mẫu đại diện thống kê. Không dùng tỷ lệ trong 56 review để ước lượng frequency của 736 review.

## Working Label Rules

### Sentiment

- `Positive`: chỉ khen hoặc thể hiện hài lòng, không có complaint rõ ràng.
- `Negative`: nội dung chính là complaint, lỗi hoặc bất tiện.
- `Mixed`: vừa khen vừa nêu complaint cụ thể.

Rating là metadata tham khảo, không thay thế việc đọc nội dung.

### Severity

- `High`: chặn account access/onboarding, money movement, đặt hoặc hủy lệnh, hoặc làm người dùng không thể tiếp tục core task.
- `Medium`: task còn khả thi nhưng bị chậm, gián đoạn, khó hiểu hoặc dữ liệu cập nhật không kịp.
- `Low`: vấn đề thẩm mỹ, bất tiện nhẹ hoặc complaint quá chung nhưng không cho thấy core task bị ảnh hưởng đáng kể.
- `None`: không có complaint.

### Multi-label

- Gán một `primary_pain_point` theo tác động chính.
- Dùng `secondary_pain_points` khi review có vấn đề độc lập thứ hai hoặc nguyên nhân kỹ thuật hỗ trợ cho pain point chính.
- Không suy diễn category chỉ từ rating.

## Kết quả mẫu

### Sentiment

| Label | Reviews |
|---|---:|
| Negative | 45 |
| Mixed | 5 |
| Positive | 6 |

### Severity

| Label | Reviews |
|---|---:|
| High | 15 |
| Medium | 30 |
| Low | 5 |
| None | 6 |

### Primary label

| Primary label | Reviews |
|---|---:|
| Performance / Reliability | 9 |
| Positive / General Satisfaction | 5 |
| UX / Navigation / Complexity | 4 |
| Product / Portfolio Information | 6 |
| Trading / Order Execution | 7 |
| Fee / Pricing | 3 |
| Onboarding / KYC / Verification | 2 |
| Deposit / Withdrawal / Transfer | 6 |
| Customer Support | 4 |
| Community / Moderation (candidate) | 1 |
| Authentication / iOTP | 5 |
| Localization / Language (candidate) | 1 |
| Notification / Communication (candidate) | 1 |
| Security / Account Protection (candidate) | 1 |
| Feature Request (candidate) | 1 |

Các count trên là combined count của 56 review và chỉ mô tả sample, không phải kết quả frequency analysis.

## Phát hiện cho Taxonomy

1. `Positive / General Satisfaction` không phải pain point. Nên chuyển thành `no_pain_point` hoặc outcome riêng; sentiment đã biểu diễn chiều tích cực. MR-002, MR-003, MR-004 và MR-016 là positive thuần túy.
2. Cần cho phép multi-label. MR-006 có cả thông báo giao dịch chậm và hiển thị lãi/lỗ rối; MR-011 có lag và không hủy được lệnh; MR-017 có verification bị treo dẫn tới không đăng ký được.
3. Cần thêm candidate `Community / Moderation`. MR-005 đánh giá app tích cực nhưng phản ánh lăng mạ trong cộng đồng. Category hiện tại không bao phủ vấn đề này.
4. `Notification / Communication` là candidate cần kiểm tra thêm. MR-006 phản ánh email giao dịch đến chậm, nhưng một review chưa đủ để tạo category final.
5. Cần rule tách `Performance`, `Product / Portfolio Information` và `UX`: toàn app lag/crash/đơ là Performance; dữ liệu giá/NAV/lãi lỗ sai hoặc chậm cập nhật là Product Information; không tìm, đọc hoặc thao tác được do bố cục/navigation là UX.
6. Cần rule tách `Trading / Order Execution` và UX. Không đặt/hủy/khớp được lệnh là Trading; thao tác khó nhưng vẫn thực hiện được có thể là Trading primary và UX secondary.
7. Severity không thể suy ra từ rating. MR-011 có rating 3 nhưng được gán High vì không hủy được lệnh; MR-013 có rating 4 nhưng vẫn có complaint Medium.
8. Classification cho App Store phải đọc cả title và content. MR-008 chỉ xác định được `Customer Support` từ title “Không có nhân viên hỗ trợ”; content “Dịch vụ kém” không đủ cụ thể.
9. `Authentication / iOTP` xuất hiện rõ trong follow-up sample. Vẫn cần targeted sample cho các biến thể khác như iOTP, password reset và QR login trước khi freeze category.

## Kết quả Follow-up Sample

Follow-up sample có 29 Negative, 2 Mixed và 1 Positive review. Severity gồm 11 High, 18 Medium, 2 Low và 1 None. Các category mới/candidate đã được kiểm tra trực tiếp gồm Authentication/iOTP, Localization/Language, Notification/Communication, Security/Account Protection và Feature Request.

Các case đáng chú ý:

- Account access bị chặn: MR-025 đến MR-028, đặc biệt MR-026 và MR-042 cho thấy cần tách lỗi đăng nhập khỏi chính sách bảo mật quá cứng.
- Money movement: MR-041, MR-043, MR-053 đến MR-056 cho thấy Funding cần phân biệt transfer unavailable, withdrawal blocked, held funds và unexplained balance loss.
- Trading core task: MR-049 đến MR-052 cho thấy không đặt/sửa/hủy/khớp được lệnh nên là High dù lý do kỹ thuật có thể là performance hoặc UX.
- Multi-label: MR-036 có performance, UX, stale information và notification; MR-051 có trading, UX và market-data gap; MR-056 có funding, trading và fee.
- Không được coi các từ “lừa đảo” trong MR-029, MR-043 hoặc MR-054 là kết luận fraud. Đây là perception/complaint cần đối chiếu transaction log hoặc actual journey.

## Journey Labels Thử Nghiệm

Sample sử dụng các journey sau:

- `Account Opening / KYC`
- `Trading / Order Management`
- `Funding / Cash Transfer`
- `Product Discovery / Market Data`
- `Portfolio / Performance Tracking`
- `Customer Support`
- `Community / Social` (candidate)
- `General / Cross-journey`

`General / Cross-journey` chỉ dùng khi review nói về toàn app hoặc không đủ bằng chứng để xác định một bước cụ thể. Fee/pricing hiện được map vào journey nơi phí phát sinh; chưa tạo một journey “Fee” riêng vì fee là thuộc tính của trải nghiệm, không phải một bước hành trình.

## Việc cần làm tiếp

1. Lấy targeted sample cho `Authentication / iOTP`, security concern, feature request, fee transparency, customer support và notification để kiểm tra category ít xuất hiện.
2. Chuyển `Positive / General Satisfaction` ra khỏi pain-point taxonomy và thêm trường `complaint_present` hoặc `no_pain_point`.
3. Viết inclusion/exclusion rule và ví dụ biên cho từng pain point và journey.
4. Chốt cách xử lý multi-label và giới hạn số secondary labels.
5. Cho reviewer thứ hai gán độc lập cùng sample, đối chiếu disagreement trước khi freeze taxonomy.
