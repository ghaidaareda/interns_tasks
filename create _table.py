import mysql.connector

"""
python script to connect to database
& create table with certain columns
"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ghaidaa88",
)
mycursor = mydb.cursor()
sql_query_create_db = "CREATE DATABASE IF NOT EXISTS users;"

sql_query_create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    img_url VARCHAR(255),
    register_date DATE
);"""
# Execute SQL query to create database
mycursor.execute(sql_query_create_db)

# Execute SQL query to use database
mycursor.execute("USE users")

# Execute SQL query to create table
mycursor.execute(sql_query_create_table)
# Commit the changes
mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()
