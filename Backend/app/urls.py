from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('MotoAdventure', views.MotoAdventure, name='MotoAdventure'),
    path('MotoCompeticion', views.MotoCompeticion, name='MotoCompeticion'),
    path('MotoDeportiva', views.MotoDeportiva, name='MotoDeportiva'),
    path('MotoScooter', views.MotoScooter, name='MotoScooter'),
    path('MotoTouring', views.MotoTouring, name='MotoTouring'),
    path('MotoUrbana', views.MotoUrbana, name='MotoUrbana'),
]
