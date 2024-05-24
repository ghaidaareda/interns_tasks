from flask import Flask, render_template, jsonify, request, redirect, url_for
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
    return jsonify(users)

@app.route('/get_user <fname>', methods=['GET'])
def get_user(fname):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE fname = %s' , (fname,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if user:
        return jsonify(user)
    else:
        return 'user not found', 404
    
@app.route('/add_user')
def add_user():
    return render_template('index1.html')

@app.route('/add_user', methods=['POST'])
def create_user():
    fname = request.form['fname']
    lname = request.form['lname']
    id = request.form['id']
    img_url = request.form['img_url']
    register_date = request.form['register_date']
    if not fname or not lname or not id or not img_url or not register_date:
        return jsonify({"error": "Invalid or missing data"}), 400
    connection = get_db_connection()
    if connection is None:
        return "Database connection failed", 500
    cursor = connection.cursor()
    cursor.execute ('''INSERT INTO users 
                    (fname, lname, id, img_url, register_date)
                    VALUES (%s, %s,%s,%s,%s)'''
                    , (fname, lname, id, img_url, register_date))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


