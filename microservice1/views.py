from django.contrib.auth.views import LoginView
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'microservice1/login.html'
