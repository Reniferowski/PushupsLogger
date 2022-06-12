from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.home, name = "home"),
	path("profile/<str:pk>", views.userProfile, name = "user-profile"),
	path("ranking/", views.ranking, name ="ranking"),
	path("login/", views.loginPage, name="login"),
	path("logout/", views.logoutUser, name="logout"),
	path("register/", views.registerPage, name="register"),
	path("update-user/", views.updateUser, name="update-user"),
	path("add-pushup/", views.addPushup, name="add-pushup"),
	path("gen_pdf/", views.gen_pdf, name="gen_pdf")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)