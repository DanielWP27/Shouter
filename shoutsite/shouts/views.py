from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import Shout

def index(request):
    return HttpResponse("Hello, world. You're at the shouts index.")

def new_post(request):
    return render(request, 'shouts/shout.html')

def result(request):
    return render(request, 'placeholder')

def feed(request):
    return HttpResponse("Welcome to your feed!")

def profile(request):
    return HttpResponse("This is your profile!")
