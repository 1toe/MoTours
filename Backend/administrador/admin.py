from django.contrib import admin
from .models import Admin, TipoMoto, ModeloMoto, Producto

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin')
    search_fields = ('username', 'email')

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
