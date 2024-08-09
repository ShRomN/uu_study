# Даны следующие данные:
# Список: 
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: 
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Составляем словарь
my_dict = dict(map(lambda itm: (itm[1], sum(grades[itm[0]]) / len(grades[itm[0]])), enumerate(sorted(students))))
print(my_dict)
