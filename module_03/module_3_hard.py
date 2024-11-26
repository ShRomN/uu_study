def calculate_structure_sum(obj):
    """
    Функция подсчета суммы элементов списка.
    """
    if isinstance(obj, (int, float)):
        return obj

    s = 0

    for el in obj:
        if isinstance(el, str):
            s += len(el)
        elif isinstance(el, (float, int)):
            s += el
        elif isinstance(el, (list, tuple, set)):
            s += calculate_structure_sum(el)
        elif isinstance(el, dict):
            s += calculate_structure_sum(el.keys()) + calculate_structure_sum(el.values())

    return s



# Тестовые данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# data_structure = 1
# data_structure = '12345'

result = calculate_structure_sum(data_structure)
print(result)
