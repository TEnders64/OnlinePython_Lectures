from flask import Flask, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, "world")


@app.route('/')
def index():
	results = mysql.query_db('SELECT name, continent FROM countries LIMIT 50')
	return render_template('index.html', results=results)

app.run(debug=True)
