# Manual checks — hồ sơ nộp Day22

Không có webapp được build trong repo này. Kiểm tra dưới đây áp dụng cho workbook và One-Pager.

| Kiểm tra | Cách làm | Trạng thái |
| --- | --- | --- |
| Workbook | Mở bằng Excel/LibreOffice, xem đủ7 tab gốc + assumptions; không sửa công thức xám. Đối chiếu Cost/Job, floor, GM, containment và CAC với One-Pager. | Đã tính bằng LibreOffice; checker độc lập đối chiếu cache. |
| Provenance | Xem comment các ôcost, date6_Benchmarks!B3 và7_Assumptions. Các dòngbenchmark cũ không được xem là đã xác minh hết. | Đã kiểm tra tự động template/JSON; giá model đã browse. |
| Sensitivity | Trên bản sao, đổi containment50/60/70/80/90%; Excel tính lại phải khớp Tab2. Đổi0 completed phải coiundefined, không nhận0 cost. | Automated tests; không sửa file nộp để chạy thử. |
| One page | Mở DOCX vàPDF; đủPricing/GTM/Evidence; không mất dấu tiếng Việt, không cắt bảng hoặc tràn trang. | Đã renderPDF1trang và xem hình cả trang. |
| Mapping | Chọn từng số trong DOCX, dùngdata/one-pager-trace.json mở đúngôXLSX. Giá, GM vàthreshold phải cùngcase, không trộnpilot vớisteady-state. | Checker tự động. |
| Evidence honesty | EvalResults/PilotReport phải ghi“chưa có”;Q&A làdraft, cóowner/deadline. KhôngclaimSOC2 hoặc signedpartner. | Đã review nội dung. |
| Stranger test | Nhờ hai người không biếtDevPulse đọc2phút; hỏi3câu ởrubric, ghi sốcâu cần hỏi lại và nguyênvăncâu trảlời. | **Chưa có người thật thực hiện**. AIreader simulation giữ riêng, không tickPass. |

Reader test không thể được chứng minh bằng việc tự điền“Được”. Sau khi có người thật, cập nhật ôM!B29:B32 bằng kết quả vàrerunbuild/cache/docx/PDF/validator, tạo commitmới. Không điềntrước thờiđiểmđo.
