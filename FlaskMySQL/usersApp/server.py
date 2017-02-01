from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "keep_it_secret_keep_it_safe"

mysql = MySQLConnector(app, 'users')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users_list = mysql.query_db(query)
    return render_template('index.html', users=users_list)

@app.route('/users', methods=['POST'])
def create():
    # let's hang onto the two inputs from the form
    name = request.form['name']
    email = request.form['email']
    # write query first (insert)
    query = "INSERT INTO users (name, email, created_at, updated_at) VALUES (:name, :email, NOW(), NOW())"
    data = {
        'name': name,
        'email': email
    }
    # call the database (mysql)
    user_id = mysql.query_db(query, data)
    print user_id
    # redirect out
    return redirect('/')

app.run(debug=True)
