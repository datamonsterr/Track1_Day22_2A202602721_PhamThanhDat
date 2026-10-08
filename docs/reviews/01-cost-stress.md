# Prompt 4.7.1 — Cost/Job Stress Test

## Prompt đã chạy — English

```text
Act as a ruthless CFO and a skeptical infrastructure engineer.
Review the Cost/Job model for DevPulse, an AI-ready engineering report
for a CTO; human approval and final publishing remain mandatory.
Do NOT rewrite my numbers. Perform a stress test:
1. List omitted or underestimated costs, especially retry/timeouts,
   vendor versus customer HITL, observability/eval, storage and egress.
2. Check attempted versus completed denominator and recalculate the gap.
3. Recompute token math and caching/batch savings; assess latency viability.
4. Check promotional/list-price risks; do not invent current prices.
5. Solve GM60 containment algebra; show costs/GM at 50/60/70/80/90%.
6. Identify the single input that breaks the model when wrong by 2x.
Also audit cohort size, fixed costs and confidence-bound launch gates.

Inputs: 10 planning paid workspaces; 40 attempted jobs/month;
75% planning preparation containment, not measured eval; 30 AI-ready.
HITL A: customer final review/rework; internal QA paid by vendor.
Haiku4.5 rates USD/1M: input1, output5, write1.25, read0.1.
4 turns; 8000 cached-prefix tokens; 12000 fresh tokens/turn;
2000 output tokens/turn. No speech, telephony or server-side paid tools.
No Batch for on-demand preview; cache reads within5min must be verified.
Infra80USD/month fixed +8USD/attempt variable =10USD/attempt at40 jobs.
Retry8%, exactly one extra full inference for an affected job.
QA25% ×15min ×20USD/hour. Overhead300USD/month, separate from GM.
Price60USD/report +39USD/workspace/month;3 reports/workspace/month.
API/cache prices verified2026-10-08; all operational inputs are estimates.
Pilot3 serviced workspaces;4 attempts/workspace/month.
```

**Thực thi:** agent `lab_critic` đọc input JSON và các checkpoint; trả kết quả phản biện thật trong phiên làm bài. Không chạy API eval sản phẩm. Dưới đây là bản ghi kết quả và disposition do trợ lý đề xuất khi hoàn thành lab, không tự nhận người dùng đã phê duyệt từng sửa đổi.

## Output AI và phản hồi

| Finding từ AI | Disposition | Sửa/giữ và lý do |
| --- | --- | --- |
| Token math đúng: cache0,1004; no-cache0,1200; savings16,3333%. | accept | Giữ số từ workbook. Cache hit cần prefix ổn định và TTL; preview15min không chứng minh hit. |
| Chia40 cho Cost11,358432; chia30 completed cho15,144576, tăng33,3333%; số sai thấp25%. | accept | Giữ denominator30, numerator chứa cost toàn bộ40 attempts. |
| Overhead300 cho fully-loaded25,144576;60 không đạt3×fully-loaded. | accept | One-Pager tách COGS và overhead; không gọi contribution là GM. |
| Eval100case ×15min ×20/h =500USD một lần, API/retry10,8432USD. | partial | Thêm vào backlog/budget kiểm chứng, không cộng lại toàn bộ vào direct COGS mỗi tháng vì đây có thể là development eval. Số15min là stress assumption, chưa timesheet. |
| Support1,50/attempt chỉ mua4,5min;15min support sẽ thêm140USD/tháng, Cost19,811243 vàGM66,9813%. | accept | Ghi direct-support time thành giả định cần đo, giữ reserve baseline nhưng thêm stress. |
| Refund/sửa miễn phí có thể phát sinh vendorHITL dù A. | accept | QA sample và support reserve chứa phần dự phòng; pilot phải tách dispute time để cập nhật, không coiA là mọiHITL bằng0. |
| No-cache làmCost15,1728;gấp đôiAPI/retry làmCost15,289152. | accept | Price volatility nhỏ hơn infra/containment trong model này. Không inflate savings để đẹp pitch. |
| GM60:11,358432/c≤24 nênc≥47,3268%. | accept | Giữ đúng đại số. Đây là baseline40attempts, không kế toánbreakevenGM0. |
| Containment75% xuống37,5% choCost30,289152;GM49,51808%. | accept | Đưa containment thành biến giết mô hình. |
| Pilot3org:Cost21,366798;floor64,100395;GM64,38867%;price60 không đạtfloor3×. | accept | Nêu ngay trên One-Pager, không tô xanh pilot. |
| PilotGM60 cần66,77124%;floor3× cần80,12549%, nghiêm hơn. | accept | Go-live cần cả hai gate theo volume thực tế. |
| ≥4paid chỉ đúng tại75% pointestimate. Wilson75/100lower65,69554% không đủfloor4paid71,79216%. | accept | Ghi rõminimum4 là planning, không là validated rollout. Với hypothetical interval này cần6servicedpaid; không giảeval75/100 đã xảy ra. |

## Sensitivity đã kiểm tra độc lập

| c | Cost/Job | GM |
| ---: | ---: | ---: |
| 50% | 22,716864 | 62,13856% |
| 60% | 18,930720 | 68,44880% |
| 70% | 16,226331 | 72,95611% |
| 80% | 14,198040 | 76,33660% |
| 90% | 12,620480 | 78,96587% |

Không có thao tác sửa số cho đẹp sau phản biện. Các bổ sung đều là scope, volume, trial budget và evidence gate; input baseline được giữ để thấy rõ rủi ro.
