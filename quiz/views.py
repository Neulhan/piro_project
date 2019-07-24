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


def guest_q2(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p1) == int(request.GET.get('p')):
        qs.b1 = 1
        qs.save()
        print(qs.b1)
    else:
        qs.b1 = 0
        qs.save()
        print(qs.b1)

    return render(request, "guest_q2.html", {'user': queryset[0], 'id': id})


def guest_q3(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p2) == int(request.GET.get('p')):
        qs.b2 = 1
        qs.save()
    else:
        qs.b2 = 0
        qs.save()
    return render(request, "guest_q3.html", {'user': queryset[0], 'id': id})


def guest_q4(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p3) == int(request.GET.get('p')):
        qs.b3 = 1
        qs.save()
    else:
        qs.b3 = 0
        qs.save()
    return render(request, "guest_q4.html", {'user': queryset[0], 'id': id})


def guest_q5(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p4) == int(request.GET.get('p')):
        qs.b4 = 1
        qs.save()
    else:
        qs.b4 = 0
        qs.save()

    return render(request, "guest_q5.html", {'user': queryset[0], 'id': id})


def guest_q6(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p5) == int(request.GET.get('p')):
        qs.b5 = 1
        qs.save()
    else:
        qs.b5 = 0
        qs.save()

    return render(request, "guest_q6.html", {'user': queryset[0], 'id': id})


def guest_q7(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p6) == int(request.GET.get('p')):
        qs.b6 = 1
        qs.save()
    else:
        qs.b6 = 0
        qs.save()

    return render(request, "guest_q7.html", {'user': queryset[0], 'id': id})


def guest_q8(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p7) == int(request.GET.get('p')):
        qs.b7 = 1
        qs.save()
    else:
        qs.b7 = 0
        qs.save()
    return render(request, "guest_q8.html", {'user': queryset[0], 'id': id})


def guest_q9(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p8) == int(request.GET.get('p')):
        qs.b8 = 1
        qs.save()
    else:
        qs.b8 = 0
        qs.save()
    return render(request, "guest_q9.html", {'user': queryset[0], 'id': id})


def guest_q10(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p9) == int(request.GET.get('p')):
        qs.b9 = 1
        qs.save()
    else:
        qs.b9 = 0
        qs.save()

    return render(request, "guest_q10.html", {'user': queryset[0], 'id': id})


def guest_q11(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p10) == int(request.GET.get('p')):
        qs.b10 = 1
        qs.save()
    else:
        qs.b10 = 0
        qs.save()
    return render(request, "quiz/Guest_complete.html", {'user': queryset[0], 'id': id})


def guest_complete(request, id):
    queryset = User.objects.all()
    qs = Guest.objects.all()
    qs = qs.order_by('-id')
    qs = qs[0]

    queryset = queryset.filter(code=id)
    if int(queryset[0].p10) == int(request.GET.get('p')):
        qs.b10 = 1
        qs.save()
    else:
        qs.b10 = 0
        qs.save()

    qs.score = qs.b1+qs.b2+qs.b3+qs.b4+qs.b5+qs.b6+qs.b7+qs.b8+qs.b9+qs.b10
    qs.save()
    return render(request, "quiz/Guest_complete.html", {'user': queryset[0], 'score': qs})

