"""Fill only yellow template cells; keep original formulas and reference values."""
import json
from copy import copy
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.workbook.properties import CalcProperties

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'templates/Day22-AI-Product-GTM-Monetization-Model.xlsx'
OUTPUT = ROOT / 'deliverables/Day22-DevPulse-Monetization-Model.xlsx'


def build():
    inputs = json.loads((ROOT / 'data/workbook-inputs.json').read_text())
    book = load_workbook(TEMPLATE)
    for name, cells in inputs['sheets'].items():
        sheet = book[name]
        for address, value in cells.items():
            cell = sheet[address]
            if cell.fill.fgColor.type != 'rgb' or cell.fill.fgColor.rgb != 'FFFFF2CC':
                raise ValueError(f'Cannot edit non-yellow template cell {name}!{address}')
            cell.value = value
            note = inputs.get('notes', {}).get(f'{name}!{address}')
            if note:
                cell.comment = Comment(note, 'Day22 provenance')
            alignment = copy(cell.alignment)
            alignment.wrap_text = True
            alignment.vertical = 'top'
            cell.alignment = alignment
            if isinstance(value, str):
                sheet.row_dimensions[cell.row].height = max(32, min(100, len(value) / 1.6))
    book['6_Benchmarks']['B3'] = inputs['checked_on']
    book['6_Benchmarks']['B3'].comment = Comment(
        'Verified Haiku 4.5 and cache rates only; see 7_Assumptions and data/sources.json. '
        'Other read-only rows remain the historical template and are not certified current.',
        'Day22 provenance',
    )
    sheet = book.create_sheet('7_Assumptions')
    sheet.append(['DAY22 — DEVPULSE: ASSUMPTIONS & TRACEABILITY'])
    sheet.append(['Giả định vận hành ≠ eval thực đo. Các tab gốc giữ nguyên giá trị ngoài ô vàng.'])
    sheet.append(['Key', 'Value', 'Unit', 'Evidence status', 'Rationale / verification', 'Source'])
    for row in inputs.get('assumptions', []):
        sheet.append(row)
    for row in sheet:
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical='top')
            cell.font = Font(name='Calibri', size=10)
        if row[0].row >= 4:
            sheet.row_dimensions[row[0].row].height = 48
            row[1].fill = PatternFill('solid', fgColor='FFF2F2F2' if row[1].data_type == 'f' else 'FFFFF2CC')
    for column, width in {'A':30, 'B':48, 'C':20, 'D':24, 'E':70, 'F':70}.items():
        sheet.column_dimensions[column].width = width
    sheet.freeze_panes = 'C4'
    sheet.auto_filter.ref = f'A3:F{sheet.max_row}'
    sheet.sheet_view.zoomScale = 85
    sheet.page_setup.orientation = 'landscape'
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A3
    sheet.page_setup.fitToWidth = 1
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    book.calculation = CalcProperties(calcId=191029, fullCalcOnLoad=True, forceFullCalc=True)
    OUTPUT.parent.mkdir(exist_ok=True)
    book.save(OUTPUT)
    print(f'Built checkpoint {inputs["stage"]}: {OUTPUT.name}')


if __name__ == '__main__':
    build()
