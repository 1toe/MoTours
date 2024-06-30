from django.contrib import admin
from.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Información de usuario",
            {
                "fields": ("username", "email", "telefono"),
            },
        ),
    )
    list_display = ("username", "email", "telefono")

admin.site.register(Usuario, UsuarioAdmin)