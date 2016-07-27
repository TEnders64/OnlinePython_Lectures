from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
import bcrypt

mysql = MySQLConnector(app, 'world')

@app.route('/')
def reroute():
    return redirect('/countries')

@app.route('/countries')
def index():
    result = mysql.query_db("SELECT * FROM countries ORDER BY population DESC")
    return render_template('index.html', result=result)

@app.route('/countries/new')
def new():
    return render_template('new.html')

@app.route('/countries', methods=["POST"])
def create():
    query = "INSERT INTO countries (name, population, region) VALUES (:name, :population, :region)"
    data = {
        'name': request.form['name'],
        'population': request.form['population'],
        'region': request.form['region']
    }
    country_id = mysql.query_db(query, data)
    # print '/countries/'+str(country_id)
    return redirect('/countries/'+str(country_id))

@app.route('/countries/<country_id>')
def show(country_id):
    result = mysql.query_db("SELECT * FROM countries WHERE id = {}".format(country_id))
    # [{'name':'Legoland', 'population':500000}]
    return render_template('show.html', country=result[0])

app.run(debug=True)
