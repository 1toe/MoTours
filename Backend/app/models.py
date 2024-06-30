from django.db import models
from django.contrib.auth.models import User



class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre
    
class CarritoItem(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.producto} - {self.cantidad}'

    def total(self):
        return self.precio * self.cantidad
