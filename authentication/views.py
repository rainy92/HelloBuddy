from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class LoginView(View):
    def post(self, request):
        pass


class RegisterView(View):
    def post(self, request):
        pass


class LogoutView(View):
    pass