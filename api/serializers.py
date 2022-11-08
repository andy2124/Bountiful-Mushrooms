from rest_framework import serializers
from mushroom_app.models import Mushroom 

class MushroomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('date','latitude_north','latitude_south', 'longitude_east','longitude_west','mushroom_name', 'location', 'image', 'user')
        model = Mushroom
