from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Please enter a valid email address.')

        if not kwargs.get('firstName'):
            raise ValueError('Please enter your first name.')

        if not kwargs.get('lastName'):
            raise ValueError('Please enter your last name.')

        account = self.model(
			email=self.normalize_email(email), firstName=kwargs.get('firstName'), lastName=kwargs.get('lastName'), teacher=kwargs.get('teacher')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Classroom(models.Model):
	id = models.CharField(primary_key=True, max_length=300, unique=True)
'''
class Student(models.Model):
	id = models.CharField(primary_key=True, max_length=100, unique=True)
'''

class Account(AbstractBaseUser):
	classroom = models.ManyToManyField(Classroom)
	email = models.EmailField(primary_key=True, unique=True)
	district = models.CharField(max_length=100)
	school = models.CharField(max_length=100)
	firstName = models.CharField(max_length=40, default='first')
	lastName = models.CharField(max_length=40, default='last')

	is_admin = models.BooleanField(default=False)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['firstName', 'lastName', 'teacher']

	def __unicode__(self):
		return self.email

	def getName(self):
		return ' '.join([self.first_name, self.last_name])

	def getLastName(self):
		return self.last_name




'''
student number for password
'''
