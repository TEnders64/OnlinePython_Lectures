cat = {}
cat['name'] = "Oscar"
cat['legs'] = 4
cat['fur'] = True
cat['color'] = "Black"
cat['food'] = "All the wildlife"

class Mammal(object):
	def __init__(self):
		self.breathes = True
		self.fur = True
		self.limbs = 4
		self.hp = 50

	def walk(self, w=1):
		if w != 1:
			print '\nmoving in a walking motion' * w
		else:
			print 'moving in a walking motion' * w
		return self

	def health(self):
		print self.hp

class Cat(Mammal):
	def __init__(self):
		super(Cat, self).__init__()
		# self.name = name
		# self.color = color
		self.food = "All the wildlife"
		self.toes = 5
		self.hp = 30

	def meow(self):
		print 'meow'
		return self

class Bat(Mammal):
	def __init__(self):
		super(Bat, self).__init__()
		self.color = "Black"
		self.food = "Mosquitoes"
		self.wings = True
		self.hp = 15
		self.stealth = 90
		self.speed = 65

	def swoop(self):
		print 'swooping'
		return self

class SuperCat(Cat, Bat):
	def __init__(self):
		super(SuperCat, self).__init__()
		self.x = 20
		self.y = 60
		self.can_climb_banana_trees = True
		self.toes = 6
		self.hp = 160

	def moveUp(self):
		self.y -= 1;
		return self

	def leap(self):
		print "I am flying through the trees!"
		return self

	def meow(self):
		print 'ROAR'
		return self

ernie = Cat()
print ernie.health()

bart = SuperCat()
bart.name = "Bart"
bart.walk(7).swoop().leap().meow().health()

bat = Bat()
