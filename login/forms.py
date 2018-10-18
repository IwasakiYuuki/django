from django import forms
from .models import User


class LoginForm(forms.Form):
    login_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Login ID'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CreateUserForm(forms.Form):
    login_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Login ID'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
