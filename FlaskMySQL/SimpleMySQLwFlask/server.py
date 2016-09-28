from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app, 'py_semirestfulusers')

@app.route('/')
def hello_world():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	return render_template('index.html', all_users=users)

@app.route('/create', methods=['POST'])
def create_user():
	query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (:first_name,:last_name,NOW(),NOW())"
	data = {
		"first_name" : request.form["first_name"],
		"last_name" : request.form["last_name"]
	}
	mysql.query_db(query, data)
	return redirect("/")
app.run(debug=True)
