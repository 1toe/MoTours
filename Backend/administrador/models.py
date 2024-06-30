from django.db import models

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
