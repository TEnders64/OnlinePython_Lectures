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

### Let's talk about Django / MVC!

First, think back to the Wall.

How big was your server.py file?

How big would it be if your site had ten or twenty pages instead of two?

This is exactly the problem Django, and many other web frameworks, seek to answer!


### Model, View, Controller
### Model, Template, View
