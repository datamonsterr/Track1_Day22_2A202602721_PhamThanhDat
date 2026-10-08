# Day22 — AI Product GTM & Monetization

**Phạm Thanh Đạt · 2A202602721 · Track 1**

Bài lab tiếp tục **DevPulse AI** từ Day20: chuẩn bị báo cáo Sprint/tháng có nguồn cho CTO quản lý delivery và chi phí AI.

## Hồ sơ nộp bài

- `deliverables/Day22-DevPulse-Monetization-Model.xlsx`: workbook hoàn thành.
- `deliverables/Day22-DevPulse-Monetization-One-Pager.docx`: One-Pager theo ba block của template.
- `deliverables/Day22-DevPulse-Monetization-One-Pager.pdf`: bản render để đọc và kiểm tra một trang.
- `docs/checkpoints/`: sáu trạm và lý do của từng quyết định.
- `docs/evidence/`: Eval Plan, Procurement Q&A và Pilot Protocol; không giả mạo kết quả chưa có.
- `docs/reviews/`: prompt English và accept/reject/partial bằng tiếng Việt.
- `templates/`: hai attachment gốc nguyên vẹn.
- `data/`: nguồn Day20, input và danh mục nguồn.

**Trạng thái bằng chứng:** chưa có telemetry, eval DevPulse, hợp đồng hoặc pilot thực đo trong đầu vào. Các số vận hành và pricing là giả thuyết được gắn nhãn và deadline xác minh. Không tuyên bố đã vượt reader test con người.

## Tái tạo và kiểm tra

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python scripts/build_workbook.py
.venv/bin/python -m pytest -q
```

Workbook cần Excel hoặc LibreOffice để cập nhật formula cache khi thay input. Quy trình render và kiểm tra được ghi tại `docs/verification.md` sau checkpoint cuối.

## Checkpoint commits

Xem `git log --oneline`: CP1 budget/job; CP2 Value Metric; CP3 Cost/Job/pricing; CP4 channel; CP5 plan; CP6 evidence/One-Pager/validation. Thông tin test và CI chỉ được ghi sau khi chạy.
