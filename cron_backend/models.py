from django.db import models
from django.conf import settings


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    # class Meta:

    def __str__(self) -> str:
        return self.title
