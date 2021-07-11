from django.shortcuts import render , redirect
from .models import User_Database
from .forms import *
from django.contrib import messages
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
#To Restrain a view form being seen if not logged in 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
	form = User_Form()
	if request.method == "POST":
		form_data = User_Form(request.POST)
		if form_data.is_valid():
			form_data.save()

	else :
		form = User_Form()
	return render(request, "funApp/index.html", {
		"form": form,
		"users": User_Database.objects.all()
		 })


def register(request):
	#When the user is already logged in 
	if request.user.is_authenticated:
		return redirect('index')

	else:
		if request.method == "POST":
			form = registerForm(request.POST)
			if form.is_valid():
				print(form)
				form.save()
				return redirect("index")
				
		else:
			form = registerForm()

		return render(request, "funApp/home.html", {
			"form": form
			})
