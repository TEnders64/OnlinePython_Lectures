#Python Fundamentals Lecture 2

####Key Assignments This Week
- <b>Scores & Grades, Names</b>
![alt text](NamesAssignment.png "DICTIONARIES!!!")

####Less Talk More Loops
- Let's see how a for loop works again.
```python
for num in range(0,5):
  print num

myDictionary = {
  'name': 'Todd',
  'location': 'Warshington'
}
for key in myDictionary:
  print key #Are we printing keys or values?
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

#Unpacking: Use an equal-lengthed Tuple to unpack a Tuple
(x, y, z) = myTuple

print x, y, z
```
####Q&A

####Group Activity: Get Your Python Chops
1. Build a function that takes in a list of numbers and a value.  Multiply each number in the list by the value given and return the updated list.
2. Build a function that takes in a dictionary.  Print the key and value of each key-value pair like so: 
```
Your dictionary has the following inside:
key1 : value1
key2 : value2
key3 : value3
...
```
3. Create a function that will examine the range of numbers from 1 to 100.  If a number is divisible by 3, print "fizz", if a number is divisible by 5, print "buzz", if a number is divisible by 3 and 5, print "fizzbuzz"