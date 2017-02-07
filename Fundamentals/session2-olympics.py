

#
#
# var my_number = 42;
# print my_number
#
#






#team 1 guessed error


















# my_list = [41, 23]
# my_second_list = [
# 	42,
# 	24
# ]
# print my_list[1] + my_second_list[2]


#team 1: undefined
#team 2: concatenate














# # It's better to ask for forgiveness than to ask for permission.
# my_list = [41, 23]
# my_second_list = [
#   	42,
#   	24
# ]
#
# try:
# 	print my_list[1] + my_second_list[2]
# except IndexError:
# 	print my_list[0] + my_second_list[1]

#1, 2: 65







# i,j = (1,2), [3,4]
# i[1] = 42
# j[0] = 42
# print i[1] + j[1]


#1: Error!
#2: 6




#
# num = 1,2,3
# print num
# #

#1: breaks
#2: "123"



# num1, num2, num3 = 1,3,5
# print (num2)

#1: 3
#2: 3


# num1, num2, num3 = num
# print(num1, num2, num3)

#1: 1 2 3
#2: (1,2,3) (1,2,3) (1,2,3)













# i,j = 1,2,3
# print j
# (i,j) = (1,2,3)
# print j

#1:
#2: ValueError: too many values to unpack









# our_list = ['Martin', 'Michael']
# for val in enumerate(our_list):
# 	print val


#1:
#1, Martin
#2, Michael

#2: Martin, Michael (or error)
#
# for idx,value in enumerate(our_list):
# 	print value, idx

#1: Martin, 1 // Michael, 2
#2: Martin, 1 // Michael, 2










name = {
	"sw":{'instrueector':"Sara Wong", 'boxer':'Sam Walton'},
	"mp":{'instructor':"Martin Puryear", 'boxer':"Manny Pacquiao"}
}
for key, val in name.items():
  if type(val) == dict:
	print val.get('instructor')


#1: :down arrow:
#2: sw 'Sara Wong' // mp 'Martin Puryear'












# for key value in name.items():
#   print key, value













#####################
#list comprehensions
#
# my_list = [1,9,3,42,9,99]
#
# for i in my_list:
# 	i += 20
#
# print my_list
#
#
#
# new_list = [i+20 for i in my_list]
# print new_list
#
#
# ice_cream_flavors = [
# 	{'chocolate': ['cocoa beans', 'honey', 'magical tastiness']},
# 	{'strawberry': ['strawberries', 'red food coloring', 'fresh cream']},
# 	{'rocky road': ['marshmallows', 'almonds', 'chocolate chips', 'chocolate']}
# ]
#
#
# def get_ingredients():
# 	for item in enumerate(ice_cream_flavors):
# 		# print flavor[1]
# 		for flavor, ingredients in item[1].items():
# 			# print flavor, ingredients
# 			for ingredient in ingredients:
# 				print ingredient
# 				if ingredient is "strawberries":
# 					break
# 				if ingredient is "marshmallows":
# 					print "YUM"
# 					return flavor
#
# print get_ingredients()
