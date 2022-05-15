from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name = "home"),
	path("user/", views.user, name = "user"),
	path("ranking/", views.ranking, name ="ranking"),
	path("kontakt/", views.kontakt, name ="kontakt"),
	path("login/", views.loginPage, name="login"),
	path("logout/", views.logoutUser, name="logout"),
]