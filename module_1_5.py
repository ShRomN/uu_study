# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных
immutable_var = (1, 2.1, '3')
# Выполните операции вывода кортежа immutable_var на экран
print('Immutable tuple:', immutable_var)
# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа
# immutable_var[0] = 5

# Создайте переменную mutable_list и присвойте ей список из нескольких элементов
mutable_list = [1, 2, 3]
# Измените элементы списка mutable_list
mutable_list[0] += 1
mutable_list[1] += 1
mutable_list[2] += 1
# Выведите на экран измененный список mutable_list
print('Mutable list:', mutable_list)
