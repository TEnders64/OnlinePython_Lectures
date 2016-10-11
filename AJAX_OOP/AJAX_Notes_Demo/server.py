from flask import Flask, request, render_template, redirect, jsonify
from mysqlconnection import MySQLConnection
app = Flask(__name__)

mysql = MySQLConnection(app, 'py_notes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes/create', methods=["POST"])
def create():
    query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
    data = {
        "title": request.form['title']
    }
    mysql.query_db(query,data)
    return redirect('/notes')

@app.route('/notes')
def all_notes():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/<id>/destroy', methods=["POST"])
def destroy_note(id):
    query = "DELETE FROM notes WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/notes')

@app.route('/notes/<id>/update', methods=["POST"])
def update_note(id):
    query = "UPDATE notes SET description = :description WHERE id = :id"
    data = { "description": request.form['description'], "id": id}
    mysql.query_db(query, data)
    return jsonify({"status": True})


app.run(debug=True)
