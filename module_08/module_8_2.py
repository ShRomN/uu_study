def personal_sum(numbers):
    """
    Функция складывает значения из коллекции numbers.
    :param numbers: коллекция значений для сложения.
    :return: кортеж состаящий из двух элементов суммы элементов которые удалось
    сложить и колличества некорректных элементов (не являются числами).
    """
    result = 0
    incorrect_data = 0

    for i in numbers:

        try:
            result += i

        except TypeError as e:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')

    return(result, incorrect_data)


def calculate_average(numbers):
    """
    Функция расчета среднего значения чисел из коллекции numbers.
    :param numbers: коллекция значений для расчета.
    :return: среднее арифмитическое чисел коллекции numbers.
    """
    try:
        sum, incor_count = personal_sum(numbers)
        result = sum / (len(numbers) - incor_count)
        return result
    
    except ZeroDivisionError as e:
        return 0
    
    except TypeError as e:
        print('В numbers записан некорректный тип данных')
        return


# Тестовые данные
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
