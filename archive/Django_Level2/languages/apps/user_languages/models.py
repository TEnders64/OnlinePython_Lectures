from __future__ import unicode_literals
from django.db import models
import bcrypt, re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def register(self, **kwargs):
		# print kwargs['password'], len(kwargs['password']), " wwww"*50
		error_list = []
		if len(kwargs['first_name']) is 0:
			error_list.append("First name is required")
		if not kwargs['first_name'].isalpha():
			error_list.append("First name is required and can contain only letters")
		if not kwargs['last_name'].isalpha():
			error_list.append("Last name is required and must contain only letters")
		if not kwargs['email']:
			error_list.append('Email is required')
		if not email_regex.match(kwargs['email']):
			error_list.append('Email must be valid!')
		if len(kwargs['password']) < 8:
			error_list.append('Password must be at least 8 characters in length')
		if not kwargs['password'] == kwargs['c_password']:
			error_list.append('Password and confirmation must match')

		if len(error_list) is 0:
			pw_hash = bcrypt.hashpw(kwargs['password'].encode(), bcrypt.gensalt())
			print pw_hash, kwargs['password'], "~"*20
			user = self.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], email=kwargs['email'], password=pw_hash)
			print user.id
			return (True, user.id)
		else:
			print error_list
			return (False, error_list)

	def login(self, **kwargs):
		error_list = []
		try:
			print "in try block"
			user = User.objects.get(email=kwargs['email'])
			print user
			input_pw = kwargs['password'].encode()
			hashed_pw = user.password.encode()
			print input_pw, hashed_pw
			if bcrypt.hashpw(input_pw, hashed_pw) == hashed_pw:
				print "heyyyy"
				return (True, user)
			print "if check failed"
			return (False, error_list)
		except:
			error_list.append("No user with matching username and password")
		# if not len(error_list):
		# 	return (True, user)
		# else:
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
