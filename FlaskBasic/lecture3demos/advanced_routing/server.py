from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<user_id>')
def show(user_id):
    return render_template('show.html', id=user_id)

app.run(debug=True)
