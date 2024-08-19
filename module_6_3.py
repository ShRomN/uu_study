class Horse:
    """
    Класс лошади.
    """
    def __init__(self):
        """
        Конструктор класса Horse.
        :param x_distance: пройденный путь;
        :param sound: звук, который издаёт лошадь.
        """
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()


    def run(self, dx:int=0):
        """
        Метод изменения дистанции, увеличивает x_distance на dx.
        :param dx: значение на которе увеличивается дистанция (x_distance).
        """
        self.x_distance += dx


class Eagle:
    """
    Класс орла.
    """
    def __init__(self):
        """
        Конструктор класса Eagle.
        :param y_distance: высота полета;
        :param sound: звук, который издаёт орел.
        """
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy:int=0):
        """
        Метод изменения высоты полета, увеличивает y_distance на dy.
        :param dx: значение на которе увеличивается высота полета (y_distance).
        """
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """
    Класс пегаса.
    """
    def __init__(self, x_distance:int=0, y_distance:int=0, sound:str='Frrr'):
        """
        Конструктор класса Pegasus.
        :param y_distance: высота полета;
        :param sound: звук, который издаёт орел.
        """
        super().__init__()

    def move(self, dx:int= 0, dy:int=0):
        """
        Метод изменения высоты и расстояния полета, увеличивает
        x_distance и  y_distance на dx и dy соответственно.
        :param dx: значение на которе увеличивается дистанция (x_distance).
        :param dx: значение на которе увеличивается высота полета (y_distance).
        """
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        """
        Метод возвращает текущее положение пегаса.
        """
        return (self.x_distance, self.y_distance)
         
    def voice(self):
        """
        Метод печатает звук пегаса.
        """
        print(self.sound)



# Тестовые данные
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
