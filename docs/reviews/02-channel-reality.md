# Prompt 4.7.3 — Channel Reality Check

## Prompt đã chạy — English

```text
I am choosing ONE go-to-market channel for the next90days: PLG.
DevPulse produces evidence-linked engineering reports for CTOs of
20-50 developer organizations using GitHub/Jira and an AI-cost ledger.
Pain moment:16:30 Friday at Sprint close, preparing Monday09:00 review,
working in GitHub/Jira and receiving a Slack report card.

ARPU219USD/month =39base +3reports×60USD.
Report GM74.75904%; SMB payback ceiling12months;
CAC budget1964.6675712USD. These are forecasts, not measured outcomes.
Local sales scenario: AE quota120000USD/year, fully-loaded AE24000USD;
250 working days; full acquisition spend48000USD/year;
40 qualified opportunities/year; win rate25%; CPO1200USD; CAC4800USD.
PLG forecast: spend1200USD,60 installs,20% activate,25% of active pay;
3paid customers and CAC400USD. No signed partner or approved listing.

1. Compute deals/year and deals/day; assess sales viability and quotas.
2. Compare CAC budget with sales cost scenario; state the multiple.
3. Stress-test the pain moment and name missing integration details.
4. Challenge active-versus-paid cohorts and free-trial service costs.
5. Give the strongest argument against PLG and a two-week falsification.
Flag assumptions. Do not fabricate current external benchmarks or pilots.
```

**Thực thi:** agent `lab_critic` đọc model và checkpoint; kết quả là AI review, không phải paid-ad experiment. Phản hồi dưới đây là decision draft của bài nộp.

| Finding từ AI | Disposition | Sửa/giữ và lý do |
| --- | --- | --- |
| ACV2628;quota120k cần45,6621deal/year hay0,1826484/day. | accept | Sales đủ nhẹ vềdeal/day nhưng chưa chứng minh acquisitionfunnel. |
| 40opps×25% chỉ10wins,26280bookings,21,9% quota; cần182,6484opps để đạtquota. | accept | Nêu rõscenario bất lợi không phải forecast đạtquota; không dùng thấpdeal/day để tô xanhsales. |
| SalesCAC4800 vsbudget1964,667571 =2,4431614×;payback29,31794months. | accept | GiữPLG nhưhypothesis; không dùngICONIQCPO chưa xác minh. |
| PLGCAC400 có thể thành600với2paid,1200với1paid;zero-paidCAC undefined. | accept | Acquisitioncap1200 vàoperating stop400; không báoCAC đođược. |
| LTV:CAC3 cần7,32948months gross-profit lifetime; chưa córetention. | accept | Không tuyên bốLTV:CAC đạt3. |
| GitHubApp không tự cung cấpAIcostledger, Jirapermission và mapping. | accept | Bổ sung ledger import, permission/onboarding test vào tháng1. Nếu cầnfounder demo từngkhách, PLG bịfalsify. |
| 10active không bằng10paid; nếu40attempts nhưng3paid,Cost/billed50,48192,reportGM15,86347%,blendedGM30,84668%. | accept | Bỏtarget10active ởplan. Baseline10paying chỉ làsteady-state sensitivity; initialfunnel3paid. |
| Trial allowance200 có thểkhông đủ phục vụ7unpaid liên tục. | accept | Chỉmột báo cáo nhỏ, expires14ngày; reserve150USDcho16trialattempts×9,358432=149,734912;sharedfloor80 tínhmộtlần ởpaidcohort.50USDcòn lại placement. Nếu chưa cópaid, floorcũng vàoacquisitionbudget và phảipause sớm. |

## Hai tuần đầu — phép thử falsify

Phạm Thanh Đạt tuyển qua một luồng install/content PLG, quan sát khả năng CTO tự cấp quyền read-only và import cost ledger. Dữ liệu thật chỉ sau consent/control gate. Nếu không hoàn thành permission+ledger+firstreport trong14ngày mà không cần cuộc demo bán hàng bắtbuộc, không scale placement. Thửngách vàconnector trước khi sửagiá.

**Giữ một kênh:** pilot interview sauactivation đểhọc, không làsales-repmotion mới. Không viết“đãchốt3khách” khi chỉ cótarget.
