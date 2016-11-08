class Vertebrate(object):
	def __init__(self):
		self.has_backbone = True

class Mammal(Vertebrate):
	def __init__(self):
		super(Mammal, self).__init__()
		print "here in mammal"
		self.number_of_legs = 4
		self.hp = 5
		self.regulates_interal_body_temp = True
		self.has_fur = True
	def breathe(self):
		print "respiring"

class Cat(Mammal):
	def __init__(self, name):
		super(Cat, self).__init__()
		self.name = name
		self.hp = 20
		self.well_being = 100
		self.hunger = 0

	def meow(self):
		print "miao"
	def sleep(self):
		if self.hp < 20:
			self.hp += 5
		print "zzzz", self.hp
	def walk(self):
		self.hp -= 3
	def chase_bird(self):
		self.hp -= 12
		print "chased a bird, hp are", self.hp


squirrel = Cat("confused")
print squirrel.hp, squirrel.number_of_legs
