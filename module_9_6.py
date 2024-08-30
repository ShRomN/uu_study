def all_variants(text:str):
    """
    Генератор возвращающий все варианты подстрок строки text.
    Атрибуты:
    :param text: исходная строка.
    :return: возвращантся один из вариантов переданной подстроки text.
    """
    i = 1
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            if j + i > len(text):
                continue
            yield text[j:j + i]


# Тестовые данные
a = all_variants("abc")
for i in a:
    print(i)