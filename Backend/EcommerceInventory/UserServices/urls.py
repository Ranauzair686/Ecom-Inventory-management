from django.contrib import admin
from django.urls import path, include
from .controller import AuthController


urlpatterns = [
    path('login/', AuthController.LoginAPIView.as_view() , name = 'login') ,
    path('signup/', AuthController.SignupAPIView.as_view() , name = 'signup') ,
]