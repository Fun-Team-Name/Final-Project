from django.test import TestCase
from teacher.models import Account, AccountManager, Classroom, Student
# Create your tests here.
class AccountTest(TestCase):
	def create_account(self,  email = 'myemail@gmail.com', firstName = 'first', lastName = 'last'):
		return Account.objects.create_user(email = email, firstName = firstName, lastName = lastName)
	def test_account_creation_shouldpass(self):
		account = self.create_account()
		self.assertTrue(isinstance(account, Account))
	def test_account_creation_shouldfail(self):
		account = self.create_account()
		self.assertFalse(isinstance(account, Account))
	def test_account_email(self):
		account = self.create_account()
		self.assertEqual(account.__str__(), account.email)
	def test_account_lastname(self):
		account = self.create_account()
		self.assertEqual(account.getLastName(), account.lastName)

# class TeacherFunctionsTest(TestCase):
# 	def add_class()
