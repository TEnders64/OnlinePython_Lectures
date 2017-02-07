from flask import Flask, render_template, request, redirect, session, flash
import datetime

app = Flask(__name__)

app.secret_key = "skjtAF3wi4l6b3l5SH7vw3ltvglMRweglkjbg"

users = []

@app.route('/')
def index():
	return render_template('index.html', users=users)

@app.route('/adopt', methods=['POST'])
def adopt():
	print request.form, "form data"
	if not request.form['first_name']:
		flash('first_name must be filled')
	user = {
		"first_name": request.form['first_name'],
		"last_name": request.form['last_name'],
		"breed": request.form['breed'],
		"date": datetime.datetime.now(),
	}
	users.append(user)
	print "this is my user",user
	return redirect('/')



app.run(debug=True)
