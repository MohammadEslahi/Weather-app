from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.username