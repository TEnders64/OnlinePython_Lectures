from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/users', methods=["POST"])
def new_user():
    errors = False
    if len(request.form['first_name']) is 0:
        flash('First Name is required')
        errors = True
    if len(request.form['last_name']) is 0:
        flash('Last Name is required')
        errors = True
    if errors:
        return redirect('/create')
    else:
        session['fullname'] = request.form['first_name'] + ' ' + request.form['last_name']
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/users/<user_id>') # /users/1  => user_id = 1
def show_user(user_id):
    print user_id # whatever <user_id> happens to look like in the route
    return render_template('show_user.html', some_id = user_id)

app.run(debug=True)
