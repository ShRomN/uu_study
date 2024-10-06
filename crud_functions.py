import sqlite3



def initiate_db():
    """
    Функция инициализации базы данных products_db.db.
    """
    # Подключаемся к БД
    db_name = 'products_db.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Создаем таблицу в БД с требуемыми полями
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL);
        '''
    )

    # # Заполняем базу данных 4-мя значениями
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
    #         (f'Продукт {i}', f'Описание {i}', i * 100)
    #     )

    # Применяем изменения
    connection.commit()
    # Завершаем соединение
    connection.close()


def get_all_products():
    """
    AФункция получения всех записей базы данных.
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