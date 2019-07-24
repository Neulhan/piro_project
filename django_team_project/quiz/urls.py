from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.next),
    path('create1/', views.create1,  name="create1"),
]
