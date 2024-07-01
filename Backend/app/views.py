from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroClienteForm, AñadirAlCarritoForm
from .models import Producto, Carrito, CarritoItem
from django.shortcuts import redirect, get_object_or_404
from .models import Producto
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
    return render(request, "app/home.html")



def MotoAdventure(request):
    productos_adventure = Producto.objects.filter(tipo='Adventure')
    return render(request, "app/MotoAdventure.html", {'productos': productos_adventure})


def Formulario(request):
    return render(request, "app/Formulario.html")

def MotoCompeticion(request):
    return render(request, "app/MotoCompeticion.html")

def MotoDeportiva(request):
    return render(request, "app/MotoDeportiva.html")

def MotoScooter(request):
    return render(request, "app/MotoScooter.html")

def MotoTouring(request):
    return render(request, "app/MotoTouring.html")

def MotoUrbana(request):
    return render(request, "app/MotoUrbana.html")

def tienda(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'app/tienda.html', context)

def carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    carrito_items = []

    for producto in productos:
        cantidad = carrito[str(producto.id)]
        carrito_items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': producto.precio * cantidad
        })

    total = sum(item['subtotal'] for item in carrito_items)
    context = {
        'carrito_items': carrito_items,
        'total': total
    }
    return render(request, 'app/carrito.html', context)
def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'app/tienda.html', {'productos': productos})
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('carrito')
def ver_carrito(request):
    carrito = CarritoItem.objects.all()
    total = sum(item.total() for item in carrito)
    return render(request, 'app/carrito.html', {'carrito': carrito, 'total': total})