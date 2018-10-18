from django.http import HttpResponse
from django.shortcuts import render

from .models import User
from . import forms


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        return HttpResponse(form.data['login_id'])
    else:
        form = forms.LoginForm()
        return render(request, 'login/login_form.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        user = User()
        user.login_id = form.data['login_id']
        user.username = form.data['username']
        user.password = form.data['password']
        user.save()
        print(User.objects.all())
        return render(request, 'login/create_user_form.html', {'form': form})
    else:
        form = forms.CreateUserForm()
        return render(request, 'login/create_user_form.html', {'form': form})


def detail(request, question_id):
    return HttpResponse("you are looking detail at %s" % question_id)


def results(request, question_id):
    return HttpResponse("you are looking results at %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are looking vote at %s" % question_id)
