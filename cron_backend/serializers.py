from rest_framework import serializers
from .models import Appointment, Doctor, Service, Clinic


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'fio', 'phone') 


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class DoctorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
