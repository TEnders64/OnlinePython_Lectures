#Python - Flask Week

####Where Are We?
- We've learned Python
  - Those fundamentals are going to come in handy!
- Now where?
  - Let's build some stuff!

####This Week's Key Assignments
- Ninja Gold
- Registration

####The Flask Mini-Framework
- HTTP Request/Response Cycle
  - What's that look like again?
- Where does Flask come in?
  - Flask is going to be able to cover us from front to back and even handle DB communication (in a couple weeks)
    - We can catch incoming HTTP requests!
    - We can handle <form> data & validate it!
    - We can then do some logic and render pages (templates) with embedded Python in there!
    - We could redirect users elsewhere!

#####GET & POST requests
- GET requests
  - Links and redirects
- POST requests
  - Forms package up information for us in an envelope and deliver it on a 'wire'
  - ```<form action="/users" method="post">``` Here our 'wire' is the route ```/users```

#####Templates
Client-side views  
  - Client-side meaning HTML we are going to deliver to the user
  - Jinja2 templating is built into Flask when we install it.
  - All we have to do is set up a templates folder in our project!

#####More on Templating
Jinja2 Is Our Engine, We Are The Driver
- Embedded Python and passing data into our 'views' (aka templates)
```html
<!-- in project_folder/templates/index.html -->
<html>
  <body>
    <h1>Hi There, please fill in your name!</h1>
    <form action="/form_results" method="post">
      <input type="text" name="persons_name">
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```
There's a boat load of things we can do with Jinja
  - Dig into the documentation (link on platform in 'Flask Templates')
  - Print with ```{{ }}```
  - Execute statements ```{% %}```
    - Control structures like a For loop
    - Conditionals like ```if, elif, else```

```html
<!-- in project_folder/templates/results.html -->
<html>
  <body>
    {% for num in range(0,2) %}
    <h1>Hi There, {{name}}!</h1>
    {% endfor %}
  </body>
</html>
```  
This is all great, but how do we get `name` over to the template?  And what is `name`?
  - Back inside our server.py file...
```python
#... project_name/server.py
@app.route('/form_results', methods=['POST'])
def form_results():
  return render_template('results.html', name=request.form['persons_name'])
```

####Let's Get Flasking with a Group Activity
1. Set up a project/folder called <b>My_First_Flask</b>.  
2. Create a folder inside it called <b>templates</b>.
3. Create a new file called <b>server.py</b> in the <b>My_First_Flask</b> directory (not the templates).  
4. Set up your server.py to listen for <b>GET</b> request to '/' and in response, render a template called <b>index.html</b> that has a form on it.
  - The form should only have one input and ask the user for their email address. Don't forget your submit input.
5. Make this form <b>POST</b> to the route '/process'
6. Simply ```print request.form``` in your <b>server.py</b> file when the route '/process' gets matched (i.e. when someone submits the form from index.html)
#####Bonus Round
7. Go ahead and create a <b>results.html</b> file in your templates folder and have the following:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Results Page</title>
</head>
<body>
  {% for i in range(0,2) %}
  <h1>{{email_address}}</h1>
  {% endfor %}
</body>
</html>
```
8. Instead of just printing request.form after the form is submitted, render the <b>results.html</b> file and populate the email_address.  HINT: to pass information into a template, you can say something like...
```python
return render_template('some_template.html', variable_name=some_value)
```
