# Checkpoint 4 — Chọn một kênh và chứng minh affordability

**Chọn duy nhất PLG** trong 90 ngày. Khách mục tiêu: CTO nhóm sản phẩm 20–50 developer dùng GitHub/Jira, tự cài một app read-only, xem báo cáo mẫu và tự mua. GitHub là distribution surface, không phải một partner đã đồng ý bán giúp; không chọn Partner-Led. Pilot phỏng vấn sau activation là hoạt động học của PLG, không là motion sales rep khác.

## Ngân sách và rep motion

| Input/output | Số | Lý do |
| --- | ---: | --- |
| ARPU | $219/tháng | $39 workspace + 3 × $60 report |
| Report GM dùng bảo thủ | 74,75904% | Thấp hơn blended GM; linked từ Tab2 |
| SMB payback ceiling | 12 tháng | Convention của lab, chưa chứng minh retention |
| CAC budget | $1.964,667571 | 219 × 0,7475904 × 12 |
| ACV | $2.628 | 219 × 12; giả sử cadence ổn định |
| AE fully loaded | $24.000/năm | $2.000/tháng, giả định local scenario |
| Quota | $120.000/năm | 5× AE cost, giả định planning |
| Working days | 250/năm | Convention dùng trong worksheet |
| Deal/AE/năm | 45,66210 | 120.000 / 2.628 |
| Deal/AE/ngày | 0,1826484 | 45,66210 / 250 |
| Full rep acquisition spend | $48.000/năm | 24k AE + 12k marketing + 12k tools/management |
| Qualified opportunities | 40/năm | Giả định, chưa có pipeline |
| Cost per opportunity | $1.200 | 48.000 / 40 |
| Win rate | 25% | 10 wins/40 opportunities, giả định |
| Estimated rep CAC | $4.800 | 1.200 / 0,25 |
| Gap | 2,44316× | 4.800 / 1.964,667571 |

Sales-Led **khả thi về số deal/ngày** với quota local giả định, nhưng **không đạt CAC affordability**. Không suy từ threshold 1 deal/ngày thành kết luận tuyệt đối mọi motion có sales đều không thể. [Tunguz 2016](https://tomtunguz.com/smallest-acv-to-justify-inside-sales-team/) là khung historical để tính lại, không là chi phí nhân sự hiện tại ở Việt Nam. Không xác minh được bản gốc ICONIQ CPO 2026 trong phạm vi này nên không dùng các mức $6.300/$8.000/$11.200 trong model như sự thật hiện hành.

## PLG bottom-up forecast

Acquisition budget **$1.200/90 ngày** gồm 40h founder content × $20 = $800, $200 content/tools và $200 placement/trial allowance. 60 qualified org installs × 20% activation × 25% activated-to-paid = **3 paid customers**. Estimated CAC **$400**, payback **2,44316 tháng** theo conservative GM; tất cả conversion là giả định, không phải kết quả quảng cáo. Trial allowance và founder time đã tính vào acquisition spend; production service COGS giữ riêng. Không extrapolate cohort 3 wins thành 10 tài khoản mà không có pipeline nối tiếp.

Quota đặt $120k tương đương 45,66 deal/year; rep scenario 40 opportunity ×25% chỉ tạo 10 deal và $26.280 bookings, tức 21,9% quota. Đó là một failure scenario cần được nêu, không hai forecast cùng được coi là đạt. Để chạm quota cần khoảng 183 opportunity/year; nếu cùng $48k spend vẫn tạo được số này thì CAC khoảng $1.051,20 và rep motion có thể thay đổi kết luận. Chưa có bằng chứng throughput ấy; không lấy kết quả tốt làm mặc định.

Không báo LTV:CAC đạt 3× khi chưa có churn/retention. Chỉ biết với conservative monthly gross profit $163,7223, cần ≥7,33 tháng gross-profit lifetime để đạt LTV:CAC=3 ở CAC $400; đây là điều kiện cần, không là LTV đo được.

## Scorecard rationale

PLG/Sales/Partner điểm lần lượt **22/17/11**. PLG finance4 vì forecast $400 nhỏ hơn cap, buyer3 vì B2B permission friction chưa đo, team3 vì một owner có thể làm onboarding nhỏ, access3 vì app/listing còn chưa build, pain5 vì GitHub/Jira trùng nơi report được chuẩn bị, measurement4 vì event funnel đo được trong 90 ngày. Sales finance1 vì CAC vượt cap; buyer4 và access4 vì CTO có thể demo nhưng tốn người. Partner team1 và access1 vì chưa có quan hệ hoặc công ty partner cam kết; không chấm cao chỉ vì tên marketplace.

## Stop conditions trong 30 ngày

Phạm Thanh Đạt thử 3 pilot tự cài, không tuyển AE. Nếu sau 20 qualified installs không có 4 activation, hoặc median time-to-first-report vượt 14 ngày, giảm phạm vi kết nối và dừng placement. Sau tối đa $1.200 acquisition spend, nếu chưa có 3 trả tiền thì CAC vượt $400: dừng chi, phỏng vấn và đổi offer trước khi scale. Nếu bắt buộc demo riêng từng khách mới cài được, PLG bị falsify; không âm thầm đổi sang sales mà giữ CAC PLG trên giấy.

Theo [GitHub requirements](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app), listing có gate review/verification. Kế hoạch cần app installation link trực tiếp cùng kênh PLG nếu listing chưa được duyệt; không ghi đã có listing. App cần [minimum permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app). Chưa build, chưa xin quyền trong lab này.
