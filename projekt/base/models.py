from django.db import models

class User(models.Model):
    id_uzytkownika = models.BigAutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=35)
    pseudonim = models.CharField(max_length=20)
    wiek = models.IntegerField()

class Pushups(models.Model):
    id_uzytkownika = models.ForeignKey(User, on_delete = models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    powtorzenia = models.IntegerField()
    seria = models.IntegerField()

class Ranking(models.Model):
    id_uzytkownika = models.ForeignKey(User, on_delete = models.CASCADE)
    sumaPowt = models.IntegerField()
    iloscSerii = models.IntegerField()