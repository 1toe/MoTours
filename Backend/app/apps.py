from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
from django.shortcuts import render

def registro_usuario_standard(request):
    return render(request, 'registro_usuario_standard.html')