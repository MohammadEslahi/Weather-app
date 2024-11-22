from django.db import models
from django.contrib.auth.models import AbstractUser




class City(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    fav_cities = models.ManyToManyField(City, related_name='users', blank=True)

    def __str__(self):
        return self.username
    






    