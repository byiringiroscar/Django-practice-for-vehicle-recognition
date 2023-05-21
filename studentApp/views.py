from django.shortcuts import render

from .models import Student
from django.db import connection


# Create your views here.

def register_(request):
    posts = Student.objects.all()
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


def register(request):
    posts = Student.objects.filter(surname__startswith='maron') | Student.objects.filter(surname__startswith='white')
    return render(request, 'output.html', {'posts': posts})
