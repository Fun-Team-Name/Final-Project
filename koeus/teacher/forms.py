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

class signup(forms.Form):
	email = forms.EmailField()
	password1 = forms.CharField()
	password2 = forms.CharField()

	def clean_email(self):
		data = self.cleaned_data['email']
		if not re.match(r"[^@]+@[^@]+.[^@]+", email);
			raise ValidationError(_('Invalid email'))
		#check user with email exists
		return data
