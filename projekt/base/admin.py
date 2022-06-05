from django.contrib import admin

from .models import User, Ranking, Pushups


admin.site.register(Ranking)
@admin.register(User)
class userAdmin(admin.ModelAdmin):
    fields = ("username","imie", "nazwisko", "email", "opis", "avatar")
    list_display = ("username", "nazwisko", "email",)
    ordering = ("nazwisko",)
    search_fields = ("nazwisko", "email",)

@admin.register(Pushups)
class pushupsAdmin(admin.ModelAdmin):
    fields = ("powtorzenia", "seria")
    list_display = ("user", "data")
    list_filter = ("data",)
    ordering = ("user",)
    search_fields = ("data", "user")
