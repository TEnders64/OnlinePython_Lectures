from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager (models.Manager):
      def login(self, **kwargs):
          user = User.objects.get(email=kwargs['email'])
          if user[0]:

              return (True, user[0])
          else:
              return (False, "Email/Password not found")

      def register(self, **kwargs):
          return (False, errors_list)

class User (models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      email = models.EmailField()
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()
