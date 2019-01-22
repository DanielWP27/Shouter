"""shouter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from shoutsite import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('admin/', admin.site.urls),
    path('new_post/', views.new_post, name='new_post'),
    path('submit_post/', views.submit_post, name='submit_post'),
    path('login/', views.login_user, name='login_user'),
    path('login_red/', views.login_redirect, name='login_redirect'),
    path('logout/', views.logout_user, name='logout_user'),
]
