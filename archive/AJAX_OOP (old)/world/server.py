from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "WAHIGHWJRBgousebtvkj2hqvkb326j3vucqawhmtx2qjg34x7um4crky2q3v6n4fue65xjrsd46wjh2c3"
bcrypt = Bcrypt(app)
# app.url_map.strict_slashes = False

mysql = MySQLConnector(app, "world")


@app.route('/')
def go_to_world():
	return redirect('/countries')
#
# @app.route('/users')
# def user_index():
# 	return render_template('user_index.html')
#
# @app.route('/users', methods=['POST'])
# def user_create():
# 	errors = []
# 	if not request.form['first_name']:
# 		print "no first name"
# 		errors.append('first name must be filled out')
# 	elif not request.form['first_name'].isalpha():
# 		print "not alpha first name"
# 		errors.append('first name must contain only letters')
# 	if not request.form['last_name']:
# 		print "no last name"
# 		errors.append('last name must be filled out')
# 	elif not request.form['last_name'].isalpha():
# 		print ""
# 		errors.append('last name must contain only letters')
# 	if not request.form['password']:
# 		errors.append('password must be filled out')
# 	elif not re.match(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}', request.form['password']):
# 		errors.append('password must be at least 8 characters long and contain a number and a capital letter')
#
# 	print errors
# 	if errors:
# 		for error in errors:
# 			flash(error)
# 		session['replacement_form_info'] = {
# 			'first_name'
# 		}
# 		return redirect('/users')
# 	else: #if no errors
# 		hashed_pw = bcrypt.generate_password_hash(request.form['password'])
# 		print hashed_pw, request.form['password']
# 		new_user = {
# 			'first_name': request.form['first_name'],
# 			'last_name': request.form['last_name'],
# 			'pw_hash': hashed_pw
# 		}
# 		insert_query = "INSERT INTO users (first_name, last_name, pw_hash) VALUES (:first_name, :last_name, :pw_hash)"
# 		return redirect('/countries')
#
# @app.route('/users/login', methods=['POST'])
# def user_login():
# 	errors = []
# 	if not request.form['first_name']:
# 		errors.append('first name must be filled out')
# 	elif not request.form['first_name'].isalpha():
# 		errors.append('first name must contain only letters')
# 	if not request.form['last_name']:
# 		errors.append('last name must be filled out')
# 	elif not request.form['last_name'].isalpha():
# 		errors.append('last name must contain only letters')
# 	if not request.form['password']:
# 		errors.append('password must be filled out')
# 	elif not len(request.form['password']) > 8:
# 		errors.append('password too short')
# 	if errors:
# 		for error in errors:
# 			flash(error)
# 	else:
# 		user = "SELECT * FROM users WHERE username = {}".format(request.form['username'])
# 		if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
# 			session['id'] = user[0]['id']
# 			return redirect('/countries')
# 		else:
# 			flash('user with that username/password combination not found in database')
# 			return redirect('/users')

@app.route('/countries', methods=['POST'])
def create():
	create_data = {
	'name': request.form['name'],
	'region': request.form['region'],
	'population': request.form['population'],
	'capital': request.form['capital'],
	'gnp': request.form['gnp']
	}
	create_query = "INSERT INTO countries (name, region, gnp, capital, population) VALUES (:name, :region, :gnp, :capital, :population)"
	row = mysql.query_db(create_query, create_data)
	return redirect('/render_partial')

@app.route('/countries') #method == GET
def index():
	# results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id ORDER BY countries.population DESC LIMIT 10')
	# print results, type(results)
	return render_template('index.html')


@app.route('/countries/new')
def new():
	return render_template('edit.html', results=False)

@app.route('/render_partial')
def partial():
	results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id ORDER BY countries.population DESC LIMIT 10')
	return render_template('partials/partial.html', results=results)

@app.route('/countries/<id>')
def show(id):
	print id, type(id)
	results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id WHERE countries.id = {}'.format(id))
	language_query = "SELECT * FROM languages WHERE country_id = :country_id"
	language_data = {
		'country_id': id,
	}
	languages = mysql.query_db(language_query, language_data)
	return render_template('show.html', results=results[0], languages=languages)


@app.route('/countries/<id>', methods=['POST'])
def update(id):
	print id
	print "in route \n\n\n", request.form
	insert_data = {
	'name': request.form['name'],
	'gnp': request.form['gnp'],
	'region': request.form['region'],
	'population': request.form['population'],
	'id': request.form['hidden'],
	'capital': request.form['capital']
	}
	print insert_data
	insert_query = "UPDATE countries SET name = :name, gnp = :gnp, region = :region, population = :population WHERE id = :id"
	mysql.query_db(insert_query, insert_data)
	return redirect('/render_partial')

@app.route('/countries/<id>/edit')
def edit(id):
	results = mysql.query_db('SELECT countries.id, countries.name, region, cities.population, gnp, cities.name AS country_capital FROM countries JOIN cities ON countries.capital = cities.id WHERE countries.id = {}'.format(id))
	return render_template('edit.html', results=results[0])

@app.route('/countries/<id>/delete')
def destroy(id):
	mysql.query_db('DELETE FROM countries WHERE id = {}'.format(id))
	return redirect('/render_partial')


app.run(debug=True)
