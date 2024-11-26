def print_params(a = 1, b = 'строка', c = True):
    """
    Функция вывода параметров
    """
    print(a, b, c)


# Проверка работы функции - print_params
print_params(b = 25)
print_params(c = [1,2,3])

# Создаем список
values_list = [1, 2.1, '3']
# Создаем словарь
values_dict = {'a': 4, 'b': 5.1, 'c': '6'}

# Передаем список и словарь с помощью распаковки 
print_params(*values_list)
print_params(**values_dict)

# Создаем список с двумя элементами разных типов
values_list_2 = [7, 8.1]

# Проверяем работу передавая список и параметр
print_params(*values_list_2, 42)

# Вывод тестовых данных
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
