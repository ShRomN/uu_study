# Исходные данные
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Формирование переменных срезультатами
first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {i: len(i) for i in (first_strings + second_strings) if len(i) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
