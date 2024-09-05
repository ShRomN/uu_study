from random import randint
from time import sleep
from threading import Thread
from queue import Queue

class Table:
    """
    Класс содержащий информацию о столе.
    """
    def __init__(self, number:int=0, guest=None):
        """
        Конструктор класса Table.
        :param number: номер стола;
        :param guest: гость который сидит за данным столом.
        """
        self.number = number
        self.guest = guest


class Guest(Thread):
    """
    Класс содержащий информацию о госте.
    """
    def __init__(self, name:str):
        """
        Конструктор класса Guest.
        :param name: имя гостя.
        """
        super().__init__()
        self.name = name

    def run(self):
        """
        Метод выполняющий бронирование.
        """
        # Ожидание
        sleep(randint(3, 10))


class Cafe:
    """
    Класс содержащий информацию о кафе.
    """
    def __init__(self, *args):
        """
        Конструктор класса Cafe.
        :param args: кортеж неименованных параметров объектов - Table.
        """
        self.queue = Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests):
        """
        Метод обрабатывающий прибытие гостей.
        :param args: кортеж неименованных параметров объектов - Guest.
        """
        for guest in guests:
            tbl_idx = self.__get_empty_table()
            if tbl_idx != -1:
                self.tables[tbl_idx].guest = guest
                print(f'{guest.name} сел(-а) за стол номер {self.tables[tbl_idx].number}')
                guest.start()
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        """
        Метод обрабатывающий обслуживание гостей.
        """
        while not self.queue.empty() or not self.__is_all_tables_empty():
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                    # Проверяем очередь на пустоту и если она не пуста
                    # сажаем гостя за освободившийся стол 
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest.start()
        
        # Сообщение о окончании обслуживания гостей
        print('Все гости обслужены!')
        
    def __get_empty_table(self):
        """
        Метод возвращающий индекс пустого стола из списка - self.tables.
        :return: индекс пустого стола списка - self.tables или -1 если пустой стол отсутствует.
        """
        for i in range(len(self.tables)):
            if self.tables[i].guest is None:
                return i
        return -1

    def __is_all_tables_empty(self):
        """
        Метод проверяющий пустоту всех столов из списка - self.tables.
        :return: True если все столы всписке пусты иначе False.
        """
        return all(map(lambda tbl: tbl.guest is None, self.tables))


# Тестовые данные
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
