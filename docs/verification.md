# Kiểm tra và tái tạo

## Đã chạy trước CP6

Workbook được LibreOffice7.4.7.2 tính lại trong container tạm. Sau đó chỉ transplant formula cache vào bản openpyxl, giữ nguyên formula text và giá trị readonly trên template. Checker độc lập tính và đối chiếu **132formula**; không tin cache một cách mù quáng.

DOCX dùng attachment gốc làm package/style đầu vào, được rút gọn theo ba block. LibreOffice renderPDF **1trang**; đã xem ảnh cả trang, không thấy mất dấu, cắt bảng hoặc tràn. MetadataPages được ghi sau khi render thật; PDF là bằng chứng trang chính. **75trace entries** đối chiếu với workbook và các số hiển thị, có kiểm tra rounding.

Template XLSX/DOCX gốc lưu trongtemplates; SHA256 ởdata/template-manifest.json. data/sources.json ghi mứcgiá/ngày/scope đã kiểm tra. 6_Benchmarks!B3 chỉ xác nhận model/cache đã dùng; không nhận tất cả benchmark lịch sử là hiện hành.

Kiểm tra worker vàCI cuối được bổ sung sau PRverification; không coi skipstage<6 là bằng chứng củaartifactcuối. Humanreader test chưa được chạy.

## Tái tạo artifacts

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
docker run --rm -d --name day22-office-bootstrap debian:bookworm-slim sh -c 'apt-get update -qq && apt-get install -y -qq --no-install-recommends libreoffice-calc libreoffice-writer fonts-dejavu-core && touch /tmp/day22-office-ready && sleep 3600'
```

Chờ container cài xong; kiểm tra bằng`docker exec day22-office-bootstrap test -f /tmp/day22-office-ready`. Sau đó chạy:

```bash
.venv/bin/python scripts/build_workbook.py
.venv/bin/python scripts/recalculate.py xlsx
.venv/bin/python scripts/build_one_pager.py
.venv/bin/python scripts/recalculate.py pdf
.venv/bin/python -m pytest -q
.venv/bin/python scripts/validate_model.py
docker stop day22-office-bootstrap
```

Không save lại XLSX bằng openpyxl sau recalculate nếu chưa tính cache lại: openpyxl không evaluate formulas. Giá trịcached trongdata/calculated-results.json có thể dùng đểdiff; đây làderiveddata, không phải nguồnthứhai thaychoExcel.

CI chỉ đọc artifact đãcommit và kiểm tra; không regenerate binary bằng font khác. Kiểm traOffice/GoogleSheets trên bản sao khi thayinput, vì sẽ phảiđổi confidence/volume gate và reruntrace/render.

## Giới hạn bằng chứng

Unit/integration tests của repo kiểm tra mô hình tài chính và contract tài liệu. Không phải eval chất lượngDevPulse, hosted browsercheck, customerpayment hoặc pilotresult. Controlproof, SOC2 và humanreader test không được tạo từ đây.
