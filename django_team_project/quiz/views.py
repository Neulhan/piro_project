from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Guest


def home(request):
    print('test')
    if request.method == "GET":
        name = request.get('name')
        code = request.get('code')
        print(name, code)
        next_url = 'http://127.0.0.1:8000/quiz/' + 'code' + '/create_quiz1'
        return render(request, 'create_quiz1.html', {'name':name, 'code':code})
    else:
    return render(request, "index.html", {'next_url': next_url})


def create_quiz1(request, quiz_value):

    return render(request, "create_quiz1.html", {})


"""

    
"""