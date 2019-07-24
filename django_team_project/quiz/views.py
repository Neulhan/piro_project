from django.shortcuts import render
from .models import User, Guest
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, "layout.html")


def next(request):
    name = request.GET.get('name')
    code = request.GET.get('code')
    User.objects.create(name=name, code=code)

    return render(request, reverse())





