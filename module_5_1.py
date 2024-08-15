class House:
    """
    Класс содержащий информацию о объектах домов.
    """
    def __init__(self, name:str, number_of_floors:int):
        """
        Конструктор класса House.
        Атрибуты:
        name - имя;
        number_of_floors - кол-во этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor:int):
        """
        Метод выводит на экран (в консоль) значения от 1 до new_floor(включительно).
        Атрибуты:
        new_floor - номер этажа, на который нужно приехать.
        """
        print(*range(1, new_floor + 1), sep='\n') if 0 < new_floor <= self.number_of_floors else print('Такого этажа не существует')


# Тестовые данные
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
