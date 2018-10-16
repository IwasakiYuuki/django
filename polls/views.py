from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def detail(request, question_id):
    return HttpResponse("you are looking detail at %s"%question_id)

def results(request, question_id):
    return HttpResponse("you are looking results at %s"%question_id)

def vote(request, question_id):
    return HttpResponse("you are looking vote at %s"%question_id)
