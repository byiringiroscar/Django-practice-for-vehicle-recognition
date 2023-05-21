from django.contrib import admin
from django.urls import path, include

from . import views

name = 'login_app'

urlpatterns = [
    path('', views.base, name='base'),
    path('loginn/', views.loginn, name='login')
]
