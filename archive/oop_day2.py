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
