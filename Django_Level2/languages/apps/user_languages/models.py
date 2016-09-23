from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def register(self, **kwargs):
        errors = False
        error_list = []
        if len(kwargs['first_name']) is 0:
            error_list.append("First name is required")
            errors = True
        if not kwargs['first_name'].isalpha():
            error_list.append("First name can only contain letters")
            errors = True
        if not kwargs['last_name'].isalpha():
            error_list.append("Last name is required and must contain only letters")

        if not errors:
            user = User.objects.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], password=kwargs['password'])
            print user.id
            return (True, user.id)
        else:
            return (False, error_list)


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
