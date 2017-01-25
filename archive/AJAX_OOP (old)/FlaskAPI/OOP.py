
class Computer(object):
	def __init__(self, ram="2", os="linux"):
		self.cpu = "i5"
		self.ram = ram
		self.hard_drive = "Seagate"
		self.os = os
		self.turned_on = False
		# print self.ram
		# print type(self.ram)

	def boot(self):
		self.turned_on = True
		print "powered on!"

	def run_program(self, program):
		if self.turned_on:
			print "running {}".format(program)

	def about(self):
		if self.turned_on:
			print "I'm running {} with {}gb of ram".format(self.os[0], self.ram[0])

class Laptop(Computer):
	def __init__(self, ram, os, weight):
		super(Laptop, self).__init__(ram)
		self.weight = weight

	def show_all(self):
		print "here are my attributes: {}, {}, {}, {}".format(self.weight, self.os, self.ram, self.hard_drive)

my_laptop = Laptop(8, "ubuntu", 2)
my_laptop.boot()
my_laptop.show_all()




# my_pc = Computer(16, "macOS")
# my_pc.boot()
# my_pc.run_program('Atom')
# my_pc.about()
