# 2024/01/30 00:00|Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
import sqlite3

# Создайте таблицу Users
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# MODULE_14_1
# Заполните её 10 записями
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

# cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', 500, 1)

cursor.execute('SELECT id, username, age, balance FROM Users GROUP BY AGE')
users = cursor.fetchall()

# Обновите balance у каждой 2ой записи начиная с 1ой на 500
# for user in users:
#     if int(user[0]) % 2 == 1:
#         cursor.execute(
#             'UPDATE Users SET balance = ? WHERE id = ?', (user[3] - 500, user[0]))
#         print(user)

# Удалите каждую 3ую запись в таблице начиная с 1ой
# count = 1
# for user in users:
#     if count == int(user[0]):
#         cursor.execute('DELETE FROM Users WHERE id = ?', (user[0],))
#         count += 3

# MODULE_14_2
# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))
# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
# print(total)

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM Users')
total_sum = cursor.fetchone()[0]
# print(total_sum)

# Вывести в консоль средний баланс всех пользователей.
cursor.execute('SELECT AVG(balance) FROM Users')
total_avg = cursor.fetchone()[0]
print(total_avg)

connection.commit()
connection.close()
