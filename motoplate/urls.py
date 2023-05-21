from django.contrib import admin
from django.urls import path, include

from . import views

name = 'motoplate'

urlpatterns = [
    path('',  views.index, name='index')
]