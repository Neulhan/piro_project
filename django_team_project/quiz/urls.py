from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.next),
    path('check1/', views.checking1),
    path('check2/', views.checking2),
    path('check3/', views.checking3),
]