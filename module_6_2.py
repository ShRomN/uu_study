class Vehicle:
    """
    Класс транспортных средств (ТС).
    """
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, model:str, color:str, engin_power:int):
        """
        Конструктор класса Vehicle.
        :param owner: собственник ТС;
        :param model: модель ТС;
        :param color: цвет ТС;
        :param engin_power: мощность двигателя ТС.
        """
        self.owner = owner
        self.__model = model
        self.__engin_power = engin_power
        self.__color = color

    def get_model(self):
        """
        Метод возвращает строку с информацией о модели ТС.
        """
        return f'Модель: {self.__model}'
    
    def get_horsepower(self):
        """
        Метод возвращает строку с информацией о мощности двигателя ТС.
        """
        return f'Мощность двигателя: {self.__engin_power}'
    
    def get_color(self):
        """
        Метод возвращает строку с информацией о цвете ТС.
        """
        return f'Цвет: {self.__color}'
    
    def print_info(self):
        """
        Метод выводит обобщенную информацию о ТС.
        """
        print(
            self.get_model(),
            self.get_horsepower(),
            self.get_color(),
            f'Владелец: {self.owner}',
            sep='\n'
        )
    
    def set_color(self, new_color:str):
        """
        Метод изменяющий цвет объекта ТС.
        :param new_color: цвет ТС.
        """
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    """
    Класс седанов.
    """
    __PASSENGERS_LIMIT = 5
        


# Тестовые данные
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()