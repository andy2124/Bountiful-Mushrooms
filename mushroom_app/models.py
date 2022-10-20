from django.db import models

class Mushroom(models.Model):
    date = models.DateTimeField(auto_now=True)
    latitude_north = models.IntegerField(default=0)
    latitude_south = models.IntegerField(default=0)
    longitude_east = models.IntegerField(default=0)
    longitude_west = models.IntegerField(default=0)
    mushroom_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.URLField(unique=True)
    
    def __str__(self):
        return f'{self.mushroom_name} -- {self.date}'

