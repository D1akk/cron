from django.db import models
from django.conf import settings


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.specialization +' '+ self.surname + ' ' +self.name

    class Meta:
        verbose_name = 'Стоматолог'
        verbose_name_plural = 'Стоматологи'  



class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'  
