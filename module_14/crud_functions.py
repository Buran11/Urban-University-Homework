import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')  # MODULE_14_5
    connection.commit()
    connection.close()


def is_included(username):  # MODULE_14_5
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    check_user = cursor.execute(
        'SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        connection.commit()
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True


def is_included_product(title):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    check_product = cursor.execute(
        'SELECT * FROM Products WHERE title = ?', (title,))
    if check_product.fetchone() is None:
        connection.commit()
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True


def add_user(username, email, age):  # MODULE_14_5
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    if is_included(username) == False:
        cursor.execute(f'''
                       INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', '{1000}')
        ''')
        connection.commit()

    connection.commit()
    connection.close()


def add_product(title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    if is_included_product(title) == False:
        cursor.execute(f'''
                       INSERT INTO Products (title, description, price) VALUES ('{title}', '{description}', '{price}')
        ''')
        connection.commit()

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products
