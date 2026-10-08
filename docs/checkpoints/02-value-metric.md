# Checkpoint 2 — Value Metric

## Scorecard phản ánh bằng chứng hôm nay

Attribution **1/10**, Autonomy **0/10**. Không có log, eval, xác nhận định nghĩa của khách hoặc hệ thống chạy end-to-end trong đầu vào. Chỉ chấm 1 cho khả năng viết quy tắc job có ranh giới; không tự chấm điểm cho feature dự kiến. Gợi ý workbook là Seat hoặc Hybrid.

| Câu | Điểm | Vì sao |
| --- | ---: | --- |
| Attribution 1: log đầy đủ | 0 | Không có telemetry DevPulse. |
| Attribution 2: eval có số | 0 | Không có eval; 75% sau này là giả định planning. |
| Attribution 3: khách đồng ý success | 0 | Chưa phỏng vấn/pilot. |
| Attribution 4: phân biệt nguyên nhân | 0 | Day20 mô tả PR-to-token mapping, không cung cấp bằng chứng đã chạy. |
| Attribution 5: định nghĩa billing chặt | 1 | Đã viết rule dedup/quality gate; chưa được khách xác nhận. |
| Autonomy 1–5 | 0 từng câu | Chưa có execution evidence; CTO vẫn review từng báo cáo. |

## Benchmark ngược — kiểm tra 08/10/2026

- [Swarmia Standard](https://www.swarmia.com/pricing/): Seat, **$45/developer/tháng, trả theo năm**; engineering effectiveness và AI cost/impact. Cùng nhóm nhu cầu, không cùng phạm vi dịch vụ. Không chia giá seat thành giá report rồi coi là tương đương.
- [LinearB Essentials](https://linearb.io/pricing): Hybrid, **$29/user/tháng, trả theo năm**, gồm 1.000 monthly AI credits/user; credit thêm bắt đầu $0,015. Trang nêu nhóm từ 50+ developer. DevPulse nhắm nhóm nhỏ hơn và output báo cáo hẹp hơn; chưa chứng minh fit.

## Decision Note — 3 câu

Tôi chọn **Hybrid**: phí workspace cho kết nối, lưu trữ và support chuẩn, cộng Usage trên báo cáo AI-ready được giao từ báo cáo đầu tiên; không tính seat hoặc ROI tiết kiệm.

Attribution 1/10 và Autonomy 0/10 vì chưa có log/eval/pilot, CTO vẫn review; lựa chọn khớp gợi ý và chưa đủ điều kiện bán Outcome.

Mô hình lỗ khi cho refresh vô hạn, cam kết sửa tất cả báo cáo lỗi hoặc tenant có chi phí đồng bộ vượt quota; giới hạn dataset, số kỳ và ngân sách, không charge retry/sửa lỗi, cảnh báo và cần opt-in trước overage.

**Market override:** không áp dụng; Hybrid nằm trong gợi ý. Phí workspace không phải minimum spend và không bao gồm báo cáo. Không bán hoặc thu tiền trong bài lab; đây là giả thuyết pricing để kiểm chứng.
