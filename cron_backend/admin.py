from django.contrib import admin
from .models import Appointment, Doctor, Service, Clinic

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(Clinic)