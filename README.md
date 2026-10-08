# Day22 — AI Product GTM & Monetization

**Phạm Thanh Đạt · 2A202602721 · Track 1 · 08/10/2026**

Bài lab tiếp tục **DevPulse AI** từ Day20: chuẩn bị báo cáo Sprint/tháng có nguồn Jira, GitHub và AI-cost ledger cho CTO nhóm 20–50 developer.

## Hồ sơ nộp bài

- [Excel model](deliverables/Day22-DevPulse-Monetization-Model.xlsx): bảy tab gốc đã điền và một tab assumptions/traceability bổ sung.
- [Word One-Pager](deliverables/Day22-DevPulse-Monetization-One-Pager.docx): ba block Pricing, GTM và Evidence.
- [PDF One-Pager](deliverables/Day22-DevPulse-Monetization-One-Pager.pdf): bản render đúng một trang.
- [Sáu checkpoint](docs/checkpoints/): quyết định, số học, nguồn và các gate chưa đạt.
- [Evidence Pack](docs/evidence/): Eval Plan, Procurement Q&A và Pilot Protocol.
- [AI critique logs](docs/reviews/): prompt English, kết quả thật và disposition bằng tiếng Việt.
- [Verification](docs/verification.md) và [manual checks](MANUAL_TESTS.md).
- [Nguồn](data/sources.json), [input](data/workbook-inputs.json), [numeric mapping](data/one-pager-trace.json).

## Kết luận mô hình

Baseline **forecast 10 paying workspace**: Cost/Job COGS **$15,144576**; giá sàn **$45,433728**; đề xuất **$60/report + $39/workspace/tháng**; report GM **74,75904%**; containment tối thiểu cho GM60 **47,3268%**. PLG forecast CAC **$400**; rep-motion CAC scenario **$4.800**.

Đầu vào không có telemetry, eval DevPulse, pilot, customer payments hoặc signed partner. Các số vận hành và giá bán là giả định có rationale và deadline xác minh. Pilot ba paying workspace chưa đạt floor3× ở giá $60; chỉ scale khi gate theo volume thực tế và eval lower bound đạt. Human reader test vẫn ghi **chưa thực hiện**; không dùng AI simulation làm bằng chứng người thật.

## Checkpoint commits

| Checkpoint | Commit | Đầu ra |
| --- | --- | --- |
| CP1 | da756a8 | Buyer, ngân sách và Job |
| CP2 | fabbded | Hybrid, scorecard và hai benchmark |
| CP3 | c5125b9 | Năm nhóm chi phí, giá và sensitivity |
| CP4 | 75fac90 | PLG và CAC affordability |
| CP5 | 8e2ce03 | Pain Moment và kế hoạch có gate |
| CP6 | 86ed869 | Evidence Pack và One-Pager có trace |

[PR verification #3](https://github.com/datamonsterr/Track1_Day22_2A202602721_PhamThanhDat/pull/3) đã merge sau khi review diff và CI xanh. **64 tests pass, không skip; 132 formula caches, 75 trace entries, hai template hashes và chín nguồn đã kiểm tra.** [CI trên main sau merge](https://github.com/datamonsterr/Track1_Day22_2A202602721_PhamThanhDat/actions/runs/37733888574).

## Tái tạo và kiểm tra

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python scripts/build_workbook.py
.venv/bin/python scripts/recalculate.py xlsx
.venv/bin/python scripts/build_one_pager.py
.venv/bin/python scripts/recalculate.py pdf
.venv/bin/python -m pytest -q
.venv/bin/python scripts/validate_model.py
```

Các lệnh `recalculate` cần container LibreOffice như hướng dẫn trong verification. Workbook cần Excel/LibreOffice để cập nhật formula cache khi đổi input; openpyxl không tự tính công thức. Hai attachment gốc lưu nguyên vẹn trong `templates/`; dữ liệu Day20 được lưu trong `data/day20-metrics-pack.md`.
