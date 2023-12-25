from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from .models import Appointment, Doctor, Specialist, Clinic
from .serializers import AppointmentSerializer, DoctorSerilizer, SpecialistSerializer, ClinicSerializer


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
        })

class ListCreateAppointment(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)
    

class AppointmentListView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)


class AppointmentAddView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class AppointmentSelectView(APIView):
    def post(self, request):
        client_id = request.data.get('client_id')
        appointment_id = request.data.get('appointment_id')
        client = settings.AUTH_USER_MODEL.objects.get(id=client_id)
        client.appointments.add(*appointment_id)
        client.save()
        return Response({"massage":"Запись добавлена"})  

#Временное решение класса Доктора
class DoctorListView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerilizer(doctors, many=True)
        return Response(serializer.data)


class DoctorAddView(APIView):
    def post(self, request):
        serializer = DoctorSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class SpecialistListView(APIView):
    def get(self, request):
        services = Specialist.objects.all()
        serializer = SpecialistSerializer(services, many=True)
        return Response(serializer.data)
    

class ClinicListListView(APIView):
    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)