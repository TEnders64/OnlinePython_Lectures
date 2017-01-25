#Python - Django!
####Key Assignments
- Ninja Gold (Monday)
- Email Validation (Wednesday)
- Login and Registration (Friday before Code Review!)

### Django Models

- The *M* in MVC
- Models help us represent grouped data, similar to the tables in MySQL
- We can constrain data types in the same way MySQL did
- We can validate the data
  - *REMEMBER: Skinny Controllers, Fat Models*

####Field Types

- IntegerField, CharField, DateField, ForeignKey, etc.
- Very similar to MySQL's `INT`, `VARCHAR()`, `DATETIME`, etc.
- Note: We don't have to state the *id* field anymore
```
class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
```

####The Object Relational Mapper (ORM)

- Every model we create comes with its own ORM that helps us manage that specific model (table)
- By default an instance of ORM is created for _each_ model and we refer to it as `objects`
  - For example: `User.objects.all()` tells the User model's ORM (*objects*) to fetch all records from the Users table

####Validations

- Validations are nothing new
  - We can approach them the same way we did in Flask
- Again, thinking fat models, let's place the responsibility of validations on the Models.py file, but on a *custom manager*

####Custom Managers

```
class UserManager (models.Manager):
      def login(self, **kwargs):
        #...

      def register(self, **kwargs):
        #...

class User (models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()
```
- We've updated the User model to create an instance of UserManager.
- The UserManager class houses our heavier logic and will be our new ORM that replaces the older version of `objects`

### Group Assignment (Sports_ORM)
- Download the Sports_ORM assignment
- Test your queries by modifying the existing queries inside the context dictionary in the index method
- Copy/paste the working queries into the three .md files below the questions
- Prosper!


##### Look through the documentation!

[Jack's ORM assignment](https://github.com/madjaqk/sports_orm)


#### Tips
- Start with whatever you want your output to be
- Filter to limit the bounds
- Step through relationships using __ then access their attributes like normal
	```
	Player.objects.filter(curr_team__league__name="American Conference of Amateur Football")
	```
