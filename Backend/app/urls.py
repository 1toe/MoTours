from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path('clientes_lista/', views.clientes_lista, name='clientes_lista'),
    path('registro/', views.registro_cliente, name='Formulario'),
    path("MotoAdventure", views.MotoAdventure, name="MotoAdventure"),
    path("MotoCompeticion", views.MotoCompeticion, name="MotoCompeticion"),
    path("MotoDeportiva", views.MotoDeportiva, name="MotoDeportiva"),
    path("MotoScooter", views.MotoScooter, name="MotoScooter"),
    path("MotoTouring", views.MotoTouring, name="MotoTouring"),
    path("MotoUrbana", views.MotoUrbana, name="MotoUrbana"),
    path("accounts/", include("django.contrib.auth.urls")),
]

