import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from src.lib.text import count_freq, normalize, tokenize, top_n



def read_text(path_str: str) -> str:
    path = Path(path_str)
    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return path.read_text(encoding="utf-8")


def cmd_cat(input_path: str, numbered: bool) -> None:
    text = read_text(input_path)
    for i, line in enumerate(text.splitlines(), start=1):
        print(f"{i:>6} {line}" if numbered else line)


def cmd_stats(input_path: str, top: int) -> None:
    text = read_text(input_path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word:<20} {count}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    sub = parser.add_subparsers(dest="command", required=True)
    cat_p = sub.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_p.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_p = sub.add_parser("stats", help="Частоты слов в тексте")
    stats_p.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_p.add_argument("--top",type=int,default=5,help="Сколько топ-слов выводить (по умолчанию 5)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("параметр --top должен быть положительным числом")
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print("Ошибка: файл не в кодировке UTF-8", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
