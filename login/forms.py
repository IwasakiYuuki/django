from django import forms
from .models import User


class LoginForm(forms.Form):
    login_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Login ID'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CreateUserForm(forms.Form):
    login_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Login ID'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'UserName'}))

    def clean(self):
        cldata = super().clean()
        login_id = cldata.get('login_id')
        password = cldata('password')
        username = cldata('username')
        raise forms.ValidationError('this is in clean()')

    def clean_login_id(self):
        login_id = self.cleaned_data['login_id']
        print("aaaaaaa")
        raise forms.ValidationError('this is test.')

    def clean_password(self):
        password = self.cleaned_data['password']
        print('pass')
        raise forms.ValidationError('this is pass.')