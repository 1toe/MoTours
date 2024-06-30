from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import RegistroClienteForm

def registro_cliente(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.set_password(form.cleaned_data['password'])
            cliente.save()
            return redirect("home")
    else:
        form = RegistroClienteForm()
    return render(request, "app/Formulario.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirigir a la página principal
        
        else:
            return redirect("registro")  # Redirigir a la página de registro

    return render(request, "app/login.html")

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
