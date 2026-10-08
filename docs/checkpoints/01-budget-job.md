# Checkpoint 1 — Ngân sách và Job

## Dữ liệu đầu vào và giới hạn

Tiếp tục **DevPulse AI** từ Metrics Pack Day20 của Phạm Thanh Đạt. Bản gốc được lưu tại `data/day20-metrics-pack.md`; tài liệu là mô tả sản phẩm và mục tiêu, không phải telemetry hoặc kết quả eval. Repo Day22 lúc clone là repo trống. Hai attachment là template có worked example CSKH, không phải dữ liệu khách hàng DevPulse. Không lấy containment 82% hay 1.000 ticket mẫu làm kết quả thực đo.

## Hai cách định vị

**A — công cụ:** DevPulse AI là nền tảng engineering intelligence tổng hợp Jira, GitHub và chi phí AI cho CTO. CTO đề xuất, IT/Procurement duyệt; chi từ ngân sách phần mềm.

**B — công việc:** DevPulse chuẩn bị báo cáo Sprint/tháng có đối chiếu nguồn để CTO giải trình delivery và chi phí AI, giảm giờ Tech Lead tổng hợp thủ công. CTO là sponsor và budget owner; CEO/CFO duyệt theo hạn mức. Chi từ ngân sách vận hành khối kỹ thuật cho reporting, không khẳng định sa thải hoặc thay thế toàn bộ một vị trí.

Chọn **B** vì thay thế một khối công việc có chi phí giờ công dễ đối chiếu; pilot phải xác nhận budget owner và quyền ký, không giả định câu định vị tự thay đổi quy trình Procurement.

## Job và quy tắc đếm

Một Job là **một báo cáo Sprint hoặc tháng sẵn sàng để CTO review**, đã đối chiếu Jira delivery, GitHub PR và AI-cost ledger, mọi số quan trọng có nguồn, độ phủ tối thiểu 80% developer active, không có lỗi nghiêm trọng. Đếm theo `(workspace_id, period_id, report_type)` ở event `report_ready`; retry, refresh cùng kỳ và sửa lỗi không được tính thêm. Không tính báo cáo bị chặn vì thiếu dữ liệu, lỗi số liệu, hoặc ca phải được khách viết lại. CTO review và xuất bản vẫn là core action Day20; không bán kết quả ROI do AI gây ra.

**Biến thể HITL A:** khách chịu final review và tự xử lý báo cáo không đạt. DevPulse chịu QA nội bộ và support trực tiếp; không nhận nghĩa vụ giao báo cáo managed service. Nếu sau này DevPulse sửa tất cả ca thất bại, phải chuyển sang B và tính lại chi phí.

Ba phép thử: báo cáo là đầu ra khách cần; event và khóa kỳ cho phép đếm; quality gate và quy tắc không tính tiền đủ cụ thể để triển khai. Đây là thiết kế, chưa có log production chứng minh.
