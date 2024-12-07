class User():
    """
    Класс описывающий объект - User.
    """
    def __init__(self, username:str, password:str, age:int) -> None:
        """
        Конструктор класса User.
        :param username: имя пользователя;
        :param password: пароль пользователя;
        :param age: возраст пользователя.
        """
        self.username = username
        self.password = password
        self.age = age

    def __str__(self) -> str:
        """
        Метод возвращий строковое представление объекта User.
        :return: строковое представление объекта User.
        """
        return f'Имя: {self.username}; Пароль: {self.password}; Возраст: {self.age}.'

    def __hash__(self):
        """
        Метод возвращий hash объекта User.
        :return: hash объекта User.
        """
        return hash(self.username)
    
    def __eq__(self, other):
        """
        Переопределение оператора сравнения объектов типа User (на равенство их хешей).
        :param other: объект User с которым сравнивается текущий объект.
        :return: True если объекты равны иначе False.
        """
        return hash(self) == hash(other)
    
    @staticmethod
    def in_list(name, l_users):
        """
        Статический метод проверки нахождения объекта в списке объектов User по его имени.
        :param name: имя пользователя для поиска в списке;
        :param l_users: список объектов User в котором осуществляется поиск.
        :return: True если объекты с именем есть в списке иначе False.
        """
        user = User(name, '1234567890', 1)
        return user in l_users
    

# Список пользователей для тестирования работы
users = [
        User('user_1', 'password_1', 1),
        User('user_2', 'password_2', 2),
        User('user_3', 'password_3', 3),
        User('user_4', 'password_4', 4),
        User('user_5', 'password_5', 5)
    ]