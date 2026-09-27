# TCInvest Customer Voice / Review Mining

## 1. Mục tiêu

Project này phục vụ phân tích **public reviews của TCInvest** trên Google Play và App Store.

Câu hỏi nghiên cứu chính:

> Trong public reviews của TCInvest, những pain point nào xuất hiện lặp lại, pain point nào nghiêm trọng nhất, chúng tập trung ở customer journey nào và pain point nào đáng được team kiểm chứng sâu hơn như candidate business problem?

Các đầu ra chính dự kiến:

- Phân loại review theo Customer Journey
- Phân loại theo Pain Point
- Sentiment
- Severity
- Frequency
- Top 5 Complaints
- Representative Reviews
- Candidate Business Problems
- Evidence để handover cho M4/M5

---

# 2. Nguồn dữ liệu

## Google Play

App:

`com.fss.tcbs.mobiletrading`

Collection configs:

- `vi_vn`
- `en_vn`

Primary raw dataset:

`01_data/raw/google_play/2026-09-22_google_play_raw.csv`

Hiện có:

- 3.223 unique reviews
- Review sớm nhất: `13/08/2015`
- Review mới nhất: `21/09/2026`
- Duplicate `reviewId`: 0
- Missing content: 0
- Missing rating: 0
- Missing date: 0
- Missing `app_version`: 459

Collector sử dụng `Sort.NEWEST` và tiếp tục pagination bằng `continuation_token` cho đến khi không còn batch mới.

Không có time filter trong quá trình collection.

---

## App Store

App ID:

`1037255487`

Storefront:

`vn`

Primary raw dataset hiện tại:

`01_data/raw/app_store/2026-09-22_app_store_raw_expanded_v2.csv`

Hiện có:

- 522 unique review IDs
- Duplicate `review_id`: 0
- Review sớm nhất: `14/04/2023`
- Review mới nhất: `14/09/2026`

### Lưu ý về App Store

App Store canonical trước đây chỉ có 447 reviews.

Sau Recency Gap Audit:

- Diagnostic mới tìm thêm 75 review IDs
- 75/75 được xác minh là valid
- Canonical v2 được rebuild thành 522 reviews

Public App Store endpoints có coverage không ổn định theo:

- page
- sort mode
- JSON/XML
- thời điểm request

Do đó 522 reviews hiện tại là:

> Broadest validated union của saved public evidence hiện có.

Không được coi đây là toàn bộ lifetime reviews của TCInvest trên App Store.

---

# 3. Tổng dữ liệu hiện tại

| Source | Reviews |
|---|---:|
| Google Play | 3.223 |
| App Store | 522 |
| **Total** | **3.745** |

Lưu ý:

> 3.745 reviews không đồng nghĩa với 3.745 unique customers.

Public reviewers là self-selected sample và không đại diện cho toàn bộ customer population của TCInvest.

---

# 4. Chuẩn hóa dữ liệu

Hai nguồn đã được đưa về common schema.

Primary standardized files:

- `01_data/interim/google_play_standardized.csv`
- `01_data/interim/app_store_standardized.csv`
- `01_data/interim/reviews_merged_standardized.csv`

Merged dataset:

- 3.745 rows
- Duplicate `(source, review_id)`: 0
- Missing `review_text_raw`: 0
- Missing `rating`: 0
- Missing `review_date`: 0

Global key sử dụng:

`(source, review_id)`

Không assume `review_id` globally unique giữa Google Play và App Store.

---

# 5. Data Quality Audit

Đã hoàn thành Data Quality Audit.

Một số điểm đáng chú ý:

- Very short reviews `≤10 ký tự`: 533
- Exact duplicate-text: 417 records / 69 groups
- Missing `app_version`: 459 reviews
- Suspected spam: 0
- Core fields không có missing / invalid values
- Google Play và App Store có temporal coverage khác nhau
- App Store public endpoint coverage không ổn định

Audit report:

`04_analysis/validation/data_quality_audit.md`

---

# 6. Cleaning

Cleaning đã hoàn thành.

Input:

- 3.745 reviews

Output:

- 3.745 clean reviews
- Rejected rows: 0

Primary clean dataset:

`01_data/processed/reviews_clean_full.csv`

Cleaning rules:

- Không tự động xóa review chỉ vì rất ngắn
- Không xóa exact duplicate text nếu khác `review_id`
- Không remove vì thiếu `app_version`
- Không remove vì rating thấp hoặc cao
- Không coi `collection_locale` là actual review language

Review chỉ bị remove nếu:

- thiếu `review_id`
- thiếu / invalid `review_date`
- rating ngoài 1–5
- `review_text_raw` rỗng / whitespace-only
- được xác định rõ là invalid/spam bằng rule cụ thể

### Text handling

Giữ nguyên:

`review_text_raw`

Tạo thêm:

`review_text_clean`

Chỉ thực hiện cleaning nhẹ:

- trim whitespace
- normalize line break
- collapse repeated whitespace

Không:

- remove dấu tiếng Việt
- translate
- remove emoji
- remove punctuation
- sửa chính tả
- paraphrase

Cleaning log:

`00_docs/methodology/data_cleaning_log.md`

---

# 7. Analysis Time Range

Team đã chốt:

> **24 tháng gần nhất**

Time range:

`22/09/2024 → 22/09/2026`

Theo Temporal Coverage Audit:

- Total: 736 reviews
- Google Play: 403
- App Store: 333

Lý do chọn 24 tháng:

- Gần với trạng thái sản phẩm hiện tại hơn full history
- Sample size vẫn đủ lớn để phân tích
- Google Play và App Store cân bằng hơn đáng kể
- Giảm ảnh hưởng từ historical Google Play reviews từ năm 2015
- Phù hợp với mục tiêu xác định current pain points và candidate business problems

---

# 8. Taxonomy

Hiện đã có Pain Point Taxonomy v0.

File:

`04_analysis/taxonomy/taxonomy_v0.md`

Các nhóm ban đầu:

1. Performance / Reliability
2. UX / Navigation / Complexity
3. Onboarding / KYC / Verification
4. Authentication / iOTP
5. Trading / Order Execution
6. Deposit / Withdrawal / Transfer
7. Customer Support
8. Fee / Pricing
9. Product / Portfolio Information
10. Positive / General Satisfaction

Taxonomy này chưa phải final.

Cần tiếp tục:

- đọc manual sample
- kiểm tra category overlap
- bổ sung category còn thiếu
- chốt Customer Journey taxonomy
- chốt severity rules
- freeze taxonomy trước full classification

---

# 9. Pipeline dự kiến

```text
Data Collection
      ↓
Validation / Provenance Audit
      ↓
Standardization
      ↓
Data Quality Audit
      ↓
Cleaning
      ↓
Select Analysis Time Range
      ↓
Manual Review
      ↓
Refine Taxonomy
      ↓
Sentiment Analysis
      ↓
Topic Modelling
      ↓
Pain Point Classification
      ↓
Customer Journey Mapping
      ↓
Severity
      ↓
Manual Validation
      ↓
Frequency / Rating / Trend Analysis
      ↓
Top 5 Complaints
      ↓
Representative Reviews
      ↓
Candidate Business Problemsgi