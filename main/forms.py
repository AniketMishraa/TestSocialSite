from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .import models

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit = True):
		user = super(RegistrationForm,self).save(commit = False)
		#user.username = self.cleaned_data['username']
		#user.email = self.cleaned_data['username']

		if commit:
			user.save()
		return user

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		exclude = ('password1','password2','password',)
		fields = (
			'email',
			'username',
			)
class EditOtherProfileForm(UserChangeForm):

	class Meta:
		
		model = models.Profile
		exclude = ('password1','password2','password',)
		fields = (
			'nickname',
			'profile_pic',
			)