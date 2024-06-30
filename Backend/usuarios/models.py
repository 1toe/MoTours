from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        swappable = 'AUTH_USER_MODEL'

Usuario._meta.get_field('groups').remote_field.related_name = 'usuario_set'
Usuario._meta.get_field('user_permissions').remote_field.related_name = 'usuario_permissions_set'
