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


# Тестовые данные
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
