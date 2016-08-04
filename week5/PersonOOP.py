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

class Coder(Person):
  def __init__(self, name, age, type_speed):
    super(Coder, self).__init__(name, age)
    self.type_speed = type_speed

  def code(self):
    print "I'm Coding Here!"

coder1 = Coder('Michael', 30, '60wpm')
coder1.talk()
