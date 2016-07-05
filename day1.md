#Python Fundamentals Day 1

####Administrative
- Track access?
- Yellow Belts
- Slack Communication

####What You're Going To Get
- Weekly Mentor Session ~ 20 mins
  - If you don't have burning questions, still keep your meeting.
- Weekly Code Review
  - If you have a specific assignment you want reviewed, mention it to your mentor.
- Daily Algorithms
  - We'll be using a hosted GitHub repo to pull our challenges from.  We'll post solutions the morning after.
- 8 weeks of Python instruction
  - 2x Lectures and 2x Office Hours a week
    - Prompt us for topics/demos to discuss in office hours
  - M/W Lecture 4pm T/Th Office Hours 3pm

####Expectations For You
- 20 hours a week
- Read materials before class
- Don't wait until it's too late!
- On-site Pace vs Online Pace

####This Month's Outlook
- Week 1: Python Fundamentals
- Week 2: OOP
- Week 3: MySQL
- Week 4: Flask

####Let's Look At This Week's Checklist

####Let's Talk Python
- Python Shell
- Data Types
  - <b>Booleans</b>:  True/False
  - <b>Numbers</b>: 2, 2.5
  - <b>Lists</b>: [10, 'You', xyz, 50]
  - <b>Dictionaries</b>:  {'city': 'Sheboygan'}
  - <b>Tuples</b>:  (False, {'user': 'Felix'})
  - <b>Strings</b>: "hello world"
- Indentation & Line Endings & Comments
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
  michael = "Todd"
  print "Hi my name is: ", michael
  # "Hi my name is: Todd"
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

####Demo Time: Odds And Evens
