# Metrics Pack — Day 20

## 00 — Dự án, persona, core job
- **Dự án:** DevPulse AI — AI-Powered Engineering Intelligence & Executive Reporting Platform
- **Persona:** CTO / Head of Engineering (Quản lý cấp cao phụ trách toàn bộ khối kỹ thuật và ngân sách công nghệ)
- **Core job:** "Tôi cần vào jira github kiểm tra xem số lượng feature được ship, các dev đang làm việc tốt không hoặc đọc qua báo cáo của các lead dưới quyền, giải trình với cấp trên về sử dụng AI hiệu quả"

---

## 01 — Core Action Card (+ kết quả tự kiểm 5 tiêu chí)
### Core Action Card
- **Tên hành vi:** Phê duyệt & Xuất Báo cáo Hiệu quả Kỹ thuật & ROI AI (Publish & Export Engineering & AI Impact Review)
- **Actor:** CTO / Head of Engineering
- **Object:** Bản tổng hợp đánh giá Sprint/Tháng (hội tụ dữ liệu Jira delivery, Git activity, báo cáo Team Lead cấp dưới, và chỉ số ROI ứng dụng AI)
- **Trigger:** Kết thúc chu kỳ Sprint (bi-weekly) hoặc lịch họp giao ban với Ban điều hành (Board/CEO) đòi hỏi giải trình hiệu quả ngân sách AI và năng suất ship hàng.
- **Completion rule (Quy tắc hoàn thành):** CTO hoàn tất review các insight tổng hợp, xác nhận/ghi chú đánh giá điều hành và kích hoạt hành động **"Publish & Export/Share Report"** gửi C-suite/Lead cấp dưới (Hệ thống ghi nhận trạng thái báo cáo chuyển thành `PUBLISHED_AND_SHARED`).

### Tự kiểm 5 tiêu chí
1. **Gần core value:** Đạt. Giải quyết trực tiếp bài toán cốt lõi: chuyển hóa dữ liệu vụn vặt (Jira, GitHub, AI cost) thành căn cứ điều hành và chứng cứ giải trình ROI cho cấp trên.
2. **Do user chủ động thực hiện (không phải output hệ thống):** Đạt. CTO trực tiếp kiểm chứng số liệu, bổ sung nhận định quản trị và chủ động bấm xác nhận/xuất báo cáo; hệ thống chỉ chuẩn bị dữ liệu tổng hợp.
3. **Phân biệt với thao tác UI thuần túy:** Đạt. Không tính các hành vi thụ động như "mở dashboard", "xem danh sách commit", hay "click tab Jira". Đây là hành động trao đổi nỗ lực (effort) để chốt báo cáo trách nhiệm (governance accountability).
4. **Có điểm kết thúc rõ ràng để đếm được (Completion rule):** Đạt. Có mốc kết thúc dứt khoát khi bản báo cáo chuyển trạng thái sang `PUBLISHED` kèm event bắn ra `engineering_ai_report_published` có metadata hợp lệ.
5. **Có thể lặp lại theo nhu cầu tự nhiên:** Đạt. Lặp lại định kỳ theo nhịp quản trị tự nhiên: 2 tuần/lần (theo sprint review) hoặc 1 tháng/lần (theo executive board review). 

---

## 02 — Action Nature Card + kết luận cadence
### Action Nature Card
| Thành phần | Câu hỏi & Trả lời |
| :--- | :--- |
| **Actor** | CTO / Head of Engineering (kết hợp cùng các Tech Lead trực thuộc). |
| **Intent** | Kiểm chứng số lượng feature được ship, đánh giá năng suất đội ngũ dev thông qua đối chiếu PRs vs Token usage, và hoàn tất báo cáo minh bạch giải trình ROI AI với ban giám đốc. |
| **Trigger** | **External:** Mốc kết thúc chu kỳ Sprint (bi-weekly) từ Jira/GitHub và lịch họp giao ban Ban điều hành (Board/C-suite hàng tháng).<br>**Internal:** Áp lực tối ưu hóa chi phí token AI và giải tỏa hoài nghi về hiệu quả ứng dụng AI trong quy trình kỹ thuật. |
| **Effort** | **Medium – High:** Dành 15–30 phút cho mỗi phiên review: rà soát biểu đồ tương quan PRs vs Token, đọc ghi chú tóm tắt từ các Tech Lead, bổ sung nhận định quản trị và bấm phê duyệt/xuất bản. |
| **Value timing** | **Immediate:** Nhận ngay bản báo cáo chuẩn hóa, số liệu đối chiếu khách quan để bước vào cuộc họp giao ban.<br>**Cumulative:** Xây dựng bức tranh lịch sử xu hướng năng suất và hệ số ROI công nghệ qua từng quý/năm. |
| **State** | **State-dependent:** Yêu cầu trạng thái chu kỳ sprint hoặc kỳ tháng đã được đóng (dữ liệu Jira story points, GitHub PR merges, và API token logs từ proxy đã đồng bộ đầy đủ). |
| **Dependency** | Phụ thuộc vào hạ tầng tích hợp: DevPulse AI Proxy (tracking token), GitHub API (tracking PRs/commits), Jira webhook (tracking delivery), và phản hồi sơ bộ từ Tech Lead cấp dưới. |
| **Repeat condition** | Lặp lại tự nhiên khi chu kỳ làm việc mới kết thúc: chu kỳ Sprint 2 tuần (Bi-weekly) cho kỹ thuật và chu kỳ kế toán/quản trị tháng (Monthly) cho HĐQT. |

