import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from flask import g 
import requests as fetch 
from . import models 
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from.forms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def index(request):
    mushroom_data = models.Mushroom.objects.all()
    context = {
        'mush_data':mushroom_data
    }

    return render(request, 'mushroom_app/index.html', context)

def signup(request):
    if request.method == "GET":
        form = NewSignUpForm()
        return render(request, 'mushroom_app/signup.html', {
            'form' : form
    })
    elif request.method == 'POST':
        form = NewSignUpForm(request.POST) #getting info back from forms model that user enters in field
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )
        return HttpResponseRedirect(reverse('signup'))

def user_login(request):
    if request.method == 'GET':
        return render(request, 'mushroom_app/login.html', {
            'form': NewLoginIn()
        })
    elif request.method == 'POST':
       form = NewLoginIn(request.POST)
       if form.is_valid():
           password = form.cleaned_data['password'],
           user = authenticate(request, username=form.cleaned_data['username'], password=password)
           if user is not None:
               login(request, user)
               print(user,'user')
               print(request,'request')
               return HttpResponseRedirect(reverse('profile')) 
           else:
               form.add_error('username', 'invalid credentials')
               return render(request, 'mushroom_app/login.html',{
                   'form': form
               })

def profile(request):
    return render(request, 'mushroom_app/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mushroom_app:login'))



# def home(request):
#     url = ('https://mushroomobserver.org/api2/observations?detail=high')
#     # url = ('https://api.thecatapi.com/v1/images/search')
#     response = fetch.get(url)``
#     print(response)
#     # return HttpResponse('Welcome to mushrooms')
#     return HttpResponse(response)

# def testjson(request):

#      results = [
#      ]
