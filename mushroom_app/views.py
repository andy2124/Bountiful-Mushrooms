import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from matplotlib.style import context
from . import models 
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model


def index(request):
    mushroom_data = Mushroom.objects.all().order_by('-date')
    context = {
        'mush_data':mushroom_data,
		'form_1': NewMushroomForm(),
    }

    return render(request, 'mushroom_app/index.html', context)

def register(request):
	if request.method == "POST":
		form = NewSignUpForm(request.POST)
		# print(form,'form')
		if form.is_valid():
			user = form.save()
			# print(form, 'form')
			# print(request.POST) 
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('mushroom_app:profile')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
	# if request.method == "GET":
		form = NewSignUpForm()
	return render(request=request, template_name="registration/register.html", context={"form":form})

@login_required
def profile(request):
	form = NewMushroomForm()
	context = {
		'form': form, 
		'mushroom':  Mushroom.objects.filter(user = request.user)
	}
	if request.method == "POST":
		form = NewMushroomForm(request.POST)
	if form.is_valid():
		mush = Mushroom()
		mush.image = form.cleaned_data['image']
		mush.mushroom_name = form.cleaned_data['mushroom_name']
		mush.location = form.cleaned_data['location']
		mush.save()
	return render(request, 'registration/profile.html', context)

@login_required
def user_logout(request):
	logout(request)
	return render(request, 'registration/login.html')

@login_required
def new_mushroom(request):
	if request.method == "POST":
		form = NewMushroomForm(request.POST)
		if form.is_valid():
			mush = Mushroom()
			mush.image = form.cleaned_data['image']
			mush.mushroom_name = form.cleaned_data['mushroom_name']
			mush.location = form.cleaned_data['location']
			mush.user = request.user
			mush.save()
	return redirect('mushroom_app:profile')
	
def delete(request, mushroom_id): #mushroom could be anything 
	mushroom = get_object_or_404(Mushroom, id= mushroom_id, user=request.user)
	mushroom.delete()
	return redirect('mushroom_app:index')
