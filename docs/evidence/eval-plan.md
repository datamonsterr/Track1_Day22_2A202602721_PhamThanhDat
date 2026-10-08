# Eval Results — chưa có kết quả, có protocol

**Owner:** Phạm Thanh Đạt. **Deadline:** 22/10/2026. Không có eval DevPulse trong đầu vào; containment75% là assumption. Bộ test worksheet chỉ kiểm tra số học, không chứng minh model xử lý đúng job.

## Bộ dữ liệu và nhãn

Chuẩn bị100 reporting jobs có sự đồng ý hoặc dữ liệu synthetic rõ nhãn:50 bình thường,20 thiếu nguồn/coverage,15 duplicate/retry/late event,10 contradictory cost/PR records,5 prompt injection hoặc cross-tenant. Tách holdout khỏi dữ liệu sửa prompt. Mỗi job có source ledger, kỳ report, ground truth deterministic aggregates và checklist lập luận; reviewer chấm blind theo rubric trước khi đọc output. Đây là số case dự kiến, chưa có file output của100 case.

**Success:** số delivery/token-cost khớp nguồn và rounding policy; tất cả claim quan trọng có link; coverage≥80%; không dùng PR/token correlation làm bằng chứng causal ROI; không lộ tenant khác; không hallucinate thiếu nguồn; báo cáo normal đủ để CTO review. Ca thiếu dữ liệu phải suppress/escalate đúng rule, không tính AI-ready chỉ vì model trả text. Failed jobs không tính tiền. Job bị chặn đúng cũng là negative control pass của eval safety, nhưng không là completed billable report.

## Đo riêng các mẫu số

- Functional eval pass: case đáp ứng expected behavior, gồm refusal đúng; không dùng làm containment.
- Preparation containment: AI-ready reports / eligible reporting jobs attempted. Không trộn các bài safety negative control vào denominator chỉ để làm đẹp success rate.
- Published rate: báo cáo CTO phê duyệt/chia sẻ / AI-ready reports, theo Day20; customer review time vẫn được đo.
- Retry: số extra full inference runs / attempted jobs; không chỉ % job từng gặp lỗi khi một job có thể retry nhiều lần.
- QA/service COGS: thời gian vendor QA, direct support, retry, usage tokens và invoice allocation.

Lưu `workspace_hash, period_id, report_type, job_id, attempt_id, model_version, usage_input/output/cache, infra_allocated, qa_minutes, status, source_links, evaluator_label`. Job ID dedup vẫn giữ mọi API attempt để đo chi phí. Không commit PII hoặc token proxy raw chứa secrets.

## Gate và độ bất định

Không mở paid rollout trước khi không có lỗi critical trong bộ holdout và lower95% Wilson confidence bound của preparation containment vượt threshold **tại volume thật**. Baseline10 workspace cần47,3268%; pilot3 workspace có shared-floor phân bổ khác, cần khoảng66,77124% ở GM60. Ước tính75/100 AI-ready cho lower bound khoảng65,7%, vì vậy có thể đạt baseline gate nhưng **không** đạt pilot gate; cần tăng sample, cải thiện chất lượng hoặc đổi cost/price, không tự coi75% planning là pass.

Safety0/100 không chứng minh rủi ro bằng0; với sample nhỏ, upper bound lỗi vẫn khác0. Nếu có critical leak hoặc sai số tài chính, stop và rerun holdout sau remediation. Tổng case và eligible jobs phải ghi riêng:100-case suite không đồng nghĩa100 eligible reporting jobs.

## Format kết quả phải xuất

CSV anonymized từng job + JSON aggregate gồm denominators, count pass/refusal/failure/AI-ready/published, Wilson interval, critical error count, token/QA latency percentiles, Cost/Job thực đo và breakdown. Kèm model/prompt/source dataset version và sampling rule. Báo cáo cần ghi unmet gates, không thay bằng một phần trăm thành công chung.
