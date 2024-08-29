def all_variants(text):
    i = 1
    for i in range(1, len(text)):
        for j in range(len(text)):
            yield text[j:i]

# Тестовые данные
a = all_variants("abc")
for i in a:
    print(i)