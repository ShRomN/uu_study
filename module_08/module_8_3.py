class IncorrectVinNumber(Exception):
    """
    Класс исключения IncorrectVinNumber.
    """
    def __init__(self, message):
        """
        Конструктор класса IncorrectVinNumber.
        :param message: текст с сообщением исключения.
        """
        super().__init__()
        self.message = message


class IncorrectCarNumbers(Exception):
    """
    Класс исключения IncorrectCarNumbers.
    """
    def __init__(self, message):
        """
        Конструктор класса IncorrectCarNumbers.
        :param message: текст с сообщением исключения.
        """
        super().__init__()
        self.message = message


class Car:
    """
    Класс машины.
    """
    def __init__(self, model:str, vin:int, numbers:str):
        """
        Конструктор класса Car.
        :param model: модель машины;
        :param vin: vin-код машины.
        """
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        """
        Метод проверки значения vin-кода.
        :param vin_number: проверяемое значение vin-кода.
        :return: True если vin-код корректен, иначе False.
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        """
        Метод проверки значения номера машины.
        :param numbers: проверяемое значение номера машины.
        :return: True если номер машины корректен, иначе False.
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True



# Тестовые данные
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
