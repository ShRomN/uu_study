from random import randint
from threading import Lock
from time import sleep
from threading import Thread

class Bank:
    """
    Класс содержащий информацию о банке.
    """
    def __init__(self, balance:int=0):
        """
        Конструктор класса Bank.
        :param balance: стартовый баланс.
        """
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        """
        Метод выполняющий пополнение баланса.
        """
        for _ in range(100):
            add_sum = randint(50, 500)
            self.balance += add_sum
            print(f'Пополнение: {add_sum}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

        sleep(0.001)

    def take(self):
        """
        Метод выполняющий снятие с баланса.
        """
        for _ in range(100):
            sub_sum = randint(50, 500)
            print(f'Запрос на {sub_sum}')

            if sub_sum <= self.balance:
                self.balance -= sub_sum
                print(f'Снятие: {sub_sum}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                if not self.lock.locked():
                    self.lock.acquire()


# Тестовые данные
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
