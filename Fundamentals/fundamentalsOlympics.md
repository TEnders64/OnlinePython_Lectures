
Have students join teams and predict the following:

#1
```python
var my_number = 42;
print my_number
```
errors (no such thing as var!)

#2
```python
my_list = [41, 23]
my_second_list = [
  42,
  24
]
print my_list[1] + my_second_list[2]
```
error (index out of range)
#3
```python

# It's better to ask for forgiveness than to ask for permission.
my_list = [41, 23]
my_second_list = [
  42,
  24
]

try:
  print my_list[1] + my_second_list[2]
except IndexError:
  print my_list[0] + my_second_list[1]

```
65
#4
```python

i,j = (1,2), [3,4]
i[1] = 42
j[0] = 42
print i[1] + j[1]

```
error
#5
```python

num = 1,2,3
print num
num1, num2, num3 = 1,3,5
print (num2)

```
tuple, 3

#6
```python
i,j = 1,2,3
print j
(i,j) = (1,2,3)
print j
```
error
#7
```python
our_list = ['Martin', 'Michael']
for val in enumerate(our_list):
  print val

for idx,value in enumerate(our_list):
  print value, idx
```
tuples then idx and value elements

#8
```python
name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
for key, value in name:
  print key, value
```
s w, m p
#9
```python
name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
for key value in name.items():
  print key, value
```
(error)
