#Flask Recap Day
####Pieces of server.py
- imports & setup:
```python
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "keepitsecret_keepitsafe"
```
- routing:
  - server.py is listening for the routes **we** specify
  - this is only **one part** of the bridge
```python
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
  #....
```
- request object:
  - Looking at the /process route specifically...
```python
@app.route('/process', methods=["POST"])
def process():
  print request.form # debug!!! let's see what it looks like!
  return render_template('results.html', name=request.form['name'], email=request.form['email'], rating=request.form['rating'])
```
- session:
  - just a persistent dictionary per user that visits our site
  - Make sure to import it and use `secret_key`
```python
@app.route('/process', methods=["POST"])
def process():
  print request.form # let's see what it looks like!
  if not 'counter' in session:
     session['counter'] += 1
  else:
     session['counter'] = 1
  return render_template('results.html', name=request.form['name'], email=request.form['email'], rating=request.form['rating'])
```
####Pieces of Templates
- forms:
  - For sending information to a route in `server.py`
  - this is the **other piece** of the bridge!
  - Form actions must match a route in server.py
```html
<!DOCTYPE html>
<!-- index.html -->
<html>
  <head>
    <meta charset="utf-8">
    <title>Index Page</title>
  </head>
  <body>
    <h1>Submit a Survey</h1>
    <form action="/process" method="post"> <!-- this will hit the /process route in server.py via POST -->
      <p>Your Name: <input type="text" name="name"></p>
      <p>Your Email: <input type="text" name="email"></p>
      <p>Satisfaction Rating:
        <select name="rating">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
      </p>
      <p><input type="submit" value="Submit"></p>
    </form>
  </body>
</html>
```
- embedded Python:
  - For evaluating variables or doing loops or using logic to show/hide HTML content, etc.
```html
<!DOCTYPE html>
<!-- results.html -->
<html>
  <head>
    <meta charset="utf-8">
    <title>Result Page</title>
  </head>
  <body>
    <h1>You've submitted this form {{session['counter']}} time(s)!</h1>
    <p>Here are your results:</p>
    <p>Name: {{name}}</p>
    <p>Email: {{email}}</p>
    <p>Rating: {{rating}}</p>
    {% if session['counter'] > 2 %}
    <h3>You must love submitting surveys</h3>
    {% endif %}
  </body>
</html>
```
- links:
  - for navigating to another route that maybe loads another page.
```html
<!DOCTYPE html>
<!-- results.html -->
<html>
  <head>
    <meta charset="utf-8">
    <title>Result Page</title>
  </head>
  <body>
    <h1>You've submitted this form {{session['counter']}} time(s)!</h1>
    <p>Here are your results:</p>
    <p>Name: {{name}}</p>
    <p>Email: {{email}}</p>
    <p>Rating: {{rating}}</p>
    {% if session['counter'] > 2 %}
    <h3>You must love submitting surveys</h3>
    {% endif %}
    <a href="/">Go Back</a> <!-- this will hit '/' via GET in server.py, thus taking us back to the index template -->
  </body>
</html>
```
