from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    imie = models.CharField(max_length=30, null = True)
    nazwisko = models.CharField(max_length=35, null = True)
    first_name = None
    last_name= None
    wiek = models.IntegerField(null = True)

class Pushups(models.Model):
    id_uzytkownika = models.ForeignKey(User, on_delete = models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    powtorzenia = models.IntegerField()
    seria = models.IntegerField()

class Ranking(models.Model):
    id_uzytkownika = models.ForeignKey(User, on_delete = models.CASCADE)
    sumaPowt = models.IntegerField()
    iloscSerii = models.IntegerField()