from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('feed/', views.feed, name='feed'),
    path('submit_post/', views.submit_post, name='submit_post'),
    path('profile/', views.profile, name='profile'),
    ]
