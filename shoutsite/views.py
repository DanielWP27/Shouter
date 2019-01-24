from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import datetime

from .models import Shout

def feed(request):
    if request.user.is_authenticated:
        text = Shout.objects.all()
        context = {'text': text}
        return render(request, "shouts/feed.html", context)
    else:
        return redirect('login_user')

@login_required
def new_post(request):
    return render(request, 'shouts/shout.html')

@login_required
def submit_post(request):
    if request.method == 'POST':
        if len(request.POST.get("shout_input","")) != 0:
            new_shout = Shout(shout_text=request.POST.get("shout_input",""),pub_date=datetime.datetime.now(),user=request.user)
            new_shout.save()
            return redirect('feed')
        else:
            return redirect('new_post')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        form = AuthenticationForm(request.POST)
        context = {'form': form}
        return render(request, 'login.html', context)  

def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return redirect('login_user')

@login_required  
def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required
def profile(request):
    text = Shout.objects.filter(user=request.user)
    context = {'text': text}
    return render(request, 'profile.html', context)
