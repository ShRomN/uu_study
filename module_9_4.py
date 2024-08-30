from random import choice

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name,'w', encoding='utf-8') as file:
            for l in data_set:
                file.write(str(l) + '\n')
    
    return write_everything


class MysticBall:
    """
    Класс содержащий информацию о объектах домов.
    """
    def __init__(self, *words):
        """
        Конструктор класса MysticBall.
        :param words: список строк.
        """
        self.words = words

    def __call__(self):
        """
        Метод срабатываемый при использовании объекта как функции.
        """
        return choice(self.words)


# Lambda-функция:
# Исходные данные
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Вывод результатов
print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
# Тестовые данные
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
