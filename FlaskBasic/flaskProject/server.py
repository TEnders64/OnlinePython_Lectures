from flask import Flask, render_template, request, redirect

app = Flask(__name__)

username = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/users', methods=["POST"])
def new_user():
    global username
    username = request.form['first_name']
    print username, '=================='
    return redirect('/show')

@app.route('/show')
def show():
    print username
    return render_template('show.html', user=username)

app.run(debug=True)
