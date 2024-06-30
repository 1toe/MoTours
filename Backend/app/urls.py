from django.urls import path, include
from . import views 
from .views import *

urlpatterns = [
    path("home", views.home, name="home"),
    path('login/', login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),
    path('clientes_lista/', views.clientes_lista, name='clientes_lista'),
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path("MotoAdventure", views.MotoAdventure, name="MotoAdventure"),
    path("MotoCompeticion", views.MotoCompeticion, name="MotoCompeticion"),
    path("MotoDeportiva", views.MotoDeportiva, name="MotoDeportiva"),
    path("MotoScooter", views.MotoScooter, name="MotoScooter"),
    path("MotoTouring", views.MotoTouring, name="MotoTouring"),
    path("MotoUrbana", views.MotoUrbana, name="MotoUrbana"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('tienda/', views.tienda, name='tienda'),  # Ruta para la tienda
    path('agregar_al_carrito/<str:producto>/<int:precio>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
]

