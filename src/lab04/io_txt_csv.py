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

if __name__ == "__main__":
    write_csv([("привет", 2), ("мир", 1)], "data/lab04/check.csv", header=("word", "count"))
    write_csv([], "data/lab04/empty.csv")
    write_csv([], "data/lab04/header_only.csv", header=("a", "b"))
    try:
        write_csv([("a", 1), ("b",)], "data/lab04/bad.csv")
    except ValueError as e:
        print("ValueError:", e)
