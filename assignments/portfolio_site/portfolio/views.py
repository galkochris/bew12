from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Portfolio Home")

def contact(request):
    return HttpResponse("Contact Me")

def greet_by_name(request, name):
    return HttpResponse("Hello, %s" % name)
