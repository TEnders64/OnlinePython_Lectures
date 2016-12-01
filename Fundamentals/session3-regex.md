#Python Fundamentals Session 3

####Key Assignment This Week
- <b>Names</b>
![alt text](NamesAssignment.png "DICTIONARIES!!!")

####Less Talk More Loops
- Let's see how a for loop works again.
```python

index = 0
while index < 5:
	print index * index

for num in range(0,5):
  	print num * num

for num in range(5):
	print num**2

output = [a**2 for a in range(5)]

for key in myDictionary:
  print key #Are we printing keys or values?
  print myDictionary[key]

for key, val in myDictionary.iteritems():
	  print key, val
```
####Functions, Dictionaries, Tuples
- Functions
  - What are they good for?
    - DRY principle
    - Example

- Dictionaries
  - What are they good for?
    - Key-Value pair indexing
    - What order are they in?

- Tuples
  - What are they good for?
    - Immutable Sequence
    - Keep their order (hence sequence)
    - Swaps are easier
```python
myTuple = ('Me', 'You', 'We')
#Looping
for val in myTuple:
  print val

#Accessing
print myTuple[2]

#Unpacking: Use a Tuple to unpack a Tuple
(x, y, z) = myTuple

print x, y, z
```

####Our Friend the Regular Expression
- Basic Syntax
- Ordinary characters
- Escaping: "\"
- Anything: "."
- Start: "^"
- End: "$"
- Word characters: "\w", "\W"
- Digit characters: "\d"
- Boundaries and spaces: "\b", "\s"
- Groups: "[a-zA-Z0-9]"
- Repetitions: "*", "+", "?"
- Capture groups: "()"
- Naming them: "(?P<name>)"

#### Practice
- /users/238
- /users/michael/description
- cat in "thehandbagwrenchcatmegaphonecatastrophe"
- words starting with a capital letter
- words that end with "ly"
- words that sound like "ough"
- http://regex.alf.nu/
