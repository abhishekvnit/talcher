from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('welcome', views.welcome, name='welcome'),
    path('contact', views.contact, name='contact')
]
