from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from matplotlib.style import context
from . import models 
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from.forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model


def index(request):
    mushroom_data = models.Mushroom.objects.all()
    context = {
        'mush_data':mushroom_data
    }

    return render(request, 'mushroom_app/index.html', context)

def register(request):
	if request.method == "POST":
		form = NewSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("registration/profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewSignUpForm()
	return render(request=request, template_name="registration/register.html", context={"form":form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def user_logout(request):
	logout(request)
	return render(request, 'registration/login.html')
  	# return render(request, 'registration/profile.html')
	
# def signup(request):
#     if request.method == "GET":
#         form = NewSignUpForm()
#         return render(request, 'mushroom_app/signup.html', {
#             'form' : form
#     })
#     elif request.method == 'POST':
#         form = NewSignUpForm(request.POST) #getting info back from forms model that user enters in field
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username = form.cleaned_data['username'],
#                 first_name = form.cleaned_data['first_name'],
#                 last_name = form.cleaned_data['last_name'],
#                 email = form.cleaned_data['email'],
#                 password = form.cleaned_data['password'],
#             )
#         return HttpResponseRedirect(reverse('mushroom_app:signup'))

# def user_login(request):
#     if request.method == "GET":
#         return render(request, 'mushroom_app/login.html',{
#             'form': NewLoginIn()

#         })
# def user_login(request):
    
       
#     if request.method == 'POST':
#        form = NewLoginIn(request.POST)
#        if form.is_valid():
#            password = form.cleaned_data['password'],
#            user = authenticate(request, username=form.cleaned_data['username'], password=password)
#            if user is not None:
#                login(request, user)
#                print(user,'user has been logged in ')
#                print(request,'request')
#                return HttpResponseRedirect(reverse('profile',)) 
#            else:
#                form.add_error('username', 'invalid credentials')
#                return render(request, 'mushroom_app/login.html',{
#                    'form': form
#                })
#     return render(request, 'mushroom_app/login.html', {
#         'form': NewLoginIn()
#         })

# def profile(request, username):
#     if request.method == 'GET':

#         user = get_object_or_404(get_user_model(), username=username)

#         context = {

#         'username': user.username,
        
#         }   
#     print('we made it to the profile')
#     # return render(request, 'mushroom_app/profile.html')
#     return redirect(reverse('mushroom_app:profile', kwargs={ 'username': user.username}))

# def user_logout(request):
#     logout(request)
#     return redirect(reverse('mushroom_app:login'))



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
