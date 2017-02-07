from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "kjbwetl523,jhc4ukw3l3qktgiuwgkbskjdbggwl4jhf8qy3igabkjbsjf"

mysql = MySQLConnector(app, 'world')




@app.route('/', methods=['GET'])
def index():
	countries = mysql.query_db('SELECT * FROM countries WHERE continent = "South America"')
	print type(countries), countries
	#will come back as a list of dictionaries
	return render_template('index.html', countries=countries)

@app.route('/create', methods=['POST'])
def create():
	print request.form
	data = {
		'name' : request.form['name'],
		'continent' : request.form['continent'],
		'head_of_state' : request.form['head_of_state'],
	}
	query = 'INSERT INTO countries (name, continent, head_of_state) VALUES (:name, :continent, :head_of_state)'
	country_id = mysql.query_db(query, data)
	print country_id
	return redirect('/')

@app.route('/countries/<id>/edit')
def edit(id):
	data = {'id': id}
	country = mysql.query_db('SELECT * FROM countries WHERE id=:id', data)
	return render_template('edit.html', country=country[0])

@app.route('/countries/<id>/update', methods=['POST'])
def update(id):

	data = {
		'name' : request.form['name'],
		'continent' : request.form['continent'],
		'head_of_state' : request.form['head_of_state'],
		'id': id
	}
	query = "UPDATE countries SET name=:name, continent=:continent, head_of_state=:head_of_state WHERE id=:id"
	print query, data
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/countries/<id>/delete')
def delete(id):
	data = {'id': id}
	country = mysql.query_db('DELETE FROM countries WHERE id=:id', data)
	return redirect('/')

@app.route('/login', methods=['POST'])
def	login():
	errors = False
	fname = request.post['first_name']
	if not fname:
		flash('error! You need to enter a first name, buster!')
		errors = True
	elif len(fname) < 2:
		flash('name too short')
		errors = True

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else: #no errors
		data = {
			'first_name': fname,
		}
		mysql.query_db(query, data)

app.run(debug=True)
