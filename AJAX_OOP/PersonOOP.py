class Person(object):
  def __init__(self, name, age, hobby):
    self.name = name
    self.age = age
	self.hobby = hobby
    self.stamina = 100

  def walk(self):
    self.stamina -= 1

  def talk(self):
    print "Hi, I'm {} and I like {}!".format(self.name, self.hobby)

person1 = Person("Michael", 200)
print person1.talk()
#
# class Coder(Person):
#   def __init__(self, name, age, type_speed):
#     super(Coder, self).__init__(name, age)
#     self.type_speed = type_speed
#
#   def code(self):
#     print "I'm Coding Here!"
#
# coder1 = Coder('Todd', 32, '1000wpm')
