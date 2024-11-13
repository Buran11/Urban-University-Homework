import sqlite3
import random

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')  # создание таблицы

# создание индекса
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(30):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
#                    (f'newuser {i}', f'{i}ex@gmail.com', str(random.randint(18, 55))))

# CRUD - Create, Read, Update, Delete
# cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', # добавление данных
#                ('newuser', 'ex@gmail.com', '28'))

# cursor.execute('SELECT * FROM Users')  # чтение данных
# SELECT FROM WHERE GROUP BY HAVING ORDER BY

# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (29,))

# cursor.execute('SELECT username, age FROM Users GROUP BY AGE')

# users = cursor.fetchall()  # получение данных
# for user in users:
#     print(user)

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?',
#                (29, 'newuser'))  # изменение данных

# cursor.execute('DELETE FROM Users WHERE username = ?',
#                ('newuser',))  # удаление данных

# cursor.execute('SELECT COUNT(*) FROM Users')  # подсчет
# cursor.execute('SELECT COUNT(*) FROM Users WHERE age > ?', (28, ))
cursor.execute('SELECT SUM(age) FROM Users')
total1 = cursor.fetchone()[0]  # Получаем один конкретный элемент
cursor.execute('SELECT COUNT(*) FROM Users')
total2 = cursor.fetchone()[0]
print(total1, total1/total2)
# cursor.execute('SELECT AVG(age) FROM Users') # средний возраст
# cursor.execute('SELECT MIN(age) FROM Users') # минимум
cursor.execute('SELECT MAX(age) FROM Users')  # максимум
avg_age = cursor.fetchone()[0]
print(avg_age)


connection.commit()
connection.close()
