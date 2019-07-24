from django.urls import path
from . import views


urlpatterns = [


    path('', views.home, name='home'),
    path('<slug:quiz_value>/create_quiz1', views.create_quiz1, name='create_quiz1'),
]

"""
    path('<slug:quiz_value>/view_quiz_init', views.view_quiz_init, name='view_quiz_init'),
    path('<slug:quiz_value>/view_quiz1', views.view_quiz1, name='view_quiz1'),
    path('<slug:quiz_value>/view_quiz2', views.view_quiz2, name='view_quiz2'),
    path('<slug:quiz_value>/view_quiz3', views.view_quiz3, name='view_quiz3'),
    path('<slug:quiz_value>/view_quiz4', views.view_quiz4, name='view_quiz4'),
    path('<slug:quiz_value>/view_quiz5', views.view_quiz5, name='view_quiz5'),
    path('<slug:quiz_value>/view_quiz6', views.view_quiz6, name='view_quiz6'),
    path('<slug:quiz_value>/view_quiz7', views.view_quiz7, name='view_quiz7'),
    path('<slug:quiz_value>/view_quiz8', views.view_quiz8, name='view_quiz8'),
    path('<slug:quiz_value>/view_quiz9', views.view_quiz9, name='view_quiz9'),
    path('<slug:quiz_value>/view_quiz10', views.view_quiz10, name='view_quiz10'),
    path('<slug:quiz_value>/view_quiz_result', views.view_quiz_result, name='view_quiz_result'),

    
    path('<slug:quiz_value>/create_quiz2', views.create_quiz2, name='create_quiz2'),
    path('<slug:quiz_value>/create_quiz3', views.create_quiz3, name='create_quiz3'),
    path('<slug:quiz_value>/create_quiz4', views.create_quiz4, name='create_quiz4'),
    path('<slug:quiz_value>/create_quiz5', views.create_quiz5, name='create_quiz5'),
    path('<slug:quiz_value>/create_quiz6', views.create_quiz6, name='create_quiz6'),
    path('<slug:quiz_value>/create_quiz7', views.create_quiz7, name='create_quiz7'),
    path('<slug:quiz_value>/create_quiz8', views.create_quiz8, name='create_quiz8'),
    path('<slug:quiz_value>/create_quiz9', views.create_quiz9, name='create_quiz9'),
    path('<slug:quiz_value>/create_quiz10', views.create_quiz10, name='create_quiz10'),
    path('<slug:quiz_value>/create_quiz_result', views.create_quiz_result, name='create_quiz_result'),
    """