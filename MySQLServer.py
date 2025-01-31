import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        my_database = mysql.connector.connect(
            host='localhost',
            user="root",
            password="14051702"
        )

        cursor = my_database.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == "errorcode.ER_ACCESS_DENIED_ERROR":
            print("Error: Access denied. Check your username and password.")
        elif err.errno == "errorcode.ER_BAD_DB_ERROR":
            print("Error: Database does not exist.")
        else:
            print(err)

    else:
        cursor.close()
        my_database.close()

if __name__ == "__main__":
    create_database()

