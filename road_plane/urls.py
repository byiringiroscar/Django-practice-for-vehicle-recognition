from django.contrib import admin
from django.urls import path, include

from . import views

name = 'road_plane'

urlpatterns = [
    path('', views.check, name='check'),
    path('capture_plate', views.capture_plate, name='capture_plate'),
]