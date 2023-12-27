from django.urls import path
from .views import (
    Login,
    ListCreateAppointment,
    AppointmentListView,
    AppointmentAddView,
    AppointmentSelectView,
    DoctorAddView,
    DoctorListView,
    ServiceListView,
    ClinicListListView,
    ClinicDetailsView
)
from django.contrib.auth.views import LogoutView;

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    # path('list-create-appointment/', ListCreateAppointment.as_view(), name='list-create-appointment'),
    path('appointment-add/', AppointmentAddView.as_view(), name='appointment-add'),
    path('appointment-list/', AppointmentListView.as_view(), name='appointment-list'),
    path('doctor-add/', DoctorAddView.as_view(), name='doctor-add'),
    path('doctor-list/', DoctorListView.as_view(), name='doctor-list'),
    path('specialist-list/', ServiceListView.as_view(), name='specialist-list'),
    path('clinic-list/', ClinicListListView.as_view(), name='clinic-list'),
    path('clinic-details/<int:clinic_id>/', ClinicDetailsView.as_view()),
]