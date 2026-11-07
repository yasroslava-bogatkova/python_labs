import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

MIN_WIDTH = 8


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    src = Path(csv_path)
    dst = Path(xlsx_path)
    if src.suffix.lower() != ".csv" or dst.suffix.lower() != ".xlsx":
        raise ValueError("Неверный тип файла: ожидается .csv -> .xlsx")
    if not src.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with src.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if not rows or not any(cell.strip() for cell in rows[0]):
        raise ValueError("CSV пуст или не содержит заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)

    for cell in ws[1]:
        cell.font = Font(bold=True)

    n_cols = max(len(r) for r in rows)
    for idx in range(1, n_cols + 1):
        longest = max((len(r[idx - 1]) for r in rows if len(r) >= idx),
            default=0,)
        ws.column_dimensions[get_column_letter(idx)].width = max(MIN_WIDTH, longest + 2)

    dst.parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)
if __name__ == "__main__":
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
