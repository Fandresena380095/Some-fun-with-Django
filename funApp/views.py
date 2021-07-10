from django.shortcuts import render
from .models import User_Database
from .forms import User_Form
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