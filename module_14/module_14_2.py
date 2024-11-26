import sqlite3

# Подключаемся к БД
db_name = 'not_telegram_2.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Создаем таблицу в БД с требуемыми полями
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
    '''
)
# Создаем индекс в таблице по полю -email
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

# Заполняем базу данных 10-ю значениями
for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
    )

# Обновляем balance у каждой 2-ой записи начиная с 1-ой на 500:
cursor.execute('UPDATE Users SET balance = ? WHERE (id % 2) = 1', (500,))

# Удаляем каждую 3-ую запись в таблице начиная с 1-ой:
cursor.execute('DELETE FROM Users WHERE (id % 3) = 1')

# Удаляем каждую запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Делаем выборку всех записей где возраст <> 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
# Формируем переменную с информацией о пользователях при помощи fetchall()
users = cursor.fetchall()

# # Выводим данные в требуемом формате
# for user in users:
#     print('Имя: {} | Почта: {} | Возраст: {} | Баланс: {}'.format(*user))

# Применяем изменения
connection.commit()

# ------  1-й вариант вывода среднего значения балансов  ------
# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Подсчёт кол-ва всех пользователей
cursor.execute('SELECT COUNT(id) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
print(all_balances / total_users)


# ------  2-й вариант вывода среднего значения балансов  ------
cursor.execute('SELECT SUM(balance) / COUNT(id) FROM Users')
print(cursor.fetchone()[0])

# Завершаем соединение
connection.close()
