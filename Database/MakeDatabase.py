from shutil import Error
import sqlite3


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('Database/database.db')
    except Error as e:
        print(e)

    return connection


def create_table_products(connection):
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS Products \
        (name TEXT, type TEXT, seller TEXT)')

    connection.commit()


# create_table_products()
def add_product_to_table(connection, produto):
    cursor = connection.cursor()

    sql = "INSERT INTO Products (name, type, seller) VALUES (?, ?, ?)"
    cursor.execute(sql, produto)

    connection.commit()
    return cursor.lastrowid


# connection = create_connection('Database/database.db')
# create_table_products(connection)
# add_product_to_table(connection, ('Dados Blend', 'Dado', 'Mercado RPG'))
