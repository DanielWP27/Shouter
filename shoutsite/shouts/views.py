from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django import forms
import datetime

from .models import Shout

def index(request):
    return redirect('feed')

def new_post(request):
    return render(request, 'shouts/shout.html')

def submit_post(request):
    if request.method == 'POST':
        new_shout = Shout(shout_text=request.POST.get("shout_input",""),pub_date=datetime.datetime.now())
        new_shout.save()
        return redirect('feed')
    
def feed(request):
    text = Shout.objects.all()
    context = {'text': text}
    return render(request, "shouts/feed.html", context)

def profile(request):
    return HttpResponse(request.user.username)
