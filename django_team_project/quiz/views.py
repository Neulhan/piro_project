from django.shortcuts import render
from .models import User, Guest
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.


def home(request):
    return render(request, "layout.html")


def next(request):
    user = User.objects
    user.name = request.GET.get('name')
    user.code = request.GET.get('code')
    print(user.name, user.code)
    User.objects.create(name=user.name, code=user.code)
    return redirect(reverse('create1'))


def create1(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create1.html", {'user': qs})


def create2(request):
    return render(request, "create1.html", {'user': User.objects.all})

