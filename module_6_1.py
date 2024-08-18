class Animal:
    """
    Класс животных.
    """
    def __init__(self, alive:bool=True, fed:bool=False):
        """
        Конструктор класса Animal.
        :param alive: флаг, является ли животное живым;
        :param fed: флаг, является ли животное сытым.
        """
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        """
        Метод для кормления животного.
        :param food: объект еды.
        """
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    """
    Класс растений.
    """
    def __init__(self, name:str='', edible:bool=False):
        """
        Конструктор класса Plant.
        :param name: название растения;
        :param edible: флаг, является ли растение съедобным.
        """
        self.name = name
        self.edible = edible


class Mammal(Animal):
    """
    Класс млекопитающих.
    """
    def __init__(self, name:str, alive:bool=True, fed:bool=False):
        """
        Конструктор класса Mammal.
        :param name: название млекопитающего;
        :param alive: флаг, является ли животное живым;
        :param fed: флаг, является ли животное сытым.
        """
        super().__init__(alive, fed)
        self.name = name
        

class Predator(Animal):
    """
    Класс хищников.
    """
    def __init__(self, name:str, alive:bool=True, fed:bool=False):
        """
        Конструктор класса Predator.
        :param name: название хищника;
        :param alive: флаг, является ли животное живым;
        :param fed: флаг, является ли животное сытым.
        """        
        super().__init__(alive, fed)
        self.name = name


class Flower(Plant):
    """
    Класс цветов.
    """


class Fruit(Plant):
    """
    Класс фруктов.
    """
    def __init__(self, name:str='', edible:bool=False):
        """
        Конструктор класса Fruit.
        :param name: название фрукта;
        :param edible: флаг, является ли фрукт съедобным.
        """
        super().__init__(name, edible)
        # Переопределяем атрибут
        self.edible = True


# Тестовые данные
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
