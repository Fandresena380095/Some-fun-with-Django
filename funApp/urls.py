from django.urls import path , include
from . import views

urlpatterns = [
	path("index/", views.index , name='index' ),
	path("", include('django.contrib.auth.urls')),
	path("register/", views.register, name ="register"),
	path('login2/', views.login2 , name = "login2")
]