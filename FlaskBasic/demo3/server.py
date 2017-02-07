from flask import Flask, render_template, redirect, request, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "asjbk23tk.gbwiu3t,whjvlsa,ashkvasljhvflkhjvas.agblakg"

users = []

@app.route('/')
def index():
	print "users--->", users
	return render_template('index.html', users=users)

@app.route('/adopt', methods=['POST'])
def adopt():
	#all our validations and logic
	errors = []
	print "this is our request ---->", request.form, type(request.form)
	if not request.form['first_name']:
		errors.append('you need to enter a first name!')
	if not len(request.form['first_name']) > 2:
		errors.append('your name is too short')
	if not request.form['last_name']:
		errors.append('you need to enter a last name!')
	if not request.form['email']:
		errors.append('you need to enter an email!')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')

	user = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'breed': request.form['breed'],
		'date': datetime.now()
	}

	users.append(user)
	return redirect('/')

app.run(debug=True)
