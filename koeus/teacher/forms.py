import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
'''
class AddToClass(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
		if not re.match(r"[^@]+@[^@]+.[^@]+", email);
			raise ValidationError(_('Invalid email'))
		#check user with email exists
        return data
'''

class signupForm(forms.Form):
	email = forms.EmailField()
	password1 = forms.CharField(min_length=12)
	password2 = forms.CharField(min_length=12)

	def clean_email(self):
		email = self.cleaned_data['email']
		if not re.match(r"[^@]+@[^@]+.[^@]+", email):
			raise ValidationError(_('Invalid email'))
		#check user with email exists
		return email

	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if not password1 == password2:
			raise ValidationError(_('Passwords do not match'))
		return password1
