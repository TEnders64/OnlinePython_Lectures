my_list = [1,9,3,42,9,99]

for i in my_list:
	i += 20

# print my_list



new_list = [i+20 for i in my_list]
print new_list


ice_cream_flavors = [
	{'chocolate': ['cocoa beans', 'honey', 'magical tastiness']},
	{'strawberry': ['strawberries', 'red food coloring', 'fresh cream']},
	{'rocky road': ['marshmallows', 'almonds', 'chocolate chips', 'chocolate']}
]


def get_ingredients():
	for item in enumerate(ice_cream_flavors):
		# print flavor[1]
		for flavor, ingredients in item[1].items():
			# print flavor, ingredients
			for ingredient in ingredients:
				print ingredient
				if ingredient is "strawberries":
					break
				if ingredient is "marshmallows":
					print "YUM"
					return flavor

print get_ingredients()
