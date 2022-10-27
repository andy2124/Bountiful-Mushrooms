from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

        # from django import forms

class NewSignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25) #
    password = forms.CharField(widget=forms.PasswordInput, label='Password',max_length=10)# widget puts the dots
    first_name = forms.CharField(label='First name', max_length=25)
    last_name = forms.CharField(label='Last name', max_length=25)
    email = forms.EmailField(label='Email')

class NewLoginIn(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, label='Password',max_length=10)# widget puts the dots
    
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True,
#     label='Email',
#     error_messages={'exists': 'User exists'})

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user