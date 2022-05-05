from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def user(request):
    return render(request, 'base/user.html')
