from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('postsignup/', views.postsignup),
    path('postlogin/', views.postlogin),
] 