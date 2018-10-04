import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from teacher.models import Account
from teacher.models import Student
from teacher.models import Classroom

class signupForm(forms.ModelForm):
	password1 = forms.CharField(min_length=12, widget=forms.PasswordInput)
	password2 = forms.CharField(min_length=12, widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'firstName', 'lastName')

	def clean_email(self):
		email = self.cleaned_data['email']
		if not re.match(r"[^@]+@[^@]+.[^@]+", email):
			raise ValidationError(_('Invalid email'))
		#check user with email exists
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Passwords do not match')
		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class addStudentsForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('firstName', 'lastName', 'studentNumber')

	def clean_lastName(self):
		name = self.cleaned_data['lastName']
		return name.lower()

	def clean_firstName(self):
		name = self.cleaned_data['firstName']
		return name.lower()

	def save(self, commit=True):
		student = super().save(commit=False)
		if commit:
			student.save()
		return user

class addClassroomForm(forms.ModelForm):

	class Meta:
		model = Classroom
		fields = ('name',)

	def save(self, commit=True):
		classroom = super().save(commit=False)
		if commit:
			classroom.save()
		return classroom
