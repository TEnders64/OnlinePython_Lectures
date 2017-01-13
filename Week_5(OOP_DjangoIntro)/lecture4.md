### Landscape for the week:
- Monday: OOP
- Tuesday: More OOP / What is MVC / Why Django?
- Wednesday: Django Installation code-along
- Thursday: Django basics: URL routing and templates
- Friday: Code Review of The Wall and the early Django assignments


### Django routing

Regular Expressions

- basic characters
- boundaries `^ $ \b`
- word characters `\w`
- digits `\d`
- whitespace `\s`
- character sets `[]`
- repeats `? + *`
- groups `()`
- named groups `(?P<name>[])`


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
