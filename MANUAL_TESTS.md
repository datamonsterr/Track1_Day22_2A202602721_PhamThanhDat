# Manual checks — hồ sơ nộp Day22

Repo này chứa bài lab, không có webapp được triển khai.

| Kiểm tra | Cách làm | Trạng thái |
| --- | --- | --- |
| Workbook | Mở bằng Excel/LibreOffice; xem đủ bảy tab gốc và assumptions. Đối chiếu Cost/Job, floor, GM, containment và CAC với One-Pager. | Đã tính bằng LibreOffice và checker độc lập. |
| Provenance | Xem comment các ô cost, ngày ở 6_Benchmarks!B3 và assumptions. Các dòng benchmark cũ không được coi là đã xác minh hết. | Đã kiểm tra template/JSON; giá model đã browse. |
| Sensitivity | Trên bản sao, đổi containment 50/60/70/80/90%; đối chiếu Tab2. Zero completed phải là undefined, không nhận zero cost. | Automated tests; không sửa artifact nộp để chạy thử. |
| Một trang | Mở DOCX/PDF; đủ ba block, không mất dấu tiếng Việt, cắt bảng hoặc tràn trang. | PDF một trang đã render và xem ảnh cả trang. |
| Mapping | Dùng data/one-pager-trace.json mở đúng ô cho mỗi số; không trộn pilot với steady-state. | Checker xác minh 75 entries và rounding. |
| Evidence honesty | Eval/Pilot ghi chưa có kết quả; Q&A là draft có owner/deadline; không claim SOC2 hoặc signed partner. | Đã review nội dung. |
| Stranger test | Hai người chưa biết DevPulse đọc hai phút; trả lời ba câu rubric, ghi nguyên văn và số câu hỏi lại. | Chưa có người thật thực hiện. AI simulation giữ riêng. |

Sau human reader test, cập nhật M!B29:B32 bằng kết quả thật, rerun build/cache/render/validator và tạo commit mới. Không điền “Được” trước khi đo.
