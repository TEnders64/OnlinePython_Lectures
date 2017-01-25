### Landscape for the week:
- Monday: OOP
- Tuesday: More OOP / What is MVC / Why Django?
- Wednesday: Django Installation code-along
- Thursday: Django basics: URL routing and templates
- Friday: Code Review of The Wall and the early Django assignments


# Installing Django

### Virtual Environment

Mac:
- navigate to Python/virtualenvs
- `virtualenv djangoEnv`
- `source djangoEnv/bin/activate`
- `pip install django`
- navigate to Python/django


Windows:


### Django
- django-admin startproject project_name
- mkdir apps
- touch apps/__init__.py
- cd apps
- python ../manage.py startapp app_name
- touch app_name/urls.py

### Setting up a server / learning the file structure
- M T V
- urls.py (inner project folder) (app level)
- settings.py (inner project folder)
