#Python - Django Level 2
####Key Assignments
- Login/Reg
- Multiple Apps

####Django Models
- The <b>M</b> in MVC
- Models help us represent grouped data, similar to the tables in MySQL
- We can constrain data types in the same way MySQL did
- We can validate the data
  - <b>REMEMBER: Skinny Controllers, Fat Models</b>

####Field Types
- IntegerField, CharField, DateField, ForeignKey, etc.
- Very similar to MySQL's `INT`, `VARCHAR()`, `DATETIME`, etc.
- Note: We don't have to state the <b>id</b> field anymore
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
- By default an instance of ORM is created for <i>each</i> model and we refer to it as `objects`
  - For example: `User.objects.all()` tells the User model's ORM (<b>objects</b>) to fetch all records from the Users table

####Validations
- Validations are nothing new
  - We can approach them the same way we did in Flask
- Again, thinking fat models, let's place the responsibility of validations on the Models.py file, but on a <b>custom manager</b>

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
      userMgr = UserManager()
```
- We've updated the User model to create an instance of UserManager.
- The UserManager class houses our heavier logic and will be our new ORM that replaces `objects`
