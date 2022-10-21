#managment command use to progromanttically update 
from django.core.management.base import BaseCommand
from mushroom_app.models import *
import requests
import json


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        with open("mushrooms.json") as f:
            mushroom_data = json.loads(f.read())
            
            # print(mushroom_data, 'testing mushroom data')
        # f = open('mushrooms.json')
        # mushie = json.loads(f.read())
        # print(mushie) look at pokedex/pokemon.managment file in code
        for mushy in mushroom_data['results']:
            mushroom = Mushroom()
            mushroom.date = mushy['date'] 
            mushroom.mushroom_name = mushy['namings'][0]['name']['name']
            mushroom.latitude_north = mushy['location']['latitude_north']
            mushroom.latitude_south = mushy['location']['latitude_south']
            mushroom.longitude_east = mushy['location']['longitude_east']
            mushroom.longitude_west = mushy['location']['longitude_west']
            mushroom.location = mushy['location']['name']
            mushroom.image = mushy['primary_image']['original_url']
            mushroom.save()

            # mushroom.latitude_north = mushy[0]
            # print(mushroom, 'mushroom')
            print(mushroom.date, 'mushy')
            print(mushroom.mushroom_name,'mush name')
            print(mushroom.latitude_north,'north')
            print(mushroom.latitude_south,'south')
            print(mushroom.longitude_east,'east')
            print(mushroom.longitude_west,'west')
            print(mushroom.location,'location')
            print(mushroom.image,'image')
