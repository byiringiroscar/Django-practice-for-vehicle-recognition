from django.contrib import admin
from . models import Car_registration, Tax, Insurance, Control

# Register your models here.

admin.site.register(Car_registration)
admin.site.register(Tax)
admin.site.register(Control)
admin.site.register(Insurance)
