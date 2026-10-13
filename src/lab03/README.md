# ЛР3 - Тексты и частоты слов (словарь/множество)
## Задание А
### normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.casefold() if casefold else text.lower()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
        clean_text=text.replace('\t',' ').replace('\n',' ')
        return ' '.join(clean_text.split())
```
функция использует casefold если флаг равен True, иначе срабатывает перевод текста в нижний регистр,используя lower.Если включено,заменяет ё на е, удаляет все скрытые символы и лишние пробелы,возвращая строку, где слова разделены одним пробелом

![](/images/lab03/normalize.png)
### tokenize
``` python
def tokenize(text: str) -> list[str]:
    pattern=r'\w+(?:-\w+)*'
    return re.findall(pattern,text)
```
Функция использует регулярное выражение, чтобы найти все совпадения, проходясь по строке

![](/images/lab03/tokenize.png)

### count_freq +top_n
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
        freq_dict={}
        for token in tokens:
            freq_dict[token]=freq_dict.get(token,0)+1
        return freq_dict
```
Функция создает словарь с ключом, перебирает список слов и считает сколько раз слово встречается, get создает новые ключи со счетчиком 1 или увеличивает уже существующие

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]
```
Функция преобразует словарь в список пар (слово:частота) и сортирует по уменьшению количества повторений, а при совпадении частот сортирует по алфавиту.

![](/images/lab03/count_freq+top_n.png)

## Задание B
```python
from text import normalize, tokenize, count_freq, top_n

line = input()
tokens = tokenize(normalize(line))
freq_dict = count_freq(tokens)

print(f'Всего слов:{len(tokens)}')
print(f'Уникальных слов:{len(freq_dict)}')
print('Топ-5:')
for word, count in top_n(freq_dict):
    print(f"{word}:{count}")
```
Функция принимает строку,нормализует ее, разбивает на отдельные слова и подсчитывает частоту каждого слова, выводит длину списка токенов,а для уникальных слов выводит длину словаря freq_dict, в конце выводит через цикл топ пять слов из списка top_n
![](/images/lab03/text_stats.png)