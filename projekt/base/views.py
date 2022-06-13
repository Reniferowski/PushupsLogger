from django.shortcuts import render, redirect
from .models import User, Pushups
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserRegister, PushupsForm
from django.db.models import Count, Q, Sum
from datetime import datetime, timedelta
from django.utils import timezone

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

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
    pushups = user.pushups.all()
    context = {'user': user, 'pushups': pushups}
    return render(request, 'base/user.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm (request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.username = user.username.lower()
            form.save()
            return redirect("user-profile", pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

@login_required(login_url="login")
def addPushup(request):
    form = PushupsForm()
    user = request.user
    now = timezone.now()
    if(user.dzien == None or user.dzien.date() < now.date()):
       user.limit = False
    else:
        user.limit = True
    if(user.limit == False):
        if request.method == "POST":
            Pushups.objects.create(
                user = request.user,
                powtorzenia = request.POST.get("powtorzenia"),
                seria = request.POST.get("seria"),
                )
            user.limit = True
            user.dzien = datetime.now()
            user.save()
            return redirect("user-profile", pk=user.id)
    else:
        messages.error(request, "Dodałeś już dzisiaj trening")
        return redirect("user-profile", pk=user.id)
    return render(request, "base/add-pushup.html", {"form": form})

def ranking(request):
    now = datetime.now()
    data = (now - timedelta(days=now.weekday())).replace(hour=0,minute=0,second=0,microsecond=0)
    dzien = (now - timedelta(days=now.day-1)).replace(hour=0,minute=0,second=0,microsecond=0)
    users = User.objects.annotate(pushupRecord = Sum("pushups__powtorzenia", filter = Q(pushups__data__gte=data))).order_by('-pushupRecord')[:5]
    usersMonth = User.objects.annotate(pushupMonth = Sum("pushups__seria", filter = Q(pushups__data__gte=dzien))).order_by('-pushupMonth')[:3]
    context = {'users': users, 'usersMonth': usersMonth}
    return render(request, "base/ranking.html", context)

def gen_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize = letter, bottomup = 0)
    c.setTitle("Zestawienie Treningów")
    c.setFont("Helvetica", 14)
    

    user = request.user
    pushups = user.pushups.all()

    c.drawString(105,100,
        "Zestawienie treningow uzytkownika "+
        str(user.username)+
        " na dzien "+str(datetime.today().strftime("%d.%m.%Y"))
    )

    lines = [
        ["Data Treningu", "Powtorzenia", "Serie"],
    ]

    push = 0
    series = 0

    for pushup in pushups:
        p = [pushup.data.strftime("%d.%m.%Y"), str(pushup.powtorzenia), str(pushup.seria)]
        push += pushup.powtorzenia
        series += pushup.seria
        lines.append(p)

    lines.reverse()

    style = [
        ('GRID', (0,1), (-1,-1), 1, (0,0,0)),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTSIZE', (0, 0), (-1,-1), 18),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold')
    ]

    t = Table(lines, colWidths=[150,150,150], style=style)
    t.wrapOn(c, 80, 160)
    t.drawOn(c, 80, 160)

    c.drawString(105,450,"Do tej pory zrobiles: ")
    c.drawString(105,470, str(push) + " pompek! ")
    c.drawString(105,490, str(series) + " serii! ")

    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=False, filename="Zestawienie_Treningow_"+str(user.username)+".pdf")
