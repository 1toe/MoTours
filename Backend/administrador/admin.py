from django.contrib import admin
from django.forms import ModelForm
from administrador.models import TipoMoto, ModeloMoto, Producto, UsuarioStandard

# Register your models here.


class TipoMotoAdmin(admin.ModelAdmin):
    pass


class ModeloMotoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo")


class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Modelo y Descripción",
            {
                "fields": ("modelo", "descripcion"),
            },
        ),
        (
            "Precio y Stock",
            {
                "fields": ("precio", "stock"),
                "classes": ("collapse",),
            },
        ),
        (
            "Imagen",
            {
                "fields": ("imagen",),
            },
        ),
    )


class UsuarioStandardAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email")


admin.site.register(TipoMoto, TipoMotoAdmin)
admin.site.register(ModeloMoto, ModeloMotoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(UsuarioStandard, UsuarioStandardAdmin)