from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from json import dumps


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
		'mushroom':  Mushroom.objects.order_by('-date').filter(user = request.user)
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




def mushroom_question(request):
	data = [
		["MN", "Morchella esculenta (current)"],#MINESOTA
		["OR", "Cantharellus formosus (current)"],#OREGON
		["TX", "Chorioactis geaster (current)"],#TEXAS
		["MA", "Calvatia gigantea"],#MASSACHUSETS
		["MO", "Cantharellus lateritius"],#MISSORRI	
		["NY", "Lactarius peckii"],#NEW YORK
		["WA", "Tricholoma magnivelare"],#WASHINTON


	]
	data = dumps(data)
	return render(request, "mushroom_app/mushroom_data.html", {"data": data})


