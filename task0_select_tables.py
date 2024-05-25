from getpass import getpass
from mysql.connector import connect, Error
from tabulate import tabulate
"""
python script to connect db and select users tables
"""


try:
    connection = connect(
        host="localhost",
        user="root",
        passwd=getpass(""),
        database='users',
    )

    mycursor = connection.cursor()

    query = "SELECT * FROM `users`"
    mycursor.execute(query)
    rows = mycursor.fetchall()

    headers = [i[0] for i in mycursor.description]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    mycursor.close()
    connection.close()

except Error as e:
    print(e)