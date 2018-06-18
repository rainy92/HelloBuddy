from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(max_length=18, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=18, widget=forms.PasswordInput)


class LoginForm():
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=18, widget=forms.PasswordInput)