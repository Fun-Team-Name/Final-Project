import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from teacher.models import Account
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

class signupForm(forms.ModelForm):
	#email = forms.EmailField()
	#firstName = forms.CharField(label='Password', widget=forms.PasswordInput)
	#lastName = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	password1 = forms.CharField(min_length=12, widget=forms.PasswordInput)
	password2 = forms.CharField(min_length=12, widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'firstName', 'lastName')#, 'password1', 'password2')

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
