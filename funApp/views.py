from django.shortcuts import render , redirect
from .models import User_Database
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
#To Restrain a view form being seen if not logged in 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
	# user = authenticate(username="jojo", password="jojo1379")
	# if user is not None :
	# 	message = 'Hello Admin'
	mainUser = User.objects.get(username ="jojo")
	secondUser = User.objects.get(username ="rara")
	message = "Welcome"

	form = User_Form()
#limit access to a user : request.user.username.startswith(<something>)
	if request.method == "POST" and request.user.username.startswith('jojo'):
		form_data = User_Form(request.POST)
		if form_data.is_valid():
			form_data.save()
			message = "Cool"

	else :
		form = User_Form()
	return render(request, "funApp/index.html", {
		"form": form,
		"users": User_Database.objects.all(),
		"admin_message": message
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


def login2(request):

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		print(name, email, password)
		user = User.objects.create_user(name, email, password)
		user.save()

		return redirect("index")




	else:
		return render(request , 'funApp/login2.html', {}) 
		
		return render(request , 'funApp/login2.html', {})
