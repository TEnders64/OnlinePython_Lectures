#Python Fundamentals Lecture 1

####Administrative
- Track access?
- Slack Communication
  - Slack Channel: **Python-1**

####What You're Going To Get
- Responsive Help from your classmates and those who are ahead, plus Instructors & TAs
- Could come in the form of a Text response, Hangout, Screenhero or Zoom
- There are 3 **MUSTS** we ask you provide before reaching out for help...
 1. Put your code in a GitHub **repository**, **gist** or Slack **snippet**
 2. Articulate what **you think** the problem is
 3. List what you’ve already tried to solve the problem

- **Code Reviews**
  - This month & following, will occur through GitHub
  - Key Assignments will be code reviewed
    - **WEEK 1** Scores & Grades, Names
    - **WEEK 2** Ninja Gold, Registration Form (Flask)
    - **WEEK 3** Sakila
    - **WEEK 4** The Wall
    - **WEEK 5** Ajax Notes
    - **WEEK 6** Ninja Gold, Disappearing Ninjas (Django)
    - **WEEK 7** Belt Reviewer
    - **WEEK 8** Black Belt Week! No Code Reviews
  - Push your assignments to GitHub repos and send the link to your repo to me on Slack in a DM.  I can code review and submit pull requests to you!

- **Algorithms**
  - The Algorithms Slack Channel is where all things Algorithms will take place.  
  - You should all have your Algorithm books by now, anyone not?
  - We are doing daily Algorithm sessions, M-F @ 1pm
- **8 weeks of Python instruction**
  - 4 sessions a week
    - Prompt us for topics/demos to discuss in more depth
  - Schedule: After today, M/W 5pm, T/Th 3pm (Pacific)
  - We commence **October 31 (today)**

####Expectations For You
- 20 - 25+ hours a week
- Read materials before class
- Keep up with the assignments
- Post CORE ASSIGNMENTS to the Github Org
- Don't wait until it's too late!

####This Month's Outlook
- Week 1: Python Fundamentals
- Week 2: Flask
- Week 3: MySQL
- Week 4: Flask + MySQL (Wall Week)

####Let's Look At This Week's Checklist

####Let's Talk Python
- Python Shell
- Data Types
  - <b>Booleans</b>:  True/False
  - <b>Ints, Floats</b>: 2, 2.5
  - <b>Lists</b>: [10, 'You', xyz, 50]
  - <b>Dictionaries</b>:  {'city': 'Minneapolis'}
  - <b>Tuples</b>:  (False, "Heroes", 200)
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

####Demo Time: Odds And Evens
