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

class Classroom(models.Model):
	name = models.CharField(max_length=40, default='Classroom')

	class Meta:
		ordering = ('name',)

	@classmethod
	def create(cls, name):
		classroom = cls(name=name)
		classroom.save()
		return classroom

	def createStudent(self, firstName, lastName, studentNumber):
		student = Student.create(classroom=self, firstName=firstName, lastName=lastName, studentNumber=studentNumber)
		student.save()

	def rename(self, newname):
		self.name = newname
		self.save()
		return newname

	def __str__(self):
		return self.name

class Student(models.Model):
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
	firstName = models.CharField(max_length=40, default='N/A')
	lastName = models.CharField(max_length=40, default='N/A')
	studentNumber = models.CharField(max_length=20, default='12345')

	@classmethod
	def create(cls, classroom, firstName, lastName, studentNumber):
		student = cls(classroom=classroom, firstName=firstName, lastName=lastName, studentNumber=studentNumber)
		student.save()
		return classroom

	class Meta:
		ordering = ('lastName', 'firstName', 'studentNumber')

	def getName(self):
		return ' '.join([self.firstName, self.lastName])

	def getNameWrong(self):
		return ','.join([self.lastName, self.firstName])

	def __str__(self):
		return ','.join([self.firstName, self.lastName, self.studentNumber])


class Account(AbstractBaseUser):
	classroom = models.ManyToManyField(Classroom)
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

	def addClass(self, name):
		classroom = Classroom.create(name)
		self.classroom.add(classroom)

	def __str__(self):
		return self.email

	def getName(self):
		return ' '.join([self.firstName, self.lastName])

	def getLastName(self):
		return self.lastName

	@property
	def is_staff(self):
		return self.is_admin
