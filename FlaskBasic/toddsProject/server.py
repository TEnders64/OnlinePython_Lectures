from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!" #for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=["POST"])
def create():
    errors = False
    if len(request.form['username']) < 2:
        flash("Username must be at least 2 characters")
        errors = True
    if len(request.form['email']) == 0:
        flash("Email is required")
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    if errors:
        return redirect('/')
    else:
        # session['username'] = request.form['username']
        # session['email'] = request.form['email']
        return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html', users=[{'username':'tenders','email':'todd@todd.com'}, {'username':'marbogast', 'email':'michael@michael.com'}])

@app.route('/users/<some_user>')
def show(some_user):
    return render_template('show.html', this_user=some_user)

app.run(debug=True)
