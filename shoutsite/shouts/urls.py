from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shouts/new_post/', views.new_post, name='new_post'),
    path('', views.feed, name='feed'),
    path('', views.profile, name='profile'),
    ]
