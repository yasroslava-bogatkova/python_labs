def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa =rec
    
    if not isinstance(rec,tuple):
        raise TypeError("Запись должна быть кортежем")
    if len(rec)!=3:
        raise TypeError("В записи должны быть ФИО, группа, GPA")

    if not isinstance(fio,str) or not isinstance(group,str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa,(int,float)):
        raise TypeError("GPA должен быть числом")

    fio_parts=fio.split()
    group=group.strip()

    if not group:
        raise ValueError("Группа не может быть пустой")
    if len(fio_parts) not in(2,3):
        raise ValueError('ФИО должно состоять из 2-х и 3-х слов')
    if not(0.0<=gpa<=5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")
    
    last_name=fio_parts[0].capitalize()
    initials="".join(f'{part[0].upper()}.' for part in fio_parts[1:])

    return f'{last_name} {initials}, гр. {group}, GPA {gpa:.2f}'




test_cases=[("Иванов Иван Иванович", "BIVT-25", 4.6),("Петров Пётр", "IKBO-12", 5.0),("Петров Пётр Петрович", "IKBO-12", 5.0),("  сидорова  анна   сергеевна ", "ABB-01", 3.999),(" ","IKBO-12",4.5),("Петров Петр Петрович","BIVT-15",10.0),("Сидорова анна"," ",4.3)]
print('record')
for case in test_cases:
    try:
        result=format_record(case)
        print(f'{case} -> {result}')
    except (ValueError,TypeError) as error:
        print(f'{case} -> {error}')