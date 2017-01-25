
class Human(object):
	def __init__(self, name):
		self.name = name

	def speak(self):
		print "My name is {}".format(self.name)
		return self



class Ninja(Human):
	def __init__(self, belts, account_name):
		super(Ninja, self).__init__(account_name)
		self.skills = 10
		self.stealth = 5
		self.throwing_stars = 3
		self.github_account = account_name
		self.belts = belts
		self.visible = True
		self.known_languages = []
		# for arg in args:
		# 	self.known_languages.append(arg)

	def disappear(self):
		self.stealth += 5

	def code(self, language):
		self.skills += 1
		if not language in self.known_languages:
			self.known_languages.append(language)
			print "You leveled up! Now you know {}".format(language)
		return self

	def ninja_speak(self):
		print 'I am a ninja'
		return self

	def show_languages(self):
		for language in self.known_languages:
			print language
		return self


ninja = Ninja(4, 'Doug')
# person2 = Human('Kellen')
ninja.speak().ninja_speak().code('Python').code('Javascript').show_languages()

ninja.skills = 200
ninja.pizza_budget = 60

print ninja.pizza_budget

print Ninja.skills
