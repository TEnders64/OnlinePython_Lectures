from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
import bcrypt

mysql = MySQLConnector(app, 'world')

@app.route('/')
def index():
    result = mysql.query_db("SELECT * FROM countries ORDER BY population DESC LIMIT 10")
    return render_template('index.html', result=result)

app.run(debug=True)
