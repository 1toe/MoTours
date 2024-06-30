from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TipoMoto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.nombre)


class ModeloMoto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tipo = models.ForeignKey(TipoMoto, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Producto(models.Model):
    modelo = models.ForeignKey(ModeloMoto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.descripcion}"


from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioStandard(AbstractUser):
    # Añade campos adicionales si es necesario
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=[
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ], default='standard')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_standard_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_standard_permissions',
        blank=True,
    )