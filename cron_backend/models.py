from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     fio = models.CharField(max_length=500)
#     phone = models.DateField(null=True, blank=True)


class Clinic(models.Model):
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'


class Service(models.Model):
    type = models.CharField(max_length=150)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class Doctor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    speciality = models.ForeignKey(Service, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name+' '+self.surname

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete= models.CASCADE, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True)
    # title = models.CharField(max_length=150)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    # status = models.CharField(max_length=20)


    def __str__(self) -> str:
        return "Запись на " + self.date

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'  
