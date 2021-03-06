from shutil import Error
import sqlite3


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('Database/database.db')
    except Error as e:
        print(e)

    return connection


def consult_database():
    connection = create_connection()
    cursor = connection.cursor()

    sql = 'SELECT name, type, seller FROM Products'
    products = cursor.execute(sql).fetchall()

    return products
