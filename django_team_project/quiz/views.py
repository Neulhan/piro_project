from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Guest







def create_quiz1(request, pk):

    return render(request,"create_quiz1.html", )


def home(request):



    User.objects.create(name= , code= ,)