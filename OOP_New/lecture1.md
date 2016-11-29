#Python - OOP
####Key Assignment
- Animal

####What's OOP?
- Object Oriented Programming
  - Let's build objects that help us represent real-life objects! Crazy? Not really!
    - How would we represent a person?
      - Attributes/Properties - e.g. a Name and Age
      - Actions/Methods/Functions - e.g. Walk, Talk, Make
    - We can toss these into a class to help us represent something over and over!
```
class Person(object):
  def __init__(self):
    self.name = "Todd"
    self.age = 32
    self.stamina = 100

  def walk(self):
    self.stamina -= 1

  def talk(self):
    print "Todd habla espanol un poco"
```
  - Cool, but how do we create an <b>INSTANCE</b> of Person?
```
person1 = Person()
person1.talk()
```
  - Okay, but this isn't practical.  Everyone is named 'Todd'?!
```
class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.stamina = 100

  def walk(self):
    self.stamina -= 1

  def talk(self):
    print "{} habla espanol un poco".format(self.name)

person1 = Person('Michael', 30)
person1.talk()
```
  - That's DYNAMIC!  The <b>constructor</b> method let's us customize a bit more.
  - <b>TAKEAWAY:</b> Instead of writing copious amounts of code with the potential for repetition, let's create a BLUEPRINT!

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
