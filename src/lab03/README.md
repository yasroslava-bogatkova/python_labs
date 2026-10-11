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



### tokenize
``` python
def tokenize(text: str) -> list[str]:
    pattern=r'\w+(?:-\w+)*'
    return re.findall(pattern,text)
```



### count_freq +top_n
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
        freq_dict={}
        for token in tokens:
            freq_dict[token]=freq_dict.get(token,0)+1
        return freq_dict
```



```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]
```

