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
    print countries
    return jsonify(countries)

@app.route('/countries/<id>/destroy')
def destroy(id):
    query = "DELETE FROM countries WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    country = mysql.query_db("SELECT * FROM countries WHERE id = "+id)
    if country:
        return jsonify({'status': False})
    else:
        return jsonify({'status': True})

app.run(debug=True)
