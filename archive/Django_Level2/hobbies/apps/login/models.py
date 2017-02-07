from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
from django.utils import timezone

PASSWORD_REGEX = r'^.*\d+.*[A-Z]+.*$|^.*[A-Z]+.*\d+.*$'

# Create your models here.
class UserManager(models.Manager):
	def validate_registration(self, data):
		errors = []
		if  data['first_name']:
			if not len(data['first_name']) >= 2:
				errors.append('first name must be at least two characters!')
			if not data['first_name'].isalpha():
				errors.append('first name must contain only letters!')
		else:
			errors.append('first name must be filled!')

		if data['last_name']:
			if not len(data['last_name']) >= 2:
				errors.append('last name must be at least two characters!')
			if not data['last_name'].isalpha():
				errors.append('last name must contain only letters!')
		else:
			errors.append('last name must be filled!')

		if data['password']:
			if not len(data['password']) >= 8:
				errors.append('password must be at least 8 characters!')
			if not re.match(PASSWORD_REGEX, data['password']):
				errors.append('password gotta include number and upper case letter')
		else:
			errors.append('password must be filled out, be at least 8 characters, contain at least one numeral and one upper case letter!')

		if not data['confirm_password'] or data['password'] != data['confirm_password']:
			errors.append('password confirmation must exist and match exactly with password')

		if errors:
			return (False, errors)
		else:
			password = data['password'].encode()
			print type(password)
			hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
			user = User.objects.create(first_name=data['first_name'], last_name=data['last_name'], password=hashed_pw)
			return (True, user)

class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
