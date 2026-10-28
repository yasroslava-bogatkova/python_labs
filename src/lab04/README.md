# ЛР4 — Файлы:TXT/CSV и отчёты по текстовой статистике
## Задание A:
Модуль src/lab04/io_txt_csv.py: read_text читает текстовый файл,а write_csv записывает CSV
по умолчанию стоит кодировка utf-8,другую кодировку передают флагом --encoding cp1251,файл читается целиком в память, для больших файлов лучше читать построчно; при пустом входе: в отчет пишется word,count
```python
from pathlib import Path
import csv
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    """Открывает файл на чтение в указанной кодировке и возвращает текст как строку."""
    return p.read_text(encoding=encoding)
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        expected_length=len(rows[0])
        for row in rows:
            if len(row)!=expected_length:
                raise ValueError("Каждая строка должна иметь одинаковую длину")

    with open(path,'w',encoding="utf-8", newline="") as f:
        csv_writer=csv.writer(f,delimiter=',')
        if header is not None:
            csv_writer.writerow(header)
        csv_writer.writerows(rows)
```


## Задание B
Программа читает текст,считает частоты слов, импортируя функции из ЛР3, и сохраняет в report.csv, в консоль выводит кол-во всех слов, уникальных и топ-5
вход читается в utf-8, как и csv отчет, другую кодировку передают флагом --encoding cp1251, при не нахождении файла или не подходящей кодировке программа пишет сообщение и выходит с кодом 1
```python
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
```

## Тесты
###  Файл - "Привет, мир! Привет!!!"
Запуск команд из корня проекта python_labs
#### Запуск: py src/lab04/text_report.py

![](/images/lab04/test_a.png)

### Пустой файл
#### Запуск: py src/lab04/text_report --in data/lab04/empty.txt --out data/lab04/report_empty.csv

![](/images/lab04/test_b.png)

### Другая кодировка
#### Запуск: py src/lab04/text_report.py --in data/lab04/input_cp1251.txt --out data/lab04/report_cp1251.csv --encoding cp1251

![](/images/lab04/test_c.png)