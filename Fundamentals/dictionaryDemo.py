# myDictionary = {
#   'name': 'Todd',
#   'location': 'Warshington'
# }
#
# for xyz in myDictionary:
#   print myDictionary[xyz] #Are we printing keys or values?
#
# myList = ['Tony','Collin','Dhurata']
#
# for idx in range(0, len(myList)):
#     print myList[idx]
#
# def createUser(name="Todd"):
#     print name
#
# createUser("Collin")

myTuple = ('Me', 'You', 'We')
#Looping
# for val in myTuple:
#   print val

#Accessing
# print myTuple[2]

#Unpacking: Use a Tuple to unpack a Tuple
(x, y, z) = myTuple

# print x, y, z
a = 1
b = 2
c = 3

# (a,b) = (b,a)
#
# forward = [1,2,3,4]
# for idx in range(0, len(forward)/2):
#     (forward[idx], forward[len(forward)-1-idx]) = (forward[len(forward)-1-idx], forward[idx])
# print forward

name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
for key, value in name.items():
  print key, value
