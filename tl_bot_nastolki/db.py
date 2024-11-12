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

cursor.execute('SELECT username, age FROM Users GROUP BY AGE')

users = cursor.fetchall()
for user in users:
    print(user)

# cursor.execute('UPDATE Users SET age = ? WHERE username = ?',
#                (29, 'newuser'))  # изменение данных

# cursor.execute('DELETE FROM Users WHERE username = ?',
#                ('newuser',))  # удаление данных

connection.commit()
connection.close()
