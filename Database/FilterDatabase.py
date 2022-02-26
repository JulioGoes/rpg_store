import sqlite3


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('Database/database.db')
    except ValueError as e:
        print(e)

    return connection


def consult_database_by_type(product_type):
    connection = create_connection()
    cursor = connection.cursor()

    sql = 'SELECT name, type, seller FROM Products WHERE type = ?'
    val = (product_type, )
    products = cursor.execute(sql, val).fetchall()

    return products
