# More OOP / Intro to MVC

### Landscape for the rest of the week:
- Tuesday (that's today!): More OOP / What is MVC / Why Django?
- Wednesday: Django Installation code-along
- Thursday: Django basics: URL routing and templates
- Friday: Code Review of The Wall and the early Django assignments

### We've learned the syntax for Python's OOP

- We can create Classes
	- which can inherit from other Classes

- We can give our classes Attributes (properties) and Methods (actions)

- We can create particular instances of our class

- We can use `self` to reference the particular instance of the class and manipulate it

- We can `return this` to allow us to chain methods together

### Questions about this before we move on?

### Multiple Inheritance

```
class Vertebrate(object):
	def __init__(self):
		self.has_backbone = True

class Bird(Vertebrate):
	def __init__(self):
		super(Bird, self).__init__()
		self.feathers = True
		self.warm_blooded = True
		self.lays_eggs = True

class Lizard(Vertebrate):
	def __init__(self):
		super(Lizard, self).__init__()
		self.warm_blooded = False
		self.lays_eggs = True
		self.has_scales = True

class Dinosaur(Bird, Lizard):
	def __init__(self):
		super(Dinosaur, self).__init__()
		self.feathers = False

dino = Dinosaur()
print dino.has_scales 		#True
print dino.lays_eggs 			#True
print dino.feathers 			#False
print dino.warm_blooded 	#True <-- because it inherits from the left-most class if the attribute exists in multiple parent classes!~
print dino.has_backbone		#True

```


####The MVC (Django MTV) Concept
- Until now, we've only dealt with Flask.  What if the application gets massive?  
- How big was your server.py file in The Wall? What if instead of 2 pages you had 20?
- How do we manage all those routes and keep everything straight?
- Enter Model, View, Controller (MVC)
  - Separation of Concerns
    * Avoid chaos
    * Know where to go
    * Split out the logic in appropriate places
    * Future Maintainability
    * Reusable code


####Routing
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

####Controllers (Views)
- Think of controllers (views) as the traffic cop.
- When certain routes were matched in Flask, the following methods was executed
  - Now that our apps could get potentially large, we're going to want to split out our methods from our routes
- The flow: <b>Controller methods get executed based on the routes file</b>
  - Controllers could then call up on Models to do some database work for them.
    - We really don't want controllers doing a lot of the leg work.  We just want them to delegate tasks.

####Models (Models)
- Models are the place where we're going to house the database interaction/logic portions of our code
- The flow: <b>Models could be called into action by controllers to fetch DB info and pass it back to the controller</b>
- These model files could be big and bulky at times which is good!
  - We want controllers to be skinny and models to be dense

####Views (Templates)
- Client-facing HTML/CSS etc.
  - Nothing new here, we're still building out templates the way we would have before, but they are referred to as views in the MVC sense.  Templates in Django.
  - We still throw data into the template just as we always have.
- The flow: <b>Views (templates) are rendered by the controller and shown to the client</b>
