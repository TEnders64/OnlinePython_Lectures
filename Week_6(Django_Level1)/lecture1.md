# Python - Django!
#### Key Assignments
- Ninja Gold (Monday)
- Email Validation (Wednesday)
- Login and Registration (Friday before Code Review!)

### MTV / MVC Recap

#### Routing
- In flask, we might have a had a route set up like this:
```python
@app.route('/users')
def show_users():
  #run some SQL
  return render_template('users.html', users=users)
```
  - As we add more and more routes to our app, we're going to see the utility of creating a file dedicated to handling various routes.
  - The flow: <b>Routes get hit first and potentially matched and fire off corresponding controller (Django view) methods</b>
  - But what about the methods those routes used to invoke?

#### Controllers (Views)
- Think of controllers (views) as the traffic cop.
- When certain routes were matched in Flask, the following methods was executed
  - Now that our apps could get potentially large, we're going to want to split out our methods from our routes
- The flow: <b>Controller methods get executed based on the routes file</b>
  - Controllers could then call up on Models to do some database work for them.
    - We really don't want controllers doing a lot of the leg work.  We just want them to delegate tasks.

#### Models (Models)
- Models are the place where we're going to house the database interaction/logic portions of our code
- The flow: <b>Models could be called into action by controllers to fetch DB info and pass it back to the controller</b>
- These model files could be big and bulky at times which is good!
  - We want controllers to be skinny and models to be dense

####Views (Templates)
- Client-facing HTML/CSS etc.
  - Nothing new here, we're still building out templates the way we would have before, but they are referred to as views in the MVC sense.  Templates in Django.
  - We still throw data into the template just as we always have.
- The flow: <b>Views (templates) are rendered by the controller and shown to the client</b>

#### How did you solve the problem of passing data back and forth with Disappearing Ninjas and Ninja Gold?


#### Session
- Session still does the same thing it always does regardless of what stack we're in.  
  - Hangs onto small amounts of data that we want to preserve for a current user, etc.
- How do we activate or gain access to session?
```
>python manage.py makemigrations
>python manage.py migrate
```
- Let's look at a `views.py` file and see where session lives.
  - In the `request` dictionary!
- We can update and check the session dictionary in a similar fashion as before, but now we just state it as `request.session['key']`
- But in our templates, we should only use dot notation `request.session.username`


#### Demoing Session
