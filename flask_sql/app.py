from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'user': 'root',
    'password': 'ghaidaa88',
    'host': 'localhost',
    'database': 'users'
}

# Establish a connection to the database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', users=users)

@app.route('/user/<fname>')
def get_user():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE name = %s' , (fname,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if user:
        return render_template('index1.html', user=user)
    else:
        return 'user not found', 404 
if __name__ == '__main__':
    app.run(debug=True)


