calls = 0

def count_calls():
    """
    Функция подсчитывающая вызовы остальных функций.
    """
    global calls
    calls += 1

def string_info(s:str):
    """
    Функция возвращающая кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    """
    count_calls()
    return (len(s), s.upper(), s.lower())


def is_contains(string:str, list_to_search:list):
    """
    Функция возвращает True если строка - s находится в списке - l.
    """
    count_calls()
    for i in list_to_search:
        if i.lower() == string_info(string)[2]:
            return True
    return False


# Вызываем функции произвольное кол-во раз с произвольными данными
lst = ['abcd', 'efg', 'hi', 'jklmno', 'pqrs', 't', 'u', 'vwxyz']
l_strings = ['AbCD', 'ABc', 'abcd', 'w', 'PqRs', '__t', 'uuu', 'XYU']

for i in l_strings:
    is_contains(i, lst)

# Выводим значение переменной calls
print(calls)
