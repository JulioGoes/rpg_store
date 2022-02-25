from shutil import Error
import sqlite3


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('Database/database.db')
    except Error as e:
        print(e)

    return connection


def delete_from_database(name):
    connection = create_connection()
    cursor = connection.cursor()

    sql = 'DELETE FROM Products WHERE name = ?'
    val = (name,)
    cursor.execute(sql, val)

    connection.commit()
