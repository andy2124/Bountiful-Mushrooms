from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *

class NewSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,
    label='Email',
    error_messages={'exists': 'User exists'})
    # password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"]) 
        if commit:
            user.save()
        return user

class NewMushroomForm(ModelForm):
    class Meta:
     model = Mushroom
     fields = ['mushroom_name', 'location', 'image']


    