from flask import Flask, render_template, request, redirect, session, flash
from something import hello

app = Flask(__name__)

app.secret_key = "kj32bk6b2kjhtb235khvt32jk"

@app.route('/')
def index():
	names = ["Gerold", "Richard", "Bill", "FD", "Alfonso"]
	style = {"class": "red"}
	users = {
		'Students': [
			{'first_name':  'Michael', 'last_name' : 'Jordan', 'instructor': 1},
			{'first_name' : 'John', 'last_name' : 'Rosales', 'instructor': 1},
			{'first_name' : 'Mark', 'last_name' : 'Guillen', 'instructor': 0},
			{'first_name' : 'KB', 'last_name' : 'Tonel', 'instructor': 0}
		],
		'Instructors': [
			{'first_name' : 'Michael', 'last_name' : 'Choi'},
			{'first_name' : 'Martin', 'last_name' : 'Puryear'}
		]

	}
	hello()
	return render_template('index.html', names=names, style=style, users=users)

@app.route('/submit', methods=['POST'])
def submit():
	print request.form
	errors = []
	if len(request.form['first_name']) < 2:
		errors.append(('Hey, fill out the first name field!', 'first_name'))
	if len(request.form['last_name']) < 2:
		errors.append(('Hey, fill out the last name field!', 'last_name'))
	print errors
	if errors:
		for error in errors:
			flash(error[0], error[1])
	else:
		#we have no errors
		session['username'] = request.form['first_name'].lower() +  request.form['last_name'].lower()
		return redirect('/')

	return redirect('/')

@app.route('/user/<username>')
def user_page(username):
	print username
	session['awesome'] = username
	return redirect('/')



app.run(debug=True)
