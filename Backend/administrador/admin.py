from django.contrib import admin
from django.forms import ModelForm
from administrador.models import TipoMoto, ModeloMoto, Producto

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


admin.site.register(TipoMoto, TipoMotoAdmin)
admin.site.register(ModeloMoto, ModeloMotoAdmin)
admin.site.register(Producto, ProductoAdmin)
