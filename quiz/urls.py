from django.urls import path, re_path
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
    re_path(r'^(?P<id>\d+)/$', views.guest_first),
    re_path(r'^(?P<id>\d+)/q1/$', views.guest_q1),
    re_path(r'^(?P<id>\d+)/guest_q2/$', views.guest_q2),
    re_path(r'^(?P<id>\d+)/guest_q3/$', views.guest_q3),
    re_path(r'^(?P<id>\d+)/guest_q4/$', views.guest_q4),
    re_path(r'^(?P<id>\d+)/guest_q5/$', views.guest_q5),
    re_path(r'^(?P<id>\d+)/guest_q6/$', views.guest_q6),
    re_path(r'^(?P<id>\d+)/guest_q7/$', views.guest_q7),
    re_path(r'^(?P<id>\d+)/guest_q8/$', views.guest_q8),
    re_path(r'^(?P<id>\d+)/guest_q9/$', views.guest_q9),
    re_path(r'^(?P<id>\d+)/guest_q10/$', views.guest_q10),
    re_path(r'^(?P<id>\d+)/guest_complete/$', views.guest_complete),


]
