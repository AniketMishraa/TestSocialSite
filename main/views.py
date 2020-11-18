from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm,EditProfileForm, EditOtherProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .import models
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(response):
	return render(response, 'home.html')

def register(response):
	
	if response.method == "POST":
		form = RegistrationForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		form = RegistrationForm()

	
	return render(response, "register.html", {"form":form})
@login_required(login_url='/')
def profile(request):

	args = {'user': request.user}
	return render(request, 'profile.html', args)
@login_required(login_url='/')
def edit(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST, instance = request.user)
		pform = EditOtherProfileForm(request.POST,request.FILES, instance = request.user.profile)
		#pic = request.FILES.get('profile_pic')
		#print(pic)
		#pform.profile_pic = pic
		if form.is_valid() and pform.is_valid():

			form.save()
			pform.save()
			print(pform)
			return redirect('/profile')
	else:
		form = EditProfileForm(instance=request.user)
		pform = EditOtherProfileForm(instance = request.user.profile)
		args = {'form': form, 'pform':pform}
		return render(request, 'edit.html', args)