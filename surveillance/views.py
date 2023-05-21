from django.shortcuts import render


# Create your views here.

def police(request):
    return render(request, 'html/output.html')
