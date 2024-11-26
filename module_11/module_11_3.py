import inspect
import pandas as pd

def introspection_info(obj):
    """
    Функция проводящая интроспекцию объекта и выводящая словарь с информацией
    о его типе, атрибутах, методах, модуле и цепочки наследования.
    :param obj: передаваемы объект для сбора данных о нем.
    """
    return {
        'type': type(obj).__name__,
        'attributes': list(map(lambda y: y[0], inspect.getmembers(obj, lambda x: not callable(x)))),
        'methods': list(map(lambda y: y[0], inspect.getmembers(obj, callable))),
        'module': '__main__' if inspect.getmodule(obj) is None else inspect.getmodule(obj).__name__,
        'MRO': inspect.getmro(type(obj))
    }


# Тестовые данные
number_info = introspection_info(42)
print(number_info)

print('-' * 90)

pd_info = introspection_info(pd)
print(pd_info)
