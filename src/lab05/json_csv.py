import json
import csv
from pathlib import Path

def json_to_scv() ->None:
    j_path=Path(json_path)
    c_path=Path(csv_path)

    if not j_path.exists():
        raise FileExistsError(f"Файл не найден:{json_path}")
    with j_path.open('r',encoding='utf-8') as f:
        try:
            data=json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f'Некорректный формат JSON в файле {json_path}')

    if not data or not isinstance(data,list):
        raise ValueError ("Пустой JSON или не поддерживаемая структура")
    if not all(isinstance(item,dict) for item in data):
        raise ValueError('JSON должен содержать только список словарей')

    fieldnames=[]
    for item in data:
        for key in item.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    c_path.parent.mkdir(parents=True,exist_ok=True)

    with c_path.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)
def csv_to_json()->None:
    c_path=Path(csv_path)
    j_path=Path(json_path)

    if not c_path.exists():
        raise FileExistsError(f'Файл не найден:{csv_path}')
    data=[]
    with c_path.open('r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError(f"CSV файл {csv_path} без заголовка или пустой")
        for row in reader:
            data.append(row)

    if not data:
        raise ValueError(f'CSV не содержит данных')

    j_path.parent.mkdir(parents=True,exist_ok=True)
    with j_path.open('w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    