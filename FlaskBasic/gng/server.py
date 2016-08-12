from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if not session.get('number'):
        session['number'] = random.randrange(1, 101)

    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():

    if session['number'] > int(request.form['user_guess']):
        #too low
        session['result'] = "Too Low"
    elif session['number'] < int(request.form['user_guess']):
        #too high
        session['result'] = "Too High"
    else:
        #right on
        session['result'] = "That was correct, {} was the number!".format(session['number'])
        session['correct'] = True

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
