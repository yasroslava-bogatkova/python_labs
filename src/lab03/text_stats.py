from text import normalize, tokenize, count_freq, top_n

table_mode=True

line = input()
tokens = tokenize(normalize(line))
freq_dict = count_freq(tokens)

print(f'Всего слов:{len(tokens)}')
print(f'Уникальных слов:{len(freq_dict)}')
print('Топ-5:')
for word, count in top_n(freq_dict):
    print(f"{word}:{count}")
    







