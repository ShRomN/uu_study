from threading import Thread
from time import sleep

class Knight(Thread):
    """
    Класс содержащий информацию о рыцаре.
    """
    def __init__(self, name:str, power:int):
        """
        Конструктор класса House.
        :param name: имя рыцаря;
        :param power: сила рыцаря.
        """
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        """
        Метод выполняющий сражение рыцаря.
        """
        print(f'{self.name}, на нас напали!')

        enemies_count = 100 - self.power
        days_count = 1

        while enemies_count > 0:
            sleep(1)
            print(f'{self.name} сражается {days_count}..., осталось {enemies_count} воинов.')
            enemies_count -= self.power
            days_count += 1
        
        print(f'{self.name} одержал победу спустя {days_count} дней (дня)!')


# Тестовые данные
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
