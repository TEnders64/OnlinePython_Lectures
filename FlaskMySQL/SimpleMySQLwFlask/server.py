from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, 'py_semirestfulusers')

@app.route('/')
def index():
	return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
	errors = False
	if len(request.form['first_name']) is 0:
		errors = True
		flash("First Name can't be blank")
	if errors:
		return redirect("/")
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
