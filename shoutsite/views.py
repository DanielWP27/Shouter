# pylint: disable=no-member

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
def submit_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        if len(request.POST.get("shout_input","")) != 0:
            new_shout = Shout(shout_text=request.POST.get("shout_input",""),pub_date=datetime.datetime.now(),user=request.user)
            new_shout.save()
            return redirect('feed')
        else:
            return redirect('feed')
    else:
        return redirect('feed')

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

def profile(request, username):
    if request.user.is_authenticated:
        text = Shout.objects.filter(user__username=username)
        try:
            profile_owner = User.objects.get(username=username)
            profile_found = True
            user_profile = Profile.objects.get(owner=request.user)
            this_profile = Profile.objects.get(owner=profile_owner)
            profile_set = Profile.objects.all().filter(following__username = profile_owner.username)
            if user_profile.following.filter(username = profile_owner.username):
                already_following = True
            else:
                already_following = False

            context = {'text': text, 'this_profile': this_profile, 'profile_set': profile_set, 'username': username, 'profile_found': profile_found, 'already_following': already_following}
            return render(request, 'profile.html', context)
        except User.DoesNotExist:
            profile_owner = None
            profile_found = False
            already_following = False
            return render(request, 'profile.html')
    else:
        return redirect('feed')

@login_required
def follow_user(request, username):
    my_profile = Profile.objects.get(owner=request.user)
    user_to_follow = User.objects.get(username=username)
    my_profile.following.add(user_to_follow)
    text = user_to_follow.username
    following_profile = Profile.objects.get(owner=user_to_follow)
    following_profile.followers += 1
    following_profile.save()
    return redirect('profile', text)

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('login_user')
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile(owner=user)
            profile.save()
            login(request, user)
            return redirect('feed')
        else:
            form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
