from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'fecha_nacimiento', 'telefono', 'direccion', 'email', 'contraseña']

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Cliente.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("El email ya existe en la base de datos.")
        return email
    

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if not re.match(r"^[a-zA-Z\s]+$", nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data["fecha_nacimiento"]
        if not fecha_nacimiento:
            raise forms.ValidationError("Este campo es obligatorio.")
        return fecha_nacimiento

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"]
        if not re.match(r"^\d{9}$", telefono):
            raise forms.ValidationError("El teléfono debe tener 9 dígitos numéricos.")
        return telefono

    def clean_direccion(self):
        direccion = self.cleaned_data["direccion"]
        if not direccion.strip():
            raise forms.ValidationError("Este campo es obligatorio.")
        return direccion

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
