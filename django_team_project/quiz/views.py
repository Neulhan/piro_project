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
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p1 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create2.html", {'user': qs})


def create3(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p2 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create3.html", {'user': qs})


def create4(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p3 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create4.html", {'user': qs})


def create5(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p4 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create5.html", {'user': qs})


def create6(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p5 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create6.html", {'user': qs})


def create7(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p6 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create7.html", {'user': qs})


def create8(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p7 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create8.html", {'user': qs})


def create9(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p8 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create9.html", {'user': qs})


def create10(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p9 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "create10.html", {'user': qs})


def create11(request):
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    p = request.GET.get('p')
    qs.p10 = p
    qs.save()
    qs = User.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]
    return render(request, "quiz/User_complete.html", {'user': qs})


def guest_first(request, id):
    queryset = User.objects.all()
    queryset = queryset.filter(code=id)
    a = queryset[0].p_num
    return render(request, "quiz/Guest_layout.html", {'user': queryset[0], 'guest': a, 'id': id})


def guest_q1(request, id):
    guest = Guest.objects
    guest.name = request.GET.get('name')
    Guest.objects.create(name=guest.name)
    queryset = User.objects.all()
    queryset = queryset.filter(code=id)

    qs = User.objects.get(code=id)
    qs.p_num += 1
    qs.save()
    return render(request, "guest_q1.html", {'user': queryset[0], 'id': id})


def guest_complete(request, id):
    queryset = User.objects.all()
    queryset = queryset.filter(code=id)

    return render(request, "quiz/Guest_complete.html", {'user': queryset[0]})

