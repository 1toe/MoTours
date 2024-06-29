from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import RegistroClienteForm


# Create your views here.


def registro_cliente(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistroClienteForm()
    return render(request, "app/Formulario.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        contraseña = request.POST.get("contraseña")

        user = authenticate(request, username=email, password=contraseña)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "username": user.username})
        else:
            return JsonResponse({"success": False, "error": "Credenciales inválidas"})

    return JsonResponse({"success": False, "error": "Método no permitido"})


def logout_view(request):
    logout(request)
    return redirect("home")


def home(request):
    context = {}
    return render(request, "app/home.html", context)


def MotoAdventure(request):
    context = {}
    return render(request, "app/MotoAdventure.html", context)


def Formulario(request):
    context = {}
    return render(request, "app/Formulario.html", context)


def MotoCompeticion(request):
    context = {}
    return render(request, "app/MotoCompeticion.html", context)


def MotoDeportiva(request):
    context = {}
    return render(request, "app/MotoDeportiva.html", context)


def MotoScooter(request):
    context = {}
    return render(request, "app/MotoScooter.html", context)


def MotoTouring(request):
    context = {}
    return render(request, "app/MotoTouring.html", context)


def MotoUrbana(request):
    context = {}
    return render(request, "app/MotoUrbana.html", context)
