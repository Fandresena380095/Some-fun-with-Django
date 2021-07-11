from django.shortcuts import render , redirect
from .models import User_Database
from .forms import *
from django.contrib import messages

# Create your views here.
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
	form = registerForm()
	if request.method == "POST":
		form = registerForm(request.POST)
		form.save()
		return redirect("/index")
		
	else:
		form = registerForm()

	return render(request, "funApp/home.html", {
		"form": form
		})
