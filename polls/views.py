from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def index(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        return HttpResponse(form.data['login_id'])
    else:
        form = forms.LoginForm()
        return render(request, 'polls/login_form.html', {'form': form})


#def create_user(requet):



def detail(request, question_id):
    return HttpResponse("you are looking detail at %s" % question_id)


def results(request, question_id):
    return HttpResponse("you are looking results at %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are looking vote at %s" % question_id)
