from shutil import Error
import sqlite3


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('Database/database.db')
    except Error as e:
        print(e)

    return connection


def insert_database(product_name, product_type, product_seller):
    connection = create_connection()
    cursor = connection.cursor()

    sql = 'INSERT INTO Products (name, type, seller) VALUES (?, ?, ?)'
    val = (product_name, product_type, product_seller)
    cursor.execute(sql, val)

    connection.commit()
