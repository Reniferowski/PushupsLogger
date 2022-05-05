from django.contrib import admin

from .models import User, Ranking, Pushups

admin.site.register(User)
admin.site.register(Ranking)
admin.site.register(Pushups)