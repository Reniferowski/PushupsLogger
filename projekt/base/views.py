from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("usesrname")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Nie ma takiego użytkownika")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Błędna nazwa użytkownika lub hasło")
    context= {}
    return render(request, "base/login.html", context)

def logoutUser(request):
    logout(request)
    return rediret("home")

def home(request):
    return render(request, 'base/home.html')

def user(request, pk):
    user = User.objects.get(id = pk)
    context = {'user': user}
    return render(request, 'base/user.html', context)

def ranking(request):
    return render(request, "base/ranking.html")

def kontakt(request):
    return render(request, "base/kontakt.html")