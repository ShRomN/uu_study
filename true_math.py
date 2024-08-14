from math import inf

def divide(first, second):
    """
    Функция возвращающая результат деления или inf, есло second == 0.
    """
    return first / second if second != 0 else inf
