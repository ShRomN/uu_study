def add_everything_up(a, b):
    """
    Функция складывает числа(int, float) и строки(str).
    :param a: первое значение для сложения; 
    :param b: второе значение для сложения.
    :return: результат сложения двух чисел или строк.
    """
    try:
        return a + b
    except TypeError as e:
        return f'{a}{b}'
    

# Тестовые данные
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
