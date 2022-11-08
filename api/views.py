from rest_framework import viewsets
from mushroom_app.models import Mushroom
from .serializers import MushroomSerializer
from rest_framework import viewsets
class MushroomViewSet(viewsets.ModelViewSet):
    queryset = Mushroom.objects.all()
    serializer_class = MushroomSerializer
    http_method_names = ['get','delete','post','put']