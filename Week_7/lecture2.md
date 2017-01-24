#Python - Django!
####Key Assignments
- Login and Registration (Monday)
- Multiple Apps: Ninja Gold with Leaderboard (Tuesday)
- Belt Reviewer (Thursday)
- Belt Reviewer Deployed (Friday)

### Multiple Apps
- It’s a lot of work to design, build, test and maintain a web application. Many Python and Django projects share common problems. Wouldn’t it be great if we could save some of this repeated work?
[Documentation: reusable apps](https://docs.djangoproject.com/en/1.10/intro/reusable-apps/)
- We can easily reuse our apps when we make each app _do one thing_ and do it well.
- [Django design philosophies](https://docs.djangoproject.com/en/1.10/misc/design-philosophies/)

### Named Routes & Namespacing
- We need to change things in four places:
 - project urls
 - app urls
 - views
 - templates

- Doing this allows us to easily interact with pages from other apps in our project!

Let's go to the [Documentation](https://docs.djangoproject.com/en/1.10/topics/http/urls/)

Project level urls.py:

```python
from django.conf.urls import include, url

urlpatterns = [
    url(r'^login_reg/', include('login_reg.urls', namespace='login_reg')),
    url(r'^ninja_gold/', include('ninja_gold.urls', namespace='ninja_gold')),
]
```
App level urls.py:

```python
from django.conf.urls import url

from . import views

app_name = 'login_reg'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    ...
]
```

Login_reg/views.py:

```python
def register(request):
	#logic
	if errors:
		#flash errors
		return redirect('login_reg:index')
	else:
		#save user's id to session['id']
		return redirect('ninja_gold:index')
```

From any template:

```python
{% url 'ninja_gold:process' %}
```
