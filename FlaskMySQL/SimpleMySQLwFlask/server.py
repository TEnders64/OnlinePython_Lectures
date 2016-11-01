from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# PASSWORD_REGEX = re.compile(r'^[a-z]+[A-Z]+')
mysql = MySQLConnector(app, 'py_semirestfulusers')

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	errors = False
	if len(request.form['email']) is 0:
		errors = True
		flash('Email must be present')
	elif not EMAIL_REGEX.match(request.form['email']):
		errors = True
		flash("Invalid email address")
	if len(request.form['password']) < 8:
		errors = True
		flash("Email/Password combination not found")
	if errors:
		return redirect('/')

	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = {
		'email': request.form['email']
	}
	user = mysql.query_db(query, data)
	if user[0]:
		if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
			session['user_id'] = user[0]['id']
			return redirect('/users')

	flash('Email/Password combo not found')
	return redirect('/')

@app.route('/register', methods=['POST'])
def register():
	errors = False
	if len(request.form['first_name']) is 0:
		errors = True
		flash("First Name can't be blank")
	if not request.form['first_name'].isalpha():
		errors = True
		flash("First Name can only contain letters")
	if len(request.form['last_name']) is 0:
		errors = True
		flash("last Name can't be blank")
	if not request.form['last_name'].isalpha():
		errors = True
		flash("last Name can only contain letters")
	if not EMAIL_REGEX.match(request.form['email']):
		errors = True
		flash("Invalid email address")
	if not len(request.form['password'])>= 8:
		errors = True
		flash("Length must be at least 8 characters")
	if not request.form['password'] == request.form['c_password']:
		errors = True
		flash("Password doesn't match!")
	if errors:
		return redirect("/")

	query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first, :last, :email, :password)"
	data = {
		"first": request.form['first_name'],
		"last": request.form['last_name'],
		"email": lower(request.form['email']),
		"password": bcrypt.generate_password_hash(request.form['password'])
	}
	user_id = mysql.query_db(query, data)
	session['user_id'] = user_id

	return redirect("/users")

@app.route('/users')
def show_all():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	return render_template('index.html', all_users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users', methods=['POST'])
def create():
	query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (:first_name,:last_name,NOW(),NOW())"
	data = {
		"first_name" : request.form["first_name"],
		"last_name" : request.form["last_name"]
	}
	mysql.query_db(query, data)
	return redirect("/")

@app.route('/users/<id>')
def show(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id' : id
    }
    user = mysql.query_db(query, data)
    return render_template('show.html', this_user = user[0])

@app.route('/users/<id>/edit')
def edit(id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {
        'id' : id
    }
    user = mysql.query_db(query, data)
    return render_template('edit.html', this_user = user[0])

app.run(debug=True)
