### Landscape for the week:
- Monday: OOP
- Tuesday: More OOP / What is MVC / Why Django?
- Wednesday: Django Installation code-along
- Thursday: Django basics: URL routing and templates
- Friday: Code Review of The Wall and the early Django assignments


### Django routing

Regular Expressions

- Basic Syntax
- Ordinary characters
- Escaping: "\"
- Anything: "."
- Start: "^"
- End: "$"
- Word characters: "\w", "\W"
- Digit characters: "\d"
- Boundaries and spaces: "\b", "\s"
- Groups: "[a-zA-Z0-9]"
- Repetitions: "\*", "+", "?"
- Capture groups: "()"
- Naming them: "(?P<name>)"

####Further reading
- [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
- [regexr.com](https://regexr.com)
- [pythex.org](https://pythex.org)


### Django templates

Django uses a templating engine that is VERY similar to Jinja2.

When in doubt, read the docs:
https://docs.djangoproject.com/en/1.10/topics/templates/
https://docs.djangoproject.com/en/1.10/ref/templates/builtins/

- context dictionary

- variables `{{ username }}`
	- dot notation `{{ my_dict.first_name }}`
	- even for lists `{{ my_list.2 }}`

- tags

```python
	{% if name == "Ted" %}
		<h1> Hey ol' Teddy ol' boy! </h1>
	{% else %}
		<h1> Hey {{ name }}! </h1>
	{% endif %}

	{% for key, val in data.items %}
		<p> {{ key }}: {{ val }} </p>
	{% empty %}
		<p> This dictionary has nothing in it </p>
	{% endfor %}
```
- comments `{# single line comment #}`

```
{% comment "optional note" %}
	other stuff to be commented out
{% endcomment %}
```

- static files

```python
{% load staticfiles %}
<link rel="stylesheet" href="{% static 'app_name/css/style.css' %}">

```
- requires the following folder structure:

```
project_name/ (outer)
	apps/
		app_name/
			migrations/
			static/
				app_name/
					css/
						style.css
			templates/
				app_name/
					index.html			
	project_name/ (inner)
		settings.py
		urls.py
		etc
	manage.py
```


### Forms
- With forms, we're still treating them the same way we did in Flask.  We either have POST information or GET information, but the difference in Django is that we get to use the `request` dictionary again to check for different methods.
  - Need to check out what's inside a POST? `request.POST` has it.
  - Need to check out what's inside a GET? `request.GET` has it.
  - `request` is a one-stop shop
- <b>Notable difference in forms themselves...</b>
  - We need a <b>CSRF</b> token.  This is an added layer of security for our forms.  If the CSRF token is unrecognized, then Django won't accept it.
```
<form action="/users" method="post">
  {% csrf_token %}
  Name: <input type="text" name="name" />
  <input type="submit" value="Submit" />
</form>
```
