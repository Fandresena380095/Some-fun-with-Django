from .models import User_Database
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class User_Form(forms.ModelForm):

	class Meta:
		model = User_Database
		fields = ["name", "email"]


class registerForm(UserCreationForm):

	class Meta:
		model = User
		fields = '__all__'


