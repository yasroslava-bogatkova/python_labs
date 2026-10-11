from text import normalize, tokenize, count_freq, top_n

table_mode=True

line = input()
tokens = tokenize(normalize(line))
freq_dict = count_freq(tokens)

print(f'Всего слов:{len(tokens)}')
print(f'Уникальных слов:{len(freq_dict)}')
print('Топ-5:')

top_words=top_n(freq_dict)
if table_mode and top_words:
    max_len=max(len(word) for word, _ in top_words)
    col_width=max(max_len,5)
    print(f"{'слово':<{col_width}} | частота")
    print(f"{'-' * col_width}-----------")
    for word, count in top_words:
        print(f"{word:<{col_width}} | {count}")
else:
    for word, count in top_words:
        print(f'{word}: {count}')







