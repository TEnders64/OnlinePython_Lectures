


my_bool = True

my_int = 7

my_list = [
	'thing1',
	8,
	False,
	[2,3],
	{'hello': "world"}
]

my_dict = {
	"name": "Michael",
	"birth_month": 5,
	"birth_day": 20.7,
	"newly_added_key": "hello",
}





# var my_number = 42
# print my_number












# my_list = [41, 23]
# my_second_list = [
#   42,
#   24
# ]
# print my_list[1] + my_second_list[2]

#
#
# try:
# 	print my_list[1] + my_second_list[2]
# except:
# 	print my_list[0] + my_second_list[1]
# finally:
# 	print "nah this is great"


# i,j = (1,2), [3,4]
# i[1] = 42
# j[0] = 42
# print i[1] + j[1]


# num = 1,2,3
# print num


#
# num1, num2, num3 = 1,3,5
# print (num2)

#
# i, j = 1, 2, 3
# print j

#
# (i,j) = (1,2,3)
# print j


#
# our_list = ['Martin', 'Michael']
#
# for val in enumerate(our_list):
#   print val


# for idx, value in enumerate(our_list):
#   print idx, value

#
#
# name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
#
# for key, value in name:
#   print key, value


name = {"sw":"Sara Wong", "mpn ":"Martin Puryear"}
for thing in name.iteritems():
  print thing[1], "<-wow"

for thing in name.itervalues():
	print thing
