from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)

#set up session
app.secret_key = "keepitsecret_keepitsafe"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    print request.form # let's see what it looks like!
    if not 'counter' in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('results.html', name=request.form['name'], email=request.form['email'], rating=request.form['rating'])

@app.route('/dojos')
def dojos():
    return redirect('/')

app.run(debug=True)
