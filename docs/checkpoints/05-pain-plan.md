# Checkpoint 5 — Pain Moment và 90-Day Plan

**Pain Moment:** 16:30 thứ Sáu cuối Sprint, CTO/Tech Lead ghép Jira delivery, GitHub PR và AI-cost ledger để kịp giao ban CEO lúc 09:00 thứ Hai; lúc đó họ đang ở GitHub/Jira, nhận nhắc qua Slack #engineering-review. Đây là hypothesis từ cadence Day20, chưa là quan sát phỏng vấn.

**Điểm nhúng:** GitHub App đọc PR metadata + Jira Sprint webhook + Slack report card/link preview. Không bắt nhập lại dữ liệu trên website mới. App chưa build; là integration surface đề xuất, không chứng minh đã có kênh hoạt động. Final Publish vẫn do CTO, không tự đánh giá nhân viên hoặc chỉnh token budget.

| Giai đoạn | Việc và số cụ thể | Owner và gate |
| --- | --- | --- |
| Ngày1–30: 08/10–06/11/2026 | Phỏng vấn5 CTO, tuyển3 org tự cài; xác nhận signer/budget; procurement control15/10, eval22/10. Chỉ shadow redacted data trước gate. Pilot bắt đầu24/10 nếu đủ consent/control. | Phạm Thanh Đạt. Mỗi org có một AI-ready report trong14 ngày; coverage≥80%; không lỗi critical. Chưa có khách thật trong đầu vào. |
| Ngày31–90: 07/11/2026–05/01/2027 | Pilot4 tuần đến20/11, report23/11. Một motion PLG;60 qualified installs,12 activated,3 paid; Không liên tục phục vụ7 unpaid workspace bằng COGS của10 paid. Tổng acquisition spend≤$1.200. | Phạm Thanh Đạt. CAC≤$400; stop sau20 installs nếu chưa4 activation. Eval lower bound phải vượt containment cần thiết tại volume thực tế. |
| Ngày91+ từ06/01/2027 | Chỉ cân nhắc51–100 developer khi có retention publish theo cadence và economics thật. Không hứa scale200 khách. | Phạm Thanh Đạt. Giá≥3×COGS và GM≥60% ở volume hiện tại; chưa đủ gate thì không mở rộng. |

**Nối forecast với volume:** worksheet baseline10 paying workspace là steady-state sensitivity scenario, không phải số khách Day90 hoặc pilot đã có. Funnel đầu cho3 paid. Với3 paid và shared floor$80, Cost/Job$21,366798, floor$64,100395 vượt giá$60 dù GM64,39%; không ghi xanh toàn bộ. Cần tối thiểu4 paying workspace ở4 attempts/org, giảm fixed floor hoặc thử giá mới có đồng ý của khách. Không scale bằng giả định cứ có10 khách là thật.

Người phụ trách mọi đầu việc là Phạm Thanh Đạt vì đầu vào chỉ có một owner. Không bịa tên Sales Lead, đối tác hoặc khách pilot. Đích mở rộng phụ thuộc measured retention, nên chưa có số khách mới cam kết; đó là quyết định có gate, không ô bỏ trống.
