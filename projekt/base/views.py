from django.shortcuts import render, redirect
from .models import User, Pushups
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserRegister, PushupsForm

def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username").lower()
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
    context= {"page": page}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def registerPage(request):
    user = get_user_model()
    form = UserRegister()

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Wystąpił problem podczas zakładania konta")
    return render(request, 'base/login_register.html', {"form": form})

def home(request):
    return render(request, 'base/home.html')

def userProfile(request, pk):
    user = User.objects.get(id = pk)
    context = {'user': user}
    return render(request, 'base/user.html', context)

def ranking(request):
    return render(request, "base/ranking.html")

def kontakt(request):
    return render(request, "base/kontakt.html")

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm (request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user-profile", pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

@login_required(login_url="login")
def addPushup(request):
    form = PushupsForm()
    user = request.user

    if request.method == "POST":
        Pushups.objects.create(
            id_uzytkownika = request.user,
            powtorzenia = request.POST.get("powtorzenia"),
            seria = request.POST.get("seria"),
            )
        return redirect("user-profile", pk=user.id)
    return render(request, "base/add-pushup.html", {"form": form})