from .models import User_Database
from django import forms

class User_Form(forms.ModelForm):

	class Meta:
		model = User_Database
		fields = ["name", "email"]