#managment command use to progromanttically update 
from django.core.management.base import BaseCommand
from mushroom_app.models import *
import requests
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # url = "https://mushroomobserver.org/api2/observations?detail=high"
        # payload={}
        # headers = {}
        # response = requests.request("GET", url, headers=headers, data=payload)
        # print(response.text)
        # response = response.get("Bountiful-Mushrooms/mushrooms.json")
        # print(response,'response')
        with open("mushrooms.json") as f:
            mushroom_data = json.loads(f.read())
            print(mushroom_data, 'testing mushroom data')
        # f = open('mushrooms.json')
        # mushie = json.loads(f.read())
        # print(mushie) look at pokedex/pokemon.managment file in code
        mushroom = Mushroom()

        for mushy in mushroom_data['results']:
            mushroom.date = mushy['date'] 
            mushroom.mushroom_name = mushy['namings'][0]['name']['name']
            mushroom.latitude_north = mushy['location']['latitude_north']
            mushroom.latitude_south = mushy['location']['latitude_south']
            mushroom.longitude_east = mushy['location']['longitude_east']
            mushroom.longitude_west = mushy['location']['longitude_west']
            mushroom.location = mushy['location']['name']
            mushroom.image = mushy['primary_image']['original_url']


            # mushroom.latitude_north = mushy[0]
            print(mushroom, 'mushroom')
            print(mushroom.date, 'mushy')
            print(mushroom.mushroom_name,'mush name')
            print(mushroom.latitude_north,'north')
            print(mushroom.latitude_south,'south')
            print(mushroom.longitude_east,'east')
            print(mushroom.longitude_west,'west')
            print(mushroom.location,'location')
            print(mushroom.image,'image')
            





        # for m in mushroom_data['results'][0]['location']:
        #     mushroom.latitude_north = m["latitude_north"]
        #     print(m,'longitude')


            #mushroom_data['results'][0]['location']
            # date_ext = mushy.get('date')
            # location_ext = mushy.get('location')
            # image_ext = mushy.get('image')
            # mushroom_name_ext = mushy.get('name')
            # latitude_north_ext = mushy.get('latitude_north')
            # latitude_south_ext = mushy.get('latitude_south')
            # longitude_west_ext= mushy.get('longitude_west')
            # longitude_east_ext = mushy.get('longitude_east')

            # mush_obj = mushy.objects.create(
            #     date = date_ext,
            #     location= location_ext,
            #     image = image_ext,
            #     mushroom_name = mushroom_name_ext,
            #     latitude_north= latitude_north_ext,
            #     latitude_south = latitude_south_ext,
            #      longitude_west = longitude_west_ext,
            #      longitude_east = longitude_east_ext,

            # )
            # print(mush_obj.mushroom_name + 'has been uploaded')
