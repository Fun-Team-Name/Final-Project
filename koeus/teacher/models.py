from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from teacher import utils
from django.shortcuts import get_object_or_404


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Please enter a valid email address.')

        if not kwargs.get('firstName'):
            raise ValueError('Please enter your first name.')

        if not kwargs.get('lastName'):
            raise ValueError('Please enter your last name.')

        account = self.model(
			email=self.normalize_email(email), firstName=kwargs.get('firstName'), lastName=kwargs.get('lastName')
        )

        account.set_password(password)
        account.save(using=self._db)

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save(using=self._db)

        return account

class Account(AbstractBaseUser):
	email = models.EmailField(primary_key=True, unique=True)
	firstName = models.CharField(max_length=40, default='')
	lastName = models.CharField(max_length=40, default='')

	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['firstName', 'lastName']

	def getClasses(self):
		return self.classroom.all()

	def __str__(self):
		return self.email

	def getName(self):
		return ' '.join([self.firstName, self.lastName])

	def getLastName(self):
		return self.lastName

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin

class Classroom(models.Model):
	teacher = models.ManyToManyField(Account)
	name = models.CharField(max_length=40, default='Classroom')
	key = models.CharField(max_length=200, default='Classroom', primary_key=True, unique=True)

	class Meta:
		ordering = ('name', 'key')

	@classmethod
	def create(cls, name, user):
		keyname= user.email + utils.utcNowTimestamp()
		classroom = cls(name=name, key=keyname)
		classroom.teacher.add(user)
		classroom.save()
		return classroom

	def rename(self, newname):
		self.name = newname
		self.save()
		return newname

	def __str__(self):
		return self.name

class Student(models.Model):
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
	firstName = models.CharField(max_length=40, default='')
	lastName = models.CharField(max_length=40, default='')
	studentNumber = models.CharField(max_length=20, default='12345')

	@classmethod
	def create(cls, classroom, firstName, lastName, studentNumber):
		student = cls(classroom=classroom, firstName=firstName, lastName=lastName, studentNumber=studentNumber)
		student.save()
		return student

	class Meta:
		ordering = ('lastName', 'firstName', 'studentNumber')

	def getName(self):
		return ' '.join([self.firstName, self.lastName])

	def getNameBackwards(self):
		return ', '.join([self.lastName, self.firstName])

	def __str__(self):
		return ','.join([self.firstName, self.lastName, self.studentNumber])
