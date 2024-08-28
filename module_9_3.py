# Исходные данные
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Формирование переменных срезультатами
first_result = list(filter(lambda y: y != 0, map(lambda x: len(x[0]) - len(x[1]), zip(first, second))))
second_result = list(map(lambda i: len(first[i]) == len(second[i]), range(len(first))))

# Вывод результатов
print(list(first_result))
print(list(second_result))
