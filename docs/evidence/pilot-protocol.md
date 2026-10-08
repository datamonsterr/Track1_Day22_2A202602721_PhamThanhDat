# Pilot Report — chưa chạy, có protocol và deadline

**Owner:** Phạm Thanh Đạt. **Target:**3 tổ chức GitHub/Jira,20–50 dev, tự nguyện qua PLG; chưa có tên khách hoặc consent. **Start target:**24/10/2026 sau control/eval gate. **Duration:**4 tuần đến20/11. **Report due:**23/11/2026. Nếu gate trễ, dịch ngày và giữ trạng thái chưa chạy; không backdate kết quả.

## Trước pilot

Xác nhận budget owner, thời gian chuẩn bị báo cáo hiện tại và đồng ý thu thập metadata. Cho CTO đọc billing rule và quality gate. Customer tự cài read-only App trên repo chọn; nếu cần một cuộc demo bắt buộc cho từng khách, ghi friction và phản biện PLG. Trước15/10 chỉ shadow dữ liệu redacted; không thu raw source code, prompt secrets hoặc dữ liệu nhân sự không cần thiết.

## Thiết kế đo

Đo baseline ít nhất một chu kỳ gần nhất bằng timesheet chuẩn bị/report và artifacts đã có; cùng một người/cùng phạm vi chuẩn bị để giảm confounding. Hai Sprint report + một Board report là cadence mục tiêu, nhưng đo count thật và cửa sổ thật. Không so dashboard mới với một tháng công ty khác. CTO final review15–30 phút giữ riêng, không cộng thành giờ AI đã tiết kiệm.

Cho mỗi job ghi API tokens/cache hit/extra retry, vendor QA minutes/support, infra share, completion gate, customer rework và final Publish. Dedup theo workspace/period/type; failed jobs không bill. Cost/Job chia completed; không bỏ ca fail khỏi numerator. Retention đo organization publish trong bracket tháng tiếp theo theo Day20, không lấy DAU proxy.

## Template kết quả sau khi chạy

| Field | Hiện tại |
| --- | --- |
| Tổ chức, consent, budget signer | Chưa tuyển/xác nhận |
| Job attempted/completed/published | Chưa đo |
| Containment và Wilson interval | Chưa đo;75% chỉ forecast |
| Critical numerical/privacy failures | Chưa đo |
| Cost/Job theo5 nhóm, với/không overhead | Chưa đo |
| Net giờ chuẩn bị tiết kiệm, customer review/rework | Chưa đo;10h/report chỉ giả định |
| Win/paid/refund/CAC | Chưa đo;3 paid và$400 CAC là target |
| Permission/install friction, time-to-first-report | Chưa đo |
| Repeat Publish theo tháng | Chưa đủ cửa sổ cohort |

Baseline3 workspace cho12 attempts,9 AI-ready forecast. Shared-floor$80 làm Cost/Job$21,366798; GM64,38867% nhưng floor3×$64,100395 vượt price$60. Pilot học được phải được tài trợ; không tuyên bố economics steady-state đã chứng minh. Với cấu trúc hiện tại cần≥4 paid workspace hoặc giảm fixed cost/đổi offer trước rollout có gatefloor3×.

Chỉ đưa kết quả đo vào tài sản “Pilot Report” khi có CSV event anonymized, trước/sau có artifacts, invoice/budget reconciliation và CTO ký nhận. Không dùng báo cáo protocol này làm case study thành công hoặc testimonial.