### Kết luận cadence
> Đối với **CTO / Head of Engineering**, core action **"Phê duyệt & Xuất Báo cáo Hiệu quả Kỹ thuật & ROI AI"** thường xuất hiện **theo mô hình kết hợp (Hybrid): Bi-weekly (2 tuần/lần) cho nhịp độ Sprint Review kỹ thuật và Monthly (1 tháng/lần) cho nhịp độ Executive Board Review** vì **chu kỳ phân phối phần mềm diễn ra theo Sprint 2 tuần, trong khi chu kỳ quản trị tài chính và đánh giá ROI ngân sách diễn ra hàng tháng; việc ép buộc nhịp sử dụng hàng ngày (DAU) là phản tự nhiên đối với công việc quản trị cấp cao**. Do đó, nhịp đo phù hợp là **Bi-weekly / Monthly** ở cấp **Organization / Engineering Department (B2B Account)**.

---

## 03 — Metric System
### 1. Activation metric
- **Start event:** `organization_onboarded` (CTO tạo Workspace tổ chức và kết nối thành công ít nhất 1 nguồn dữ liệu kỹ thuật: DevPulse AI Proxy hoặc GitHub/Jira).
- **Activation event:** `first_ai_engineering_report_published` (CTO hoặc Tech Lead lần đầu tiên hoàn tất review và xuất bản thành công bản Báo cáo Hiệu quả Kỹ thuật & ROI AI chu kỳ).
- **Time window:** 14 ngày (tương ứng trọn vẹn chu kỳ 1 Sprint kỹ thuật đầu tiên kể từ khi onboard).

### 2. Engagement metric
- **Frequency:** Số lần xuất bản báo cáo hoàn tất trên mỗi tổ chức trong chu kỳ (Target: 2 lần/tháng cho Sprint Review + 1 lần/tháng cho Executive Summary).
- **Depth / Breadth:** 
  - **Depth (Độ sâu):** Tỷ lệ báo cáo có bổ sung ghi chú điều hành (`has_executive_notes == true`) và gắn kèm quyết định tái phân bổ ngân sách/quota token (`has_resource_allocation == true`).
  - **Breadth (Độ rộng):** Tỷ lệ các Squad/Team kỹ thuật trong tổ chức có dữ liệu đối chiếu PR & Token được đưa vào báo cáo tổng hợp (Coverage rate ≥ 80% tổng số dev trong tổ chức).

### 3. North Star Metric (NSM)
- **Công thức:** `Unit of value` + `Quality threshold` + `Frequency`
  - *Unit of value:* Verified AI-Engineering Impact Report (Bản báo cáo đánh giá giao hàng & ROI AI đã được phê duyệt).
  - *Quality threshold:* Đạt chuẩn dữ liệu (bao phủ ≥ 80% developer active, có dữ liệu đối chiếu chéo Jira delivery, GitHub PR merges và AI token proxy, được CTO/Lead ký duyệt).
  - *Frequency:* Hàng tháng (Monthly) hoặc theo nhịp Sprint (Bi-weekly).
- **Định nghĩa NSM:** **Monthly Verified AI-Engineering Reviews Published (Số lượng báo cáo hiệu quả kỹ thuật & ROI AI đạt chuẩn chất lượng được CTO phê duyệt và xuất bản mỗi tháng trên toàn nền tảng).**

### 4. Leading indicators
1. **AI Proxy Integration Coverage:** Tỷ lệ kỹ sư đang gọi AI APIs thông qua DevPulse Proxy (đảm bảo dữ liệu chi phí token đầu vào đầy đủ và phản ánh trung thực thói quen dev).
2. **Tech Lead Sprint Pre-review Rate:** Tỷ lệ Tech Lead cấp dưới hoàn tất xem trước và xác nhận báo cáo sơ bộ của squad mình trước mốc chốt Sprint 24 giờ.
3. **PR-to-Token Attribution Rate:** Tỷ lệ GitHub Pull Requests được gắn nhãn/ánh xạ thành công với các phiên sinh code từ AI Proxy (đo lường độ chính xác của mối tương quan năng suất vs chi phí).

### 5. Counter-metric
- **Chỉ số:** **Phantom Review Rate** (Tỷ lệ báo cáo xuất bản nhưng thời gian review < 60 giây hoặc không ai mở đọc sau xuất bản) & **Code Churn / Gaming PR Rate** (Tỷ lệ PR rỗng, spam commit hoặc PR bị rollback tăng đột biến sau khi áp dụng đo lường).
- **Lý do / Ngưỡng an toàn:** Tránh bẫy Goodhart's Law: CTO click duyệt vội vàng chỉ để lấy chỉ tiêu hình thức, hoặc lập trình viên tìm cách "lách số" bằng cách sinh code AI tràn lan, tạo PR vụn vặt để thổi phồng chỉ số năng suất. *Ngưỡng an toàn:* Thời gian CTO review báo cáo ≥ 3 phút; Tỷ lệ PR bị revert/rollback trong vòng 7 ngày sau merge phải duy trì < 5%; Tỷ lệ báo cáo được mở đọc bởi các bên liên quan sau khi xuất bản ≥ 75%.

---

## 04 — Retention Definition (6 thành phần)
| Thành phần | Định nghĩa chi tiết |
| :--- | :--- |
| **Unit** | **Organization / Engineering Workspace (B2B Account):** Đo lường ở cấp tổ chức kỹ thuật/doanh nghiệp. Việc gia hạn dịch vụ và ứng dụng nền tảng là quyết định tập thể của khối kỹ thuật do CTO dẫn dắt, không đo ở cấp từng lập trình viên đơn lẻ. |
| **Cohort entry** | **Thời điểm đạt Activation:** Tổ chức xuất bản thành công bản báo cáo đầu tiên (`first_ai_engineering_report_published`) trong vòng 14 ngày kể từ khi kết nối hệ thống. Các tổ chức được gom nhóm theo tháng kích hoạt (Monthly Acquisition Cohort, vd: `Cohort 2026-10`). |
| **Return event** | **Thực hiện lặp lại Core Action:** Tổ chức kích hoạt event `ai_engineering_report_published` có `is_verified == true` (CTO hoặc Tech Lead tiếp tục review, phê duyệt và xuất bản báo cáo hiệu quả kỹ thuật & ROI AI cho chu kỳ tiếp theo). |
| **Window** | **Bracketed Monthly / Bi-weekly Windows:** Khung chu kỳ đánh giá chuẩn là **Monthly Brackets (Tháng M+1, M+2, M+3... M+12)** cho quyết định duy trì B2B SaaS, kết hợp theo dõi nhịp vận hành nội bộ theo **Bi-weekly Sprint Windows** (Sprint N+1, N+2). Không sử dụng rolling D7/D30 vì làm méo mó bản chất chu kỳ giao ban. |
| **Threshold** | **≥ 1 Báo cáo Verified được xuất bản mỗi chu kỳ:** Trong mỗi cửa sổ tháng (hoặc sprint), tổ chức phải có ít nhất 1 bản báo cáo đạt chuẩn chất lượng dữ liệu (độ phủ ≥ 80% dev) được xuất bản và chia sẻ đến các bên liên quan. |
| **Segment** | **1. Theo quy mô đội ngũ:** Growth/Scale-up (20–50 devs), Mid-Market (51–200 devs), Enterprise (>200 devs).<br>**2. Theo cường độ chi tiêu AI (Token Spend Tier):** Heavy AI Adopters (> $3,000 token/tháng) vs Moderate/Pilot Adopters (< $1,000 token/tháng). |

---

## 05 — Product Loop
### 1. Sơ đồ Loop (≥ 2 chu kỳ)
```text
[Chu kỳ 1: Sprint N Bi-weekly Review]
Natural Trigger 1: Sprint N kết thúc trên Jira/GitHub; DevPulse tổng hợp báo cáo sơ bộ
→ Core Action 1: CTO cùng Lead review đối chiếu PRs vs Token, ký duyệt xuất bản (engineering_ai_report_published)
→ Immediate Value 1: Nhận diện rõ squad nào tối ưu hiệu quả AI, phát hiện điểm nghẽn review code
→ Saved State / Investment 1: Lưu baseline năng suất Sprint N, điều chỉnh quota token & ghi chú hành động cải tiến

→ Next Natural Trigger 2: Sprint N+1 kết thúc hoặc đến kỳ họp HĐQT tháng; hệ thống tự động so khớp với baseline Sprint N
→ Core Action 2 (Tiếp theo): CTO duyệt báo cáo luỹ kế tháng, kiểm chứng hiệu quả sau cải tiến quy trình
→ Repeat Value 2: Báo cáo giải trình C-suite với dữ liệu xu hướng thuyết phục, bảo vệ ngân sách & củng cố vị thế quản trị
```

### 2. Phân loại Loop
- **Loại loop chính:** **Work-Output Governance & Organizational Habit Loop (Vòng lặp quản trị đầu ra & thói quen tổ chức)** kết hợp **Cross-Functional Collaboration Loop (Mạng lưới phối hợp giữa Tech Lead và CTO)**.
- *Cơ chế:* Đầu ra của kỳ này (quyết định điều phối quota và hành động khắc phục) trở thành đầu vào định chuẩn (saved state/baseline) cho chu kỳ tiếp theo. Tech Lead và CTO cùng tương tác trên một nguồn sự thật dữ liệu, biến công cụ thành nghi thức vận hành chuẩn (standard operating ritual).

### 3. Metric Hypothesis
> Nếu loop này hoạt động, metric **Monthly B2B Retention Rate (Tỷ lệ tổ chức duy trì xuất bản báo cáo verified ở Tháng M+1 và M+2)** sẽ thay đổi theo hướng **tăng từ 45% lên ≥ 75%** trong **vòng 60 ngày sau onboarding**, vì **dữ liệu baseline và lịch sử xu hướng tích lũy từ các chu kỳ trước (saved state) làm cho báo cáo kỳ sau có giá trị so sánh chiến lược vượt trội, tạo ra chi phí chuyển đổi cao (high switching cost) khiến tổ chức không thể từ bỏ sản phẩm.**

---

## 06 — Tracking nhanh (4–8 events + 2 acceptance criteria)
### Bảng Core Events
| Tên event | Ý nghĩa (Value / Hành vi) | Thời điểm ghi nhận | Metric sử dụng |
| :--- | :--- | :--- | :--- |
| `organization_onboarded` | Tổ chức hoàn tất đăng ký workspace và kết nối data source đầu tiên (Proxy/GitHub/Jira). | Ngay khi webhook/API connection đầu tiên trả về status 200. | Activation Start Event, Cohort Entry Base. |
| `proxy_request_logged` | Kỹ sư thực hiện gọi AI API thông qua DevPulse Proxy. | Mỗi khi proxy chuyển tiếp thành công request kèm metadata developer. | AI Proxy Integration Coverage (Leading Indicator #1). |
| `lead_pre_review_submitted` | Tech Lead xem trước dữ liệu squad và xác nhận tính hợp lệ sơ bộ trước mốc chốt sprint. | Tech Lead bấm "Confirm Squad Metrics" trên giao diện. | Tech Lead Sprint Pre-review Rate (Leading Indicator #2). |
| `ai_engineering_report_reviewed` | CTO mở và thực hiện phiên review chi tiết đối chiếu PRs vs Token spend. | Ghi nhận khi CTO kết thúc phiên review với thời gian dwell time tương tác. | Counter-metric (Chống Phantom Review, kiểm tra dwell time ≥ 3 phút). |
| `ai_engineering_report_published` | **Core Action:** CTO phê duyệt chính thức và bấm xuất bản/chia sẻ báo cáo chu kỳ. | Ngay khi trạng thái báo cáo chuyển thành `PUBLISHED_AND_SHARED`. | **North Star Metric (NSM)**, Activation Event, Retention Return Event. |
| `report_stakeholder_viewed` | Thành viên ban giám đốc (CEO/CFO/Board) hoặc dev mở xem link báo cáo đã xuất bản. | Người nhận truy cập và xem chi tiết báo cáo qua link bảo mật hoặc PDF export. | Engagement Breadth / Value Consumption Metric, Counter-metric. |

### Tiêu chí nghiệm thu (Acceptance Criteria)
1. **Schema & Verification Integrity (Chống số liệu rác):** Mọi event `ai_engineering_report_published` bắt buộc phải kèm đầy đủ payload: `{org_id, report_id, sprint_period, dev_coverage_pct, total_token_usd, prs_merged_count, review_duration_seconds, is_verified}`. Nếu `dev_coverage_pct < 80%` hoặc `review_duration_seconds < 60s`, cờ `quality_threshold_met` phải tự động gán `false` và hệ thống không được tính lượt này vào North Star Metric.
2. **Idempotency & Deduplication Rule (Chống spam metric):** Trong cùng một tổ chức (`org_id`) và một chu kỳ đánh giá (`sprint_period`), nếu CTO thực hiện chỉnh sửa hoặc bấm re-publish báo cáo nhiều lần, hệ thống chỉ ghi nhận đúng 1 lần cho NSM và Cohort Retention dựa trên khóa duy nhất `org_id + sprint_period`. Mọi lần bấm sau chỉ ghi nhận log audit kỹ thuật, không làm sai lệch số liệu tăng trưởng.
