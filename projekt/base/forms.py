from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth.forms import UsernameField

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Pseudonim"}),
            'email': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Adres Email"}),
        }
        labels = {
            'username': "Pseudonim",
            'email': "Adres Email",
        }



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]