from django.urls import path
from . import views

name = 'surveillance'

urlpatterns = [
    path('police', views.police, name='police')
]
