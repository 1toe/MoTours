from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


app_name = "administrador"
urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("administrador:menu")),
        name="logout",
    ),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("productos/agregar/", views.agregar_producto, name="agregar_producto"),
    path(
        "productos/<int:id>/editar/",
        views.modificar_producto,
        name="modificar_producto",
    ),
    path(
        "productos/<int:producto_id>/eliminar/",
        views.eliminar_producto,
        name="eliminar_producto",
    ),
]
