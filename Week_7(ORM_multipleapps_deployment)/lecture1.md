#Python - Django!
####Key Assignments
- Login and Registration (Monday)
- Multiple Apps (Tuesday)
- Belt Reviewer (Thursday)
- Belt Reviewer Deployed (Friday)

### Login and Registration
- In views, you want to call a function you build into your Model's CustomManager class:

```python
response = User.objects.register(request.POST)
```

- In the Model, you want to override the default objects with your custom manager

```python
class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager() # <---- this!!!
```
- Name your custom manager "Name_of_class"Manager

e.g.:
```python
class UserManager(models.Manager):
	def register(self, data):
		print data
		errors = []
		...logic...
```		
- A clever way to easily tell your views whether you encountered errors or success is to _return_ a tuple or list, the zeroth index of which is a boolean, like so:

```python
#inside register
if errors:
	# return a tuple
	return (False, errors)

else:
	# do your logic to create a new password hash
	...logic...
	user = self.create(
		first_name=first_name,
		last_name=last_name,
		password=pw_hash
	)
	return (True, user)
```
