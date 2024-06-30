from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from .models import Cliente
from .models import CarritoItem

def agregar_al_carrito(request, producto, precio):
    item, created = CarritoItem.objects.get_or_create(producto=producto, precio=precio)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = CarritoItem.objects.all()
    total = sum(item.total() for item in carrito)
    return render(request, 'app/carrito.html', {'carrito': carrito, 'total': total})
@login_required
def clientes_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/clientes_lista.html', {'clientes': clientes})

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_lista')
    else:
        form = ClienteForm()
    
    return render(request, 'app/Formulario.html', {'form': form})

@csrf_protect
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('clientes_lista')
        else:
            return render(request, 'app/login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return redirect("home")

def home(request):
    return render(request, "app/home.html")

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
