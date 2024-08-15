class House:
    """
    Класс содержащий информацию о объектах домов.
    """
    def __init__(self, name: str, number_of_floors: int):
        """
        Конструктор класса House.
        Атрибуты:
        name - имя;
        number_of_floors - кол-во этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        """
        Метод выводит на экран (в консоль) значения от 1 до new_floor(включительно).
        Атрибуты:
        new_floor - номер этажа, на который нужно приехать.
        """
        print(*range(1, new_floor + 1), sep='\n') if 0 < new_floor <= self.number_of_floors else print(
            'Такого этажа не существует')

    def __len__(self):
        """
        Метод возвращает кол-во этажей здания.
        """
        return self.number_of_floors

    def __str__(self):
        """
        Метод возвращает строковое представление объекта.
        """
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        """
        Метод (перегрузка оператора ==)  проверки равенства двух объектов self и объект other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        """
        Метод (перегрузка оператора <) проверки меньше ли объект self чем объект other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        """
        Метод (перегрузка оператора <=) проверки меньше или равен объект self объекту other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """
        Метод (перегрузка оператора >) проверки больше ли объект self чем объект other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """
        Метод (перегрузка оператора >=) проверки больше или равен объект self объекту other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """
        Метод (перегрузка оператора !=) проверки неравенсатва объекта self и объекта other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return not self.__eq__(other)

    def __add__(self, value: int):
        """
        Метод (перегрузка оператора +) увеличивает кол-во этажей на переданное
        значение value, возвращает сам объект.
        Атрибуты:
        value - значение на которое необходимо увеличить кол-во этажей.
        """
        self.number_of_floors += (value if isinstance(value, int) else 0)
        return self

    def __radd__(self, value: int):
        """
        Метод (перегрузка оператора +) увеличивает кол-во этажей на переданное
        значение value, возвращает сам объект.
        Атрибуты:
        value - значение на которое необходимо увеличить кол-во этажей.
        """
        return self.__add__(value)

    def __iadd__(self, value: int):
        """
        Метод (перегрузка оператора +=) увеличивает кол-во этажей на переданное
        значение value, возвращает сам объект.
        Атрибуты:
        value - значение на которое необходимо увеличить кол-во этажей.
        """
        return self.__add__(value)


# Тестовые данные
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
