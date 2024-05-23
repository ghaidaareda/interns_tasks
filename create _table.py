import mysql.connector
import getpass

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

sql_query_add_data = """
INSERT INTO users (fname, lname, img_url, register_date)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '2022-04-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2010-01-01'),
    ('Bob', 'Johnson', 'bob.johnson@example.com', '2023-05-22');
"""

# Execute SQL query to create database
mycursor.execute(sql_query_create_db)

# Execute SQL query to use database
mycursor.execute("USE users")

# Execute SQL query to create table
mycursor.execute(sql_query_create_table)

# add example data
mycursor.execute(sql_query_add_data)


# Commit the changes
mydb.commit()

# Close the cursor and connection
mycursor.close()
