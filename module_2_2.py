# Подаются 3 целых числа и записываются в переменные
first, second, third = int(input()), int(input()), int(input())

# Если все числа равны между собой, то вывести 3
if first == second and first == third:
    print(0)
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
elif first == second or second == third or first == third:
    print(2)
# Если равных чисел среди 3-х вообще нет, то вывести 0
else:
    print(0)
