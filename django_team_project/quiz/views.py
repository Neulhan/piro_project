from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Guest


def home(request):
    return render(request, "index.html")


def create_quiz1(request, quiz_value):

    return render(request, "create_quiz1.html", {})


"""

    
"""