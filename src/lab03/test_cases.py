from text import normalize,tokenize 
print('normalize')
print(f"{"ПрИвЕт\nМИр\t"} -> {normalize("ПрИвЕт\nМИр\t")}")
print(f"{"ёжик, Ёлка"} -> {normalize("ёжик, Ёлка",yo2e=True)}")
print(f"{"Hello\r\nWorld"} -> {normalize("Hello\r\nWorld")}")
print(f"{"  двойные   пробелы  "} -> {normalize("  двойные   пробелы  ")}")


print("tokenize")
print(f"{"привет мир"} -> {tokenize("привет мир")}")
print(f"{"hello,world!!!"} -> {tokenize("hello,world!!!")}")
print(f"{"по-настоящему круто"} -> {tokenize("по-настоящему круто")}")
print(f"{"2025 год"} -> {tokenize("2025 год")}")
print(f"{"emoji 😀 не слово"} -> {tokenize("emoji 😀 не слово")}")

print("count_freq + top_n")

first_case = count_freq(["a","b","a","c","b","a"])
print(f"{["a","b","a","c","b","a"]} -> {first_case}")
print(f"n=2: {top_n(first_case,n=2)}")


second_case = count_freq(["bb","aa","bb","aa","cc"])
print(f"{["bb","aa","bb","aa","cc"]} -> {second_case}")
print(f"n=2: {top_n(second_case, n=2)}")