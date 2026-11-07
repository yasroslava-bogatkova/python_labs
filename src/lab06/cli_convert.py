import argparse
import sys
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


COMMANDS = {
    "json2csv": (json_to_csv, ".json", ".csv"),
    "csv2json": (csv_to_json, ".csv", ".json"),
    "csv2xlsx": (csv_to_xlsx, ".csv", ".xlsx"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Конвертеры данных (ЛР6)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    helps = {
        "json2csv": "Конвертировать JSON в CSV",
        "csv2json": "Конвертировать CSV в JSON",
        "csv2xlsx": "Конвертировать CSV в XLSX",
    }
    for name, text in helps.items():
        p = sub.add_parser(name, help=text, description=text)
        p.add_argument("--in", dest="input", required=True, help="Входной файл")
        p.add_argument("--out", dest="output", required=True, help="Выходной файл")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    func, in_ext, out_ext = COMMANDS[args.cmd]
    src, dst = Path(args.input), Path(args.output)

    if src.suffix.lower() != in_ext:
        parser.error(f"входной файл для {args.cmd} должен иметь расширение {in_ext}")
    if dst.suffix.lower() != out_ext:
        parser.error(f"выходной файл для {args.cmd} должен иметь расширение {out_ext}")

    try:
        if not src.is_file():
            raise FileNotFoundError(f"Входной файл не найден: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        func(str(src), str(dst))
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        return 1

    print(f"Готово: {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())