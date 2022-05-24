from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name = "home"),
	path("profile/<str:pk>", views.userProfile, name = "user-profile"),
	path("ranking/", views.ranking, name ="ranking"),
	path("kontakt/", views.kontakt, name ="kontakt"),
	path("login/", views.loginPage, name="login"),
	path("logout/", views.logoutUser, name="logout"),
	path("register/", views.registerPage, name="register"),
	path("update-user/", views.updateUser, name="update-user")
]