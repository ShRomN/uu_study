def get_multiplied_digits(number):
    """
    Функция рекурсивного умножения цифр
    """
    str_number = str(number).replace('0', '')
    first = int(str_number[0])
    return (first * get_multiplied_digits(str_number[1:])) if len(str_number) > 1 else first

# Тестовые данные
result = get_multiplied_digits(40203)
print(result)
