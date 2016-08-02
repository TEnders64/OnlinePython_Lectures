from flask import Flask, render_template, redirect, request, flash, session, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
import bcrypt

mysql = MySQLConnector(app, 'world')

@app.route('/')
def reroute():
    # return redirect('/countries')
    return render_template('index.html')
@app.route('/countries')
def index():
    result = mysql.query_db("SELECT * FROM countries ORDER BY population DESC")
    # return render_template('index.html', result=result)
    print result
    return jsonify(result)

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

@app.route('/countries/<country_id>/edit')
def edit(country_id):
    query = "SELECT * FROM countries WHERE id = :id"
    data = {
        'id': country_id
    }
    country = mysql.query_db(query, data) # [{}]
    return render_template('edit.html', country=country[0])

@app.route('/countries/<country_id>', methods=["POST"])
def update(country_id):
    query = "UPDATE countries SET name = :name, region = :region, population = :population WHERE id = :id"
    data = {
        'name': request.form['name'],
        'region': request.form['region'],
        'population': request.form['population'],
        'id': country_id
    }
    mysql.query_db(query, data)
    return redirect('/countries')

@app.route('/countries/<country_id>/delete', methods=["POST"])
def destroy(country_id):
    query = "DELETE FROM countries WHERE id = :country_id LIMIT 1"
    data = {
        'country_id': country_id
    }
    mysql.query_db(query, data)
    return redirect('/countries')

app.run(debug=True)
