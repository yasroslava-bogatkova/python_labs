import csv
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import (
    linear_search,
    binary_search,
    two_sum_brute,
    two_sum_fast,
)


def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]


def get_data(n):
    """Берёт данные из CSV через read_numbers, если файл есть, иначе генерирует."""
    sample_path = Path(f"data/samples/lab07/numbers_{n}.csv")
    if sample_path.exists():
        return read_numbers(sample_path)
    return [random.randint(-10**6, 10**6) for _ in range(n)]


def bench_sorts(n):
    data = get_data(n)
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", f"{t:.6f}"))

    for name, fn in (
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ):
        if n >= 100_000:
            rows.append(("sort", n, name, "> 60 s"))
            continue

        t = timeit.timeit(lambda: fn(data), number=1)
        rows.append(("sort", n, name, f"{t:.6f}"))

    return rows


def bench_search():
    n = 100_000
    queries_count = 10_000
    data = get_data(n)

    queries = [
        random.choice(data) if i % 2 == 0 else random.randint(-10**6, 10**6)
        for i in range(queries_count)
    ]

    rows = []

    # 1. Линейный поиск
    t_lin = timeit.timeit(
        lambda: [linear_search(data, q) for q in queries],
        number=1,
    )
    rows.append(("search_10k", n, "linear_search", f"{t_lin:.6f}"))

    # 2. Предварительная сортировка для бинарного поиска
    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)
    rows.append(("search_prep", n, "sort_for_binary", f"{t_sort:.6f}"))

    # 3. Бинарный поиск
    t_bin = timeit.timeit(
        lambda: [binary_search(sorted_data, q) for q in queries],
        number=1,
    )
    rows.append(("search_10k", n, "binary_search", f"{t_bin:.6f}"))

    return rows


def bench_two_sum():
    rows = []
    for n in [1_000, 10_000]:
        data = get_data(n)
        target = data[-1] + data[-2]

        t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))

        loops = 100
        t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=loops) / loops
        rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))

    return rows


def main():
    random.seed(42)
    all_rows = []
    for n in [1_000, 10_000, 100_000]:
        all_rows.extend(bench_sorts(n))
    all_rows.extend(bench_search())
    all_rows.extend(bench_two_sum())

    header = ("task", "n", "impl", "seconds")
    print(f"{header:<14} | {header:>8} | {header:<18} | {header:>12}")
    print("-" * 62)
    for task, n, impl, sec in all_rows:
        print(f"{task:<14} | {n:>8} | {impl:<18} | {sec:>12}")

    out_path = Path("data/lab07/bench.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(all_rows, out_path, header=list(header))
    print(f"\nРезультаты сохранены в {out_path}")


if __name__ == "__main__":
    main()
