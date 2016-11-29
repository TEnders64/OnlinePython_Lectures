from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.

class HobbyManager(models.Manager):
	def ValidateCreation(self, data):
		errors = []
		if not data['name']:
			errors.append('Hobby must be named')
		print data
		if not data['category']:
			errors.append('Category not chosen')
		if not data['danger_level']:
			errors.append('Danger level must be chosen')

		if not errors:
			hobby = Hobby.objects.create(name=data['name'], category=data['category'], danger_level=data['danger_level'])
			return hobby

class Hobby(models.Model):
	name = models.CharField(max_length=200)
	person = models.ManyToManyField(User)
	category = models.CharField(max_length=200)
	danger_level = models.IntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = HobbyManager()
