#Python - Django Level 2
####Key Assignments
- Login/Reg
- Multiple Apps

####Before we begin
- We don't have access to the request object in our Models
 - Messaging happens from views

####Demo Multiple Apps
- Namespace and named routes
 - outer urls.py:
 ```
 include('apps.friend_app.urls', namespace='friend_app')
 ```
 - app-level urls.py:
```
app_name = 'friend_app'
urlpatterns=[
	url(r'^$', views.index, name='index')
]
```
- Named Routes
 - Easy to set up
 - We can do great things!
  - In our HTML:
	 ```
	<form action="{% url 'friend_app:process' %}" method="post">
	  {% csrf_token %}
		...
		...
	</form>

	{% for user in users %}
	  <a href="{% url 'friend_app:show' user.id %}">
	    {{ user.first_name }} {{ user.last_name }}
	  </a>
	{% endfor %}
	 ```

- Many to Many Relationships

 - `models.ManyToManyField(User)`
 - QuerySets work identically
 
