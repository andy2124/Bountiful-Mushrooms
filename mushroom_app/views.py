from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse 
import requests as fetch 
from . import models 
from django.http import JsonResponse
import json

def index(request):
    mushroom_data = models.Mushroom.objects.all()
    context = {
        'mush_data':mushroom_data
    }

    return render(request, 'mushroom_app/index.html', context)

def home(request):
    url = ('https://mushroomobserver.org/api2/observations?detail=high')
    # url = ('https://api.thecatapi.com/v1/images/search')
    response = fetch.get(url)
    print(response)
    # return HttpResponse('Welcome to mushrooms')
    return HttpResponse(response)

def testjson(request):

     results = [

     ]