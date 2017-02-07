def oddEven():
	for num in range(1,2000+1):
		if num % 3 == 0:
			print "The number {} is divisible by 3".format(num)
		elif num % 3 == 1:
			print "is one more th?"
		else:
			print "The number " + str(num) + " is odd"

# oddEven()


def iterates(list):
	for index in range(0, len(list), 2):
		#everything inside the loop
		#is indented to the same level
		print index, list[index]
	#things are outside the loop because they aren't indented anymore
	print list
	return list

myList = [1,3,2,9,4,8,3,20,6]
# iterates(myList)
#
# for (var index = 0; i < arr.length; i = i + 2) {
#
# }
