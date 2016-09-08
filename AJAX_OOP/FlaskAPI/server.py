from flask import Flask, request, render_template, redirect, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'world')

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
