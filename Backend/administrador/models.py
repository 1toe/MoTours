from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

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

class AdminManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(
            username=username,
            email=self.normalize_email(email) if email else None,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )

    objects = AdminManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
