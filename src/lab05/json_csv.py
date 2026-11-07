import csv
import json
from pathlib import Path


def _check_input(path: str, suffix: str) -> Path:
    p = Path(path)
    if p.suffix.lower() != suffix:
        raise ValueError(f"Неверный тип файла: ожидается {suffix}, получено '{p.suffix}'")
    if not p.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return p


def _check_output(path: str, suffix: str) -> Path:
    p = Path(path)
    if p.suffix.lower() != suffix:
        raise ValueError(f"Неверный тип файла: ожидается {suffix}, получено '{p.suffix}'")
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def json_to_csv(json_path: str, csv_path: str) -> None:
    src = _check_input(json_path, ".json")
    dst = _check_output(csv_path, ".csv")

    try:
        with src.open(encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON: {e}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен быть списком словарей")

    fieldnames: list[str] = []
    for item in data:
        for key in item:
            if key not in fieldnames:
                fieldnames.append(key)
    if not fieldnames:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    with dst.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({k: _cell(item.get(k)) for k in fieldnames})


def csv_to_json(csv_path: str, json_path: str) -> None:
    src = _check_input(csv_path, ".csv")
    dst = _check_output(json_path, ".json")

    with src.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        if not header or not any(h and h.strip() for h in header):
            raise ValueError("CSV пуст или не содержит заголовка")
        if any(not h or not h.strip() for h in header):
            raise ValueError("В заголовке CSV есть пустые названия колонок")
        rows = [{k: ("" if v is None else v) for k, v in row.items() if k is not None}
            for row in reader]

    if not rows:
        raise ValueError("CSV не содержит строк данных")

    with dst.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)