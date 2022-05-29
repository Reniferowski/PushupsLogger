from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pushups
from django import forms
from django.contrib.auth.forms import UsernameField

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "avatar"]
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
        fields = ["username", "email", "imie", "nazwisko", "wiek", "avatar", "opis"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Pseudonim"}),
            'email': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Adres Email"}),
            'imie': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Imie"}),
            'nazwisko': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Nazwisko"}),
            'wiek': forms.NumberInput(attrs={'class': 'form-control',"placeholder":"Wiek"}),
            'opis': forms.Textarea(attrs={'class': 'form-control',"placeholder":"Opis"}),
        }
        labels = {
            'username': "Pseudonim",
            'email': "Adres Email",
        }

class PushupsForm(ModelForm):
    class Meta:
        model = Pushups
        fields = ["powtorzenia", "seria"]
        labels = {
            'powtorzenia': "powtorzenia",
            'seria': "seria",
        }