from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
import re

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "password1", "password2", "email", "telefono"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")

        # Validar longitud mínima
        if len(password2) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

        # Validar que contenga al menos una letra mayúscula
        if not re.search(r'[A-Z]', password2):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        # Validar que contenga al menos una letra minúscula
        if not re.search(r'[a-z]', password2):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")

        # Validar que contenga al menos un dígito
        if not re.search(r'\d', password2):
            raise ValidationError("La contraseña debe contener al menos un número.")

        # Validar que contenga al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password2):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")

        return password2

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ["username", "email", "telefono"]
