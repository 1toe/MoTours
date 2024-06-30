from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'is_active', 'is_admin')
    search_fields = ('username', 'nombre', 'email')
