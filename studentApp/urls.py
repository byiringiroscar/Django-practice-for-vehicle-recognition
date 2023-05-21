from django.contrib import admin
from django.urls import path

from . import views

name = 'studentApp'

urlpatterns = [
    path('register', views.register, name='register')
]