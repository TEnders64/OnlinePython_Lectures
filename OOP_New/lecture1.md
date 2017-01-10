#Python - OOP

####Key Assignment
- Animal (Tuesday)
- Django: Survey Form (Thursday)

Everything in OOP past Animal, and everything in Python Advanced Concepts, is Optional.

_Do not let yourself get behind by spending too long on the optionals!_

####What's OOP?
Object Oriented Programming
- An approach to avoid repeating ourselves and simplify debugging
- Considers things in terms of Classes and Instances
  - A Class is the ideal representation / blueprint for a thing, the Instance is the particular.
	- From one blueprint, we can create many individual instances!
  - How would we represent a person?
    - Attributes/Properties - e.g. a Name and Age
    - Actions/Methods/Functions - e.g. Walk, Talk, Make

```
class Person(object):
  def __init__(self):
    self.name = "Michael"
    self.age = 30
    self.energy = 100

  def walk(self):
    self.energy -= 1

  def talk(self):
    print "Hello there!"
```
  - Cool, but how do we create an <b>INSTANCE</b> of Person?
```
person1 = Person()
person1.talk()
```
  - Okay, but this isn't practical.  Everyone is named 'Michael'?!
```
class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.energy = 100

  def walk(self):
    self.energy -= 1

  def talk(self):
    print "Hello, I'm {}!".format(self.name)

person1 = Person('Michael', 30)
person1.talk()
```
  - That's DYNAMIC!  The <b>init</b> method lets us customize our attributes.
  - <b>TAKEAWAY:</b> Instead of writing copious amounts of code with the potential for repetition, let's create a CUSTOMIZABLE BLUEPRINT!

####Inheritance
- Our Person class looks a bit mundane doesn't it?
- What if we wanted a more specific type of Person?
  - Let's keep those goodies from the Person class but add some more things to another class.  A coder class!
```
class Coder(Person):
  def __init__(self, name, age, type_speed):
    super(Coder, self).__init__(name, age)
    self.type_speed = type_speed

  def code(self):
    print "I'm Coding Here!"
```
- We ingested a Person! Not really, but we can imagine that we've inherited all the properties and methods of the Person class inside the Coder class
```
coder1 = Coder('Michael', 30, '60wpm')
coder1.talk()
```
- What else can we get out of this Coder?  Person attributes and methods?
