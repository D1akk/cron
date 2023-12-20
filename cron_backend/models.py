from django.db import models
from django.conf import settings


class Doctor(models.Model):
    name    = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)



    def __str__(self) -> str:
        return self.title
