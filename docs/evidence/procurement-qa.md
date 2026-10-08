# Procurement Q&A — bản nháp, chưa là chứng nhận kiểm soát

**Owner:** Phạm Thanh Đạt. **Deadline kiểm tra control:** 15/10/2026. Dùng cho sản phẩm DevPulse đề xuất, chưa có production security proof, SOC2 hoặc signed DPA của DevPulse. Phân biệt điều khoản vendor đã đọc với tính năng dự định làm.

## 1. AI hallucinate hoặc đánh giá sai nhân viên thì sao?

DevPulse đề xuất chỉ diễn giải aggregate Jira/GitHub/token-cost có nguồn. Số liệu tính deterministic; lời giải thích AI phải có citation và độ phủ, không được biến correlation thành causal ROI. Thiếu dữ liệu hoặc thiếu nguồn thì không giao/bill report. CTO phải review trước Publish; sản phẩm không tự xếp hạng nhân viên, sa thải, đổi quota hoặc quyết định hiệu suất cá nhân.

**Bằng chứng còn thiếu:** holdout eval, job-level audit log, screenshot blocked report, numerical reconciliation và incident playbook. Deadline22/10 cho eval; chưa thể trả lời một measured hallucination rate. Nếu sai sau giao: freeze billing job tranh chấp, sửa miễn phí cùng ID/kỳ, reverse charge nếu chất lượng không đạt; điều khoản này là proposal cần customer agreement.

## 2. Data có bị dùng train model không?

Model baseline là first-party Anthropic API cho commercial use. [Commercial Terms, section B](https://www.anthropic.com/legal/commercial-terms) kiểm tra08/10/2026 quy định quyền với Customer Content và hạn chế training. Điều đó không tự chứng minh DevPulse đã cấu hình logging, retention, masking, vùng xử lý hoặc quyền truy cập đúng.

**Control đề xuất:** chỉ PR metadata và aggregate cost, không raw code/prompt/secret; GitHub App minimum read permissions; tách tenant; redact PII trước model; không opt-in chia sẻ training; document subprocessors/DPA và vùng xử lý; không nói data lưu ở Việt Nam khi chưa có bằng chứng. Provider retention, safety exception và ZDR phải được kiểm tra bằng điều khoản/config của deployment cụ thể; không hứa “zero retention” từ pricing page.

**Bằng chứng cần:** data-flow diagram, field whitelist, app permission manifest, sample redaction, tenant-isolation tests, subprocessor list, DPA và retention matrix. Hoàn thiện nháp15/10; chỉ pilot dữ liệu thật sau consent và control gate.

## 3. Startup dừng hoạt động thì data của khách ở đâu?

Khách giữ source of truth Jira/GitHub/AI ledger. Policy đề xuất: xuất CSV/JSON report kèm source IDs và PDF; monthly export do khách tải về; raw metadata TTL90 ngày; khi terminate, export rồi delete tenant theo lịch được thỏa thuận, gồm backup expiry. Chưa có export/restore/delete drill, nên không khẳng định đã đáp ứng exit guarantee.

**Bằng chứng cần:** sample schema không proprietary lock-in, export/download checksum, restore test, deletion log và backup lifecycle, ownership/DPA termination clause, named incident contact. CTO ký nghiệm thu export trước pilot; chưa đáp ứng thì chỉ chạy shadow redacted data.

## Các objection còn lại

| Question | Written answer format cần có | Trạng thái |
| --- | --- | --- |
| Cross-tenant access? | Tenant boundary test + role table + audit records | Chưa kiểm chứng |
| Ai có quyền Publish? | Role/permission matrix, sample approval log | Thiết kế CTO review, chưa triển khai |
| Giá vượt dự kiến? | Sample invoice, dedup/refund rule, quota và opt-in overage | Proposal đã viết |
| Model đổi giá hoặc chất lượng? | Model version pin, monthly price log, holdout migration rule | Vendor rates đã kiểm tra; eval chưa có |
| Lỗi support ai xử lý? | Contact, severity/escalation workflow và SLA đã thỏa thuận | Chưa có SLA ký |
| Dữ liệu không đầy đủ? | Missing-source gate, explicit incomplete flags, no-charge examples | Protocol, chưa output evidence |
| Thu hồi GitHub App? | Token revoke/delete workflow + test log | Chưa triển khai |

**Điểm yếu nhất:** chưa có tenant-isolation và export/delete proof. Một bản Terms của Anthropic không thay thế bằng chứng an toàn end-to-end của DevPulse. Minimum viable Evidence Pack gồm eval có mẫu số/interval, Q&A/DPA/data-flow/permission manifest, pilot có consent và cost/time logs; không dùng nhãn SOC2 giả.
