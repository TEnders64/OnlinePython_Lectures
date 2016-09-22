from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def register(self, **kwargs):
        errors = False
        if not errors:
            User.objects.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], password=kwargs['password'])
        return True

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Language(models.Model):
    language = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    # language.objects.get(id=1).users()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
