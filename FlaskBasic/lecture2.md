#Python - Flask Week Part 2

####What Did We Learn Yesterday?
- Virtual Environments
  - Sandboxes where we can pile up every tool we need for the job.  We can reuse these in multiple projects!
- Request/Response cycle
- Where Flask lives (server-side)
- What Flask can provide so far...
  - Handling different requests to different routes via different methods: GET & POST
  - Delivering templates (render_template)

####What We Are Going To Cover Today
- More Jinja2 templating
- Session vs Cookie
- Hidden Inputs

####Jinja2 Is Our Engine, You Are The Driver
- Embedded Python and passing data into our 'views' (templates)
```html
<html>
  <body>
    <h1>Hi There, {{username}}!</h1>
  </body>
</html>
```
- There's a boat load of things we can do with Jinja
  - Dig into the documentation (link on platform in 'Flask Templates')
  - Print with ```{{ }}```
  - Execute statements ```{% %}```
    - Control structures like a For loop
    - Conditionals like ```if, elif, else```

```html
<html>
  <body>
    {% for num in range(0,2) %}
    <h1>Hi There, {{username}}!</h1>
    {% endfor %}
  </body>
</html>
```  
  - This is all great, but how do we get username over to the template?
    - Back inside our server.py file...
```python
#...
@app.route('/form_results')
def form_results():
  return render_template('results.html', username=request.form['username'])
```

####Session vs Cookie vs Flash
- Session is server-side, cookies are on your browser
  - We can identify someone in Flask using the cookie file we store on their browser
  - Session can be used to stash information temporarily until that user logs out or we set a timer
  - Session storage is sparse!
- Flash Data lives for only one request/response cycle as opposed to session!

####Hidden Inputs
- Hidden inputs allow us to pack more information into a form without the user knowing it
  - When would this be useful?  
    1. What if there are multiple forms on a page?  Which one got submitted?
    2. Identifying who's logged in and trying to create comments (think: Facebook)

```html
<form action="/new_comment" method="post">
  <input type="hidden" name="current_user" value="{{session['user_id']}}">
  <input type="hidden" name="current_message" value="{{session['message_id']}}">
  <textarea name="comment"></textarea>
  <input type="submit" value="Add Comment">
</form>
```
