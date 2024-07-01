from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class ClienteManager(BaseUserManager):
    def create_user(self, username, nombre, fecha_nacimiento, email=None, password=None):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(
            username=username,
            nombre=nombre,
            fecha_nacimiento=fecha_nacimiento,
            email=self.normalize_email(email) if email else None,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nombre, fecha_nacimiento, email=None, password=None):
        user = self.create_user(
            username=username,
            nombre=nombre,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cliente_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cliente_permissions_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )

    objects = ClienteManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'fecha_nacimiento']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=100)
    descripcion = models.TextField()
    especificaciones = models.JSONField(null=True, blank=True) 
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad}'

    def total(self):
        return self.producto.precio * self.cantidad
    
class Carrito(models.Model):
    items = models.ManyToManyField(CarritoItem)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())
