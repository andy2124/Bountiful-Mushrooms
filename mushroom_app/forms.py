from django import forms

class NewSignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25) #
    password = forms.CharField(widget=forms.PasswordInput, label='Password',max_length=10)# widget puts the dots
    first_name = forms.CharField(label='First name', max_length=25)
    last_name = forms.CharField(label='Last name', max_length=25)
    email = forms.EmailField(label='Email')

class NewLoginIn(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, label='Password',max_length=10)# widget puts the dots
    