# Checkpoint 3 — Cost/Job và Pricing

## Baseline có thể tính lại

Đây là **forecast** ở 10 workspace, không phải 10 khách hiện có. Mỗi workspace thử 4 job/tháng; 75% vượt quality gate cho 3 báo cáo AI-ready. Tổng: 40 thử, **30 hoàn thành**. Khách vẫn review để publish; 10 ca không đạt khách chịu viết lại, không charge. Biến thể A.

Giá first-party [Claude Haiku 4.5](https://platform.claude.com/docs/en/about-claude/pricing), kiểm tra **08/10/2026**: input $1, output $5, cache write 5 phút $1,25, cache read $0,10 / 1M token. Không thấy thời hạn khuyến mại cho model đã chọn. Không tự chuyển sang model mới vì chưa có quality eval tương đương.

Giả định 4 lượt/báo cáo, 8.000 token prefix ổn định, 12.000 fresh token/lượt gồm history và dữ liệu tổng hợp, 2.000 output token/lượt. Prefix vượt minimum 4.096; phải chạy tuần tự trong TTL 5 phút và đo cache hit, không giả định cache chung giữa tenant.

| API cho một job thử | Phép tính | USD |
| --- | --- | ---: |
| Cache write | 8.000 × 1,25 / 1M | 0,010000 |
| Cache read | 3 × 8.000 × 0,10 / 1M | 0,002400 |
| Fresh input | 4 × 12.000 × 1 / 1M | 0,048000 |
| Output | 4 × 2.000 × 5 / 1M | 0,040000 |
| Có cache | Tổng | **0,100400** |
| Không cache | 4 × 20.000 × 1 / 1M + 0,040000 | **0,120000** |

Cache chỉ tiết kiệm **16,33%**, không copy con số 38% của ví dụ ticket. Batch không dùng baseline vì preview on-demand dự kiến trong 15 phút; overnight Batch không cache khoảng $0,060000/API/job thử. $0,050200 là best-case Batch + cache, chỉ hợp lệ nếu đo được cache hit giữa các bước. Không nhận deadline 15 phút cho Batch.

## Đủ năm nhóm chi phí

| Nhóm | Phép tính tháng | USD/tháng |
| --- | --- | ---: |
| API | 40 × 0,1004 | 4,01600 |
| Infra | $80 shared floor + 40 × $8 variable | 400,00000 |
| HITL QA | 40 × 25% × 15/60 × $20/h | 50,00000 |
| Retry | 8% × 4,01600; một lần chạy thêm/ca | 0,32128 |
| Overhead | 8h product maintenance + 7h admin, $20/h | 300,00000 |
| COGS trước overhead | API + Infra + HITL + Retry | **454,33728** |
| Tổng có overhead | COGS + overhead | **754,33728** |

$8 variable/attempt gồm $3 ingestion/DB, $1 storage/egress, $1 observability/eval, $1,50 support trực tiếp, $1,50 collection/FX/tax contingency. Đây là budget chưa có invoice, không phải mức giá nhà cung cấp. $80 shared floor được phân bổ trên 40 attempt: tổng Infra = $10/attempt. Speech, TTS và telephony = 0 vì chỉ xử lý metadata dạng text. Không dùng vector DB/embedding trong scope baseline; đã có SQL aggregates. Không dùng web-search tool trả phí.

QA vendor đã vào COGS. CTO review, quyền ký và 20 phút sửa một ca fail là chi phí khách ở A, không giả là biến mất. Nếu DevPulse nhận managed-service delivery, chuyển B: thêm 10 × 20/60 × $20 = $66,66667/tháng. Giữ mẫu số AI-ready 30 theo convention lab cho kịch bản thận trọng, nhưng nếu bán cả human-completed reports phải định nghĩa lại billing denominator trước khi dùng.

## Năm số bắt buộc

| Chỉ số | Giá trị | Ô |
| --- | ---: | --- |
| Cost/Job COGS | **$15,144576** | `1_Cost_Job!B66`, `2_Pricing!B5` |
| Giá sàn 3× COGS | **$45,433728** | `2_Pricing!B7` |
| Giá đề xuất | **$60/report** | `2_Pricing!B19` |
| Report GM | **74,75904%** | `2_Pricing!B21` |
| Containment tối thiểu GM60 | **47,3268%** | `2_Pricing!B33` |

Fully loaded Cost/Job = **$25,144576** (`1_Cost_Job!B67`). Overhead không là COGS; không gọi contribution sau overhead là GM. Giá sàn lab là 3×COGS, không khẳng định $60 đạt 3×fully-loaded cost. All-in bill $39 + 3×$60 = **$219/workspace/tháng**; forecast blended GM = 79,2540%, contribution sau $300 overhead = 65,5554%. Tính lại các giá trị chính xác từ Excel khi nộp.

Neo giá trị: 3 báo cáo × 10 giờ chuẩn bị tiết kiệm × $40/h = **$1.200/tháng**, ước tính cần stopwatch. Vùng 10–25% = $120–300/tháng; **all-in $219** nằm trong vùng, không chỉ phần usage $180. Lương analyst $2.000/tháng chỉ là neo phụ; không tuyên bố thay cả người. WTP chưa được đo. USD/VND lấy **giá bán 26.160** từ Vietcombank XML ngày 08/10/2026; không dùng tỷ giá giả định 26.000 mẫu.

## Containment stress test và đại số

Ở A: `v = 0.1004 × 1.08 + 10 = 10.108432`, `q = 0.25 × 15/60 × 20 = 1.25`, `e = 0`.

```text
Cost/Job(c) = (v + q) / c = 11.358432 / c
GM >= 0.60  <=> 11.358432 / c <= 60 × 0.40
c >= 11.358432 / 24 = 0.473268
GM < 0.50 when c < 11.358432 / 30 = 0.3786144
```

| Containment | Cost/Job USD | GM |
| ---: | ---: | ---: |
| 50% | 22,716864 | 62,13856% |
| 60% | 18,930720 | 68,44880% |
| 70% | 16,226331 | 72,95611% |
| 80% | 14,198040 | 76,33660% |
| 90% | 12,620480 | 78,96587% |

Đây là **healthy-margin containment**, không phải kế toán breakeven GM=0. Eval hiện tại chưa có; 75% planning nằm trên 47,33% nhưng **không là bằng chứng go-live**. Không mở paid rollout nếu lower confidence bound của eval/pilot chưa vượt ngưỡng.

## Biến giết mô hình và volume stress

Containment sai 2×, 75% xuống 37,5%: Cost/Job **$30,289152**, GM **49,51808%**. Infra gấp đôi cho Cost/Job $28,477909, GM 52,53682%: không đạt GM60 và floor3×. Nếu phải QA mọi report với 60 phút thay vì sample 15 phút, riêng QA $20/attempt khiến mô hình gãy. Không che rủi ro này bằng tăng giá trên giấy.

Ở pilot 3 workspace: 12 attempt, 9 AI-ready; fixed $80 phải chia trên 12, không giữ $10/attempt. COGS = $80 + 12×($8 + $0,108432 + $1,25) = **$192,301184**; Cost/Job **$21,366798**, report GM **64,38867%**, nhưng floor3× = $64,100395 > giá $60. Blended revenue $657, overhead $300 cho contribution chỉ 25,82935%; pilot có thể học được nhưng chưa vượt tất cả pricing gates. Giữ acquisition cap, không gọi pilot là steady-state model đã chứng minh.

Khi zero completed, template trả 0; đó là lỗi presentation, không phải cost bằng 0. Validator phải báo **undefined/reject**, không nhận trạng thái xanh. Không sửa formula xám của template để che khác biệt; ghi giới hạn và kiểm tra độc lập.
