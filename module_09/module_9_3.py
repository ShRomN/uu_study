# Исходные данные
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Формирование переменных срезультатами
first_result = list(filter(lambda z: z != 0, map(lambda x, y: len(x) - len(y), first, second)))
second_result = list(map(lambda i: len(first[i]) == len(second[i]), range(len(first))))

# Вывод результатов
print(list(first_result))
print(list(second_result))
