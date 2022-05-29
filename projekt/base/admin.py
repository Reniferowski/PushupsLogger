from django.contrib import admin

from .models import User, Ranking, Pushups


admin.site.register(Ranking)
admin.site.register(Pushups)
@admin.register(User)
class userAdmin(admin.ModelAdmin):
    fields = ("username","imie", "nazwisko", "email", "opis", "avatar")
    list_display = ("username", "nazwisko", "email",)
    ordering = ("nazwisko",)
    search_fields = ("nazwisko", "email",)