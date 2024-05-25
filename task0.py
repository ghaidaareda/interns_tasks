from mysql.connector import connect, Error
from getpass import getpass
"""
python script to connect db creating users table
"""


try:
    connection = connect(
        host="localhost",
        user="root",
        passwd=getpass(""),
    )

    mycursor = connection.cursor()

    query_create_db = "CREATE DATABASE IF NOT EXISTS users;"

    query_create_tb = """
    CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    img_url VARCHAR(255),
    register_date DATE
    );"""

    mycursor.execute(query_create_db)
    mycursor.execute('USE users')
    mycursor.execute(query_create_tb)

    connection.commit()
    
    mycursor.close()
    connection.close()

except Error as e:
    print(e)
