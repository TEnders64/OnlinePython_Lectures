#Python - Django!
####Key Assignments
- Ninja Gold (Monday)
- Email Validation (Wednesday)
- Login and Registration (Friday before Code Review!)

#### Models Recap
- Models provide the structure to our database.
- (models are like the skeleton to which the data are attached)
- When we makemigrations we are doing the equivalent of saving our ERD.
- When we migrate we are doing the equivalent of forward engineering. This is the point at which our database is actually created.
- We create custom managers to hold our validations and extend the basic Objects manager.
- All of this is using OOP!

### Group Assignment (Sports_ORM)
- Download the Sports_ORM assignment
- Test your queries by modifying the existing queries inside the context dictionary in the index method
- Copy/paste the working queries into the three .md files below the questions
- Prosper!

##### Look through the documentation!

### Example (walk through first few)
Level 1
1. Find all baseball _leagues_
2. Find all womens' _leagues_

Level 2
1. Find all _teams_ in the Atlantic Soccer Conference

#### Tips
- Start with whatever you want your output to be
- Filter to limit the bounds
- Step through relationships using __ then access their attributes like normal
	```
	Player.objects.filter(curr_team__league__name="American Conference of Amateur Football")
	```
