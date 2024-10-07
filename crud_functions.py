import sqlite3



def initiate_db():
    """
    Функция инициализации базы данных products_db.db.
    """
    # Подключаемся к БД
    db_name = 'products_db.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Создаем таблицу Products в БД с требуемыми полями
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL);
        '''
    )

    # # Заполняем таблицу Products базы данных 4-мя значениями
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
    #         (f'Продукт {i}', f'Описание {i}', i * 100)
    #     )

    # Создаем таблицу Users в БД с требуемыми полями
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL);
        '''
    )

    # Применяем изменения БД
    connection.commit()
    # Завершаем соединение
    connection.close()


def get_all_products():
    """
    Функция получения всех записей базы данных.
    """
    # Подключаемся к БД
    db_name = 'products_db.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('SELECT id, title, description, price From Products')
    products = cursor.fetchall()

    # Завершаем соединение
    connection.close()

    return products


def is_included(username:str):
    """
    Функция проверки наличия пользователя в таблице Users БД.
    :param username: имя пользователя.
    :return: True если пользователь есть, иначе False.
    """
    # Подключаемся к БД
    db_name = 'products_db.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Проверяем наличие пользователя в таблице
    cursor.execute(
        'SELECT * FROM Users WHERE username = ?;',
        (username, )
    )

    user = cursor.fetchone()

    # Завершаем соединение
    connection.close()
    # print(user)
    return bool(user)


def add_user(username:str, email:str, age:int, balance:int):
    """
    Функция добавления нового пользователя в таблицу Users.
    :param username: имя пользователя;
    :param email: адрес электронной почты;
    :param age: возраст пользователя;
    :param balance: баланс пользователя.
    """
    # Подключаемся к БД
    db_name = 'products_db.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Если пользователя нет в БД
    if not is_included(username):
        # Добавляем нового пользователя в таблицу
        cursor.execute(
            'INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
            (username, email, age, balance)
        )

    # Применяем изменения БД
    connection.commit()
    # Завершаем соединение
    connection.close()
