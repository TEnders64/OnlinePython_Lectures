# Python Fundamentals Session 1

#### Administrative
- Track access?
- Slack Communication
  - Slack Team: **Coding Dojo Online**
  - Slack Channel: **python-1**
  
#### What You're Going To Get

**Code Reviews**
  - Group code reviews on Fridays (and recorded) at 11am Pacific
    - **Check the Python I post in Slack**

**Python-1 consists of 4 weeks of Python then you'll join Python-2**

#### Expectations For You
- 25+ hours a week
- Read materials before class
- Don't wait until it's too late!

#### This Month's Outlook
- Week 1: Python Fundamentals
- Week 2: Flask
- Week 3: MySQL
- Week 4: Flask + MySQL (Wall Week)

#### Let's Look At This Week's Checklist

#### Let's Talk Python
- Python Shell
- Data Types
  - <b>Booleans</b>:  True/False
  - <b>Strings</b>: "hello, the world!"
  - <b>Ints, Floats</b>: 2, 2.5
  - <b>Lists</b>: [10, 'You', xyz, 50]
  - <b>Dictionaries</b>:  {'city': 'Sheboygan'}
  - <b>Tuples</b>:  (False, {'user': 'Felix'}) or (1,2,4)
  - <b>Strings</b>: "hello world"
- Indentation & Line Endings & Comments
- Loops
 - For
 - For-in
 - While


 - Predict how many times the following loop will run.
```python
  '''
  How many times will this run?
  '''
  for num in range(1,5): # The colon is necessary for loops, functions, conditionals
    print num
    return
```
  - If it helps, treat indentation like you did HTML
```html
  <div class="wrapper">
    <div class="comment">
      <h1>Hello World</h1>
      <p>How Are You?</p>
    </div> <!--end comment div -->
  </div> <!--end wrapper div -->
```
- Strings
  - print function
```python
  michael = "Sara"
  print "Hi my name is: ", michael
  # "Hi my name is: Sara"
```
  - format function
```python
  print "Hi my favorite color is: {}, no  {}".format("blue", "yellAAAAAHHH")
  # "Hi my favorite color is: blue, no yellAAAAAHHH"
```
- Lists
  - Like arrays in Javascript denoted by [ ]
```python
  teams = ['Mariners', 'Indians', 'Athletics']
  teams[1] # accesses 'Indians'
  teams[1] = 'Cardinals' # re-assigns bucket 1 to be 'Cardinals'
```
  - Built-in Methods
    - len(), pop(), append()
```python
  print len(teams) # 3
  teams.pop() # Whatever's last, in this case, 'Athletics' gets removed!
  print len(teams) # 2
  teams.append('Pirates') # teams is now ['Mariners', 'Cardinals', 'Pirates']
```
- Conditionals
  - if, else, elif
    - Example ```if 5 is not 1:```

- Loops
  - Fors, Whiles
    - Example ```for num in range(0,5):```
    - Example ```while 5 > 2:``` 
