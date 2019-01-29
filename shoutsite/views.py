# pylint: disable=no-member

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import NoReverseMatch
import datetime

from .models import User, Shout, Profile

def feed(request):
    if request.method == 'POST':
        if request.POST.get('order_by') == 'popular':
            text = Shout.objects.all().order_by('-likes', '-pub_date')
        elif request.POST.get('order_by') == 'latest_following':
            my_profile = Profile.objects.get(owner=request.user)
            text = Shout.objects.filter(user__in = my_profile.following.all()).order_by('-pub_date')
        elif request.POST.get('order_by') == 'popular_following':
            my_profile = Profile.objects.get(owner=request.user)
            text = Shout.objects.filter(user__in = my_profile.following.all()).order_by('-likes', '-pub_date')
        else:
            text = Shout.objects.all().order_by('-pub_date')  
    else:
        text = Shout.objects.all().order_by('-pub_date')
    context = {'text': text}
    return render(request, "shouts/feed.html", context)

@login_required
def new_post(request):
    return render(request, 'shouts/shout.html')

@login_required
def submit_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        if len(request.POST.get("shout_input","")) != 0:
            new_shout = Shout(shout_text=request.POST.get("shout_input",""),pub_date=datetime.datetime.now(),user=request.user)
            new_shout.save()
            return redirect('feed')
        else:
            return redirect('new_post')
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
def profile(request, username):
    text = Shout.objects.filter(user__username=username)
    try:
        profile_owner = User.objects.get(username=username)
        profile_found = True
    except User.DoesNotExist:
        profile_owner = None
        profile_found = False

    context = {'text': text, 'profile_found': profile_found}
    return render(request, 'profile.html', context)

@login_required
def follow_user(request, username):
    my_profile = Profile.objects.get(owner=request.user)
    user_to_follow = User.objects.get(username=username)
    my_profile.following.add(user_to_follow)
    context = {'text': user_to_follow.username}
    return redirect(request, 'profile.html', context)
