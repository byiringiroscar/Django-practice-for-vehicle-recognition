from django.shortcuts import render
from .models import Car_registration, Control, Tax, Insurance

# Create your views here.

plate_number = 'RAE933C'


def check(requests):
    return render(requests, 'html/plane.html')


def capture_plate(requests):
    phone_n = Car_registration.objects.filter(plate_number=plate_number)
    plate_n = Car_registration.objects.filter(plate_number=plate_number)
    tax_n = Tax.objects.all()
    insu_n = Insurance.objects.all()
    control_n = Control.objects.all()

    context = {
        'insurance': Insurance.objects.all(),
        'tax': Tax.objects.all(),
        'control': Control.objects.all(),
        'cars': Car_registration.objects.all(),
        'search': Car_registration.objects.all().get(plate_number=plate_number),
        'plate_number': plate_number,
        'phone_n': phone_n,
        'tax_n': tax_n,
        'insu_n': insu_n,
        'control_n ': control_n,

    }

    return render(requests, 'html/home.html', context)
