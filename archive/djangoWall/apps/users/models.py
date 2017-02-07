from __future__ import unicode_literals

from django.db import models
from ..users.models import Message, Comment


# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
