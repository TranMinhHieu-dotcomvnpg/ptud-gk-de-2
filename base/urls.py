from django.contrib import admin
from django.urls import path, include
from .views import home, signup, news, update_avatar,profile, task_complete, task_create, task_list

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name="home"),
    path('accounts/',include("django.contrib.auth.urls")),
    path("signup/",signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('news',news,name='news'),
    path('update-avatar/', update_avatar, name='update_avatar'),
    path('profile/', profile, name='profile'), 
    path('', task_list, name='task_list'),
    path('new/', task_create, name='task_create'),
    path('complete/<int:task_id>/', task_complete, name='task_complete'),

]
