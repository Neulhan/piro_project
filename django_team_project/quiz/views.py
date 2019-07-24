from django.shortcuts import render
from .models import User, Guest
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, "layout.html")

def checking1(request):
    return render(request, "quiz/create1.html")

def checking2(request):
    return render(request, "quiz/create2.html")


def checking3(request):
    return render(request, "quiz/create3.html")

def next(request):
    name = request.GET.get('name')
    code = request.GET.get('code')
    User.objects.create(name=name, code=code)

    return render(request, reverse())





