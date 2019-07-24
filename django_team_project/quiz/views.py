from django.shortcuts import render
from .models import User, Guest
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, "layout.html")

def checking1(request):
    return render(request, "")

def checking2(request):
    return render(request, "quiz/make1.html")


def checking3(request):
    return render(request, "makebase.html")

def next(request):
    name = request.GET.get('name')
    code = request.GET.get('code')
    User.objects.create(name=name, code=code)

    return render(request, reverse())





