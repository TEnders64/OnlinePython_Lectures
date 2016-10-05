ourList = [1,2,3,4,5,6,7,8]

def swapFirstAndLast(aList):
	for num in range(0, (len(aList)/2)):
		aList[num], aList[-num -1] = aList[-num -1], aList[num]
	return aList

print swapFirstAndLast(ourList)
