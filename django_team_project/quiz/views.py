from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Guest







def create_quiz1(request, pk):

    return render(request,"create_quiz1.html", )


def home(request):
    get = request.GET.get('name', 'code')

    User.objects.create(name=get.name, code=get.code)

    return render(request, "index.html")