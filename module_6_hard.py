from math import pi

class Figure:
    """
    Класс фигур.
    """
    sides_count = 0

    def __init__(self, color=None, *sides):
        """
        Конструктор класса Figure.
        :param color: кортеж RGB цветов объекта с их значениями;
        :param sides: аргументы сторон с их длиннами.
        """
        if color is None:
            self.__color = (255, 255, 255)
        else:
            self.set_color(*color)

        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.set_sides(*sides)

        self.field = False

    def get_color(self):
        """
        Метод получения значения цвета объекта.
        :return: список с целыми значениями RGB цветов.
        """
        return self.__color
    
    def __is_valid_color(self, r, g, b):
        """
        Метод проверки цветовых значений.
        :param r: значение красного цвета;
        :param g: зеленого цвета;
        :param b: значение синего цвета.
        :return: True если цвета корректны, иначе False.
        """
        return all(map(lambda x: 0 <= x <= 255, (r, g, b)))

    def set_color(self, r, g, b):
        """
        Метод установки нового цвета объекта.
        :param r: значение красного цвета;
        :param g: зеленого цвета;
        :param b: значение синего цвета.
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            pass

    def __is_valid_sides(self, *args):
        """
        Метод проверки сторон на корректность.
        :param args: список параметров со значеними сторон.
        :return: True если кол-во сторон совпадают и все значения положительные целые числа, иначе False.
        """
        return all(map(lambda x: isinstance(x, int) and x > 0, args)) and len(args) == self.sides_count

    def get_sides(self):
        """
        Метод получения значений сторон объекта.
        :return: список с целыми значениями сторон объекта.
        """
        return self.__sides

    def __len__(self):
        """
        Метод получения периметра объекта.
        :return: периметр объекта.
        """
        return sum(self.__sides)
    
    def set_sides(self, *new_sides):
        """
        Метод установки новых значений сторон объекта.
        :param new_sides: список параметров со значеними сторон.
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            pass


class Circle(Figure):
    """
    Класс круга.
    """
    sides_count = 1

    def __init__(self, color=None, *sides):
        """
        Конструктор класса Circle.
        :param color: кортеж RGB цветов объекта с их значениями;
        :param sides: аргументы сторон с их длиннами.
        """
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0]

    def get_square(self):
        """
        Метод получения площади круга.
        :return: значение площади круга.
        """
        return pi * self.__radius ** 2


class Triangle(Figure):
    """
    Класс триугольника.
    """
    sides_count = 3

    def __init__(self, color=None, *sides):
        """
        Конструктор класса Triangle.
        :param color: кортеж RGB цветов объекта с их значениями;
        :param sides: аргументы сторон с их длиннами.
        """
        super().__init__(color, *sides)


    def get_square(self):
        """
        Метод получения площади триугольника.
        :return: значение площади триугольника.
        """
        p = len(self) / 2
        return (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5


class Cube(Figure):
    """
    Класс куба.
    """
    sides_count = 12

    def __init__(self, color=None, *sides):
        """
        Конструктор класса Cube.
        :param color: кортеж RGB цветов объекта с их значениями;
        :param sides: аргументы сторон с их длиннами.
        """
        super().__init__(color, *sides)

    def get_volume(self):
        """
        Метод получения объема куба.
        :return: значение объема куба.
        """
        return self.get_sides()[0] ** 3



# Тестовые данные
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
