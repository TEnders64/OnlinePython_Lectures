from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "keepitsecret_keepitsafe"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    if not 'submissions' in session:
        session['submissions'] = 1
    else:
        session['submissions'] += 1
    if len(request.form['username']) > 4:
        long_name = True
    else:
        long_name = False

    return render_template('results.html', username=request.form['username'], password=request.form['password'], long_name=long_name)

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
