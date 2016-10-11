from flask import Flask, request, render_template, redirect, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'world') #make sure the db name matches your world database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countries')
def countries():
    countries = mysql.query_db("SELECT * FROM countries")
    return render_template('country_rows.html',countries=countries)

app.run(debug=True)
