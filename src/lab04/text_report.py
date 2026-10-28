import sys
import argparse
from collections import Counter
from pathlib import Path


root_dir = Path(__file__).resolve().parents[2]
"""Добавляем корень проекта в пути поиска модулей Python"""
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))
    
from src.lib.text import normalize,tokenize,count_freq,top_n
from src.lab04.io_txt_csv import read_text,write_csv

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> int:
    """Настройка аргументов командной строки (флагов)"""
    parser = argparse.ArgumentParser(description="Отчёт о частотах слов")
    parser.add_argument("--in", dest="input", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output", default="data/lab04/report.csv")
    parser.add_argument("--encoding", dest="encoding", default="utf-8")
    args = parser.parse_args()

    try:
        text = read_text(args.input, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}")
        return 1
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл в кодировке {args.encoding}. "
              f"Попробуйте --encoding cp1251",file=sys.stderr)
        return 1


    freq = frequencies_from_text(text)
    rows = sorted_word_counts(freq)
    write_csv(rows, args.output, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
