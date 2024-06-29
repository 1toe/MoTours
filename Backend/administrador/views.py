from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Producto
from .forms import ProductoForm


@login_required(login_url="/administrador/accounts/login/")
def menu(request):
    context = {}
    return render(request, "administrador/menu.html", context)


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


@login_required
@permission_required("administrador.view_producto", raise_exception=True)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "administrador/productoLista.html", {"productos": productos})


@login_required
@permission_required("administrador.add_producto")
def agregar_producto(request):
    data = {"form": ProductoForm()}
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect("administrador:lista_productos")
        else:
            data["form"] = formulario
    return render(request, "administrador/agregarProducto.html", data)


@login_required
@permission_required("administrador.change_producto", raise_exception=True)
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente.")
            return redirect("administrador:lista_productos")
    else:
        formulario = ProductoForm(instance=producto)
    return render(
        request,
        "administrador/modificarProducto.html",
        {"form": formulario, "producto": producto},
    )


@login_required
@permission_required("administrador.delete_producto", raise_exception=True)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect("administrador:lista_productos")
