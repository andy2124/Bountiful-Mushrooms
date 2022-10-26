from django.db import models
from django.contrib.auth.models import User


class Mushroom(models.Model):
    date = models.DateTimeField(auto_now=True)
    latitude_north = models.FloatField(default=0)
    latitude_south = models.FloatField(default=0)
    longitude_east = models.FloatField(default=0)
    longitude_west = models.FloatField(default=0)
    mushroom_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.URLField(unique=False)
    
    def __str__(self):
        return f'{self.mushroom_name} -- {self.date}'

class User(models.Model):
    pass