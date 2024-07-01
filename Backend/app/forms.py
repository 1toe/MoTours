from django import forms
from .models import Cliente, CarritoItem
import re

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'nombre', 'fecha_nacimiento', 'telefono', 'direccion', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not re.match(r"^[a-zA-Z\s]+$", nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        if not fecha_nacimiento:
            raise forms.ValidationError("Este campo es obligatorio.")
        return fecha_nacimiento

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if not re.match(r"^\d{9}$", telefono):
            raise forms.ValidationError("El teléfono debe tener 9 dígitos numéricos.")
        return telefono

    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        if not direccion.strip():
            raise forms.ValidationError("Este campo es obligatorio.")
        return direccion

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not re.match(r"^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-\.]+$", email):
            raise forms.ValidationError("El correo electrónico no es válido.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$", password):
            raise forms.ValidationError("La contraseña no cumple los requisitos.")
        return password

class AñadirAlCarritoForm(forms.ModelForm):
    class Meta:
        model = CarritoItem
        fields = ['cantidad']
