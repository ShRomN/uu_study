def apply_all_func(int_list, *functions):
    """
    Метод проверки значения vin-кода.
    :param int_list: список из чисел (int, float);
    :param functions: неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел).
    :return: словарь с ключами названия функций а значениями результат их работы.
    """
    # return {f.__name__: f(int_list) for f in functions}

    result = {}
    for f in functions:
        result[f.__name__] = f(int_list)
    return result


# Тестовые данные
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
