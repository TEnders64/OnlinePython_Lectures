from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "keep_it_secret_keep_it_safe"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app, 'users')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    errors = False
    if len(request.form['name']) < 2:
        flash('Name must be at least 2 characters')
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email')
        errors = True
    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters')
        errors = True
    elif request.form['password'] != request.form['confirm']:
        flash('Passwords must match')
        errors = True
    if errors:
        return redirect('/')
    else:
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW())"
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        return redirect('/users')

@app.route('/login', methods=["POST"])
def login():
    errors = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email')
        errors = True
    if len(request.form['password']) < 1:
        flash('Password is required')
        errors = True
    if errors:
        return redirect('/')
    else:
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            'email': request.form['email']
        }
        user = mysql.query_db(query, data)
        if user and bcrypt.check_password_hash(user[0]['password'], request.form['password']):
            session['user_id'] = user[0]['id']
            return redirect('/users')
        else:
            flash('Email/Password combo not found')
            return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/users')
def all_users():
    query = "SELECT * FROM users"
    users_list = mysql.query_db(query)
    return render_template('users.html', users=users_list)

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

@app.route('/users/<id>')
def show(id):
    # form a query to get a user
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    # hit the db with it
    user = mysql.query_db(query, data)
    # render the SHOW template with user info
    return render_template('show.html', user=user[0])

@app.route('/users/<id>/delete')
def destroy(id):
    # form a query to delete a user
    query = "DELETE FROM users WHERE id = :id"
    data = {
        'id': id
    }
    # hit the db with it
    mysql.query_db(query, data)
    # redirect to index
    return redirect('/')

@app.route('/users/<id>/edit')
def edit(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id': id
    }
    user = mysql.query_db(query, data)

    return render_template('edit.html', user=user[0])

@app.route('/users/<id>', methods=["POST"])
def update(id):
    query = "UPDATE users SET name = :name, email = :email WHERE id = :id"
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'id': id
    }

    mysql.query_db(query, data)

    return redirect('/users/{}'.format(id))

app.run(debug=True)
