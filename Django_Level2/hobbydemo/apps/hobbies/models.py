from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HobbyManager(models.Manager):
    def validate(self, **kwargs):
        errors = []
        if len(kwargs['name']) < 1:
            errors.append('Hobby name is required')
        elif len(kwargs['name']) < 3:
            errors.append('Hobby name must be at least 3 characters')
        if len(kwargs['description']) < 1:
            errors.append('Description is required')
        elif len(kwargs['description']) < 5:
            errors.append('Description must be at least 5 characters')
        if len(errors) > 0:
            return (False, errors)
        else:
            h = Hobby.hobbyMgr.create(name=kwargs['name'], description=kwargs['description'])
            return (True, h)

class Hobby(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    hobbyMgr = HobbyManager()
