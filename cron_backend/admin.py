from django.contrib import admin
from .models import Appointment, Doctor, Specialist, Clinic

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Specialist)
admin.site.register(Clinic)