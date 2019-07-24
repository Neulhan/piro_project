from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.next),
    path('create1/', views.create1, name="create1"),
    path('create2/', views.create2, name="create2"),
    path('create3/', views.create3),
    path('create4/', views.create4),
    path('create5/', views.create5),
    path('create6/', views.create6),
    path('create7/', views.create7),
    path('create8/', views.create8),
    path('create9/', views.create9),
    path('create10/', views.create10),
    path('create11/', views.create11),
]
