def multiplyList(some_list, value):
	for idx in range(len(some_list)):
		some_list[idx] *= value
	return some_list

def printDictionary(some_dict):
	for key in some_dict:
		print key, ":", some_dict[key]

