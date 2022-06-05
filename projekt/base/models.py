from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    imie = models.CharField(max_length=30, null = True, blank = True)
    nazwisko = models.CharField(max_length=35, null = True, blank = True)
    first_name = None
    last_name= None
    wiek = models.IntegerField(null = True, blank = True)
    email = models.EmailField(unique=True, null = True)
    avatar = models.ImageField(null=True, default="avatar.webp")
    opis = models.TextField(max_length=250, null = True, blank = True)

class Pushups(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="pushups")
    data = models.DateTimeField(auto_now_add=True)
    powtorzenia = models.IntegerField()
    seria = models.IntegerField()

    class Meta:
        verbose_name_plural = "Pushups"

class Ranking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    sumaPowt = models.IntegerField()
    iloscSerii = models.IntegerField()