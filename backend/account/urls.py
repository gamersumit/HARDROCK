from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register_view, name = 'user_register'), 
    path('signin/', views.signin_view, name = 'signin'),
    ]