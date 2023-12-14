from django.contrib import admin
from django.urls import path
from .views import RegisterVeiw, VerifyEmail
from .views import InstitutionRegisterVeiw

urlpatterns = [
    path('register/', RegisterVeiw.as_view(), name= 'register'),
    path('email-verify/', VerifyEmail.as_view(), name= 'email-verify'),
    path('register_as_intitustion/', InstitutionRegisterVeiw.as_view(), name= 'register'),
]
