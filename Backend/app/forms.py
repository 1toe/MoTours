from django import forms
from .models import Cliente
import re


class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if not re.match(r"^[a-zA-Z\s]+$", nombre):
            raise forms.ValidationError(
                "El nombre solo puede contener letras y espacios."
            )
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

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not re.match(
            r"^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-\.]+$", email
        ):
            raise forms.ValidationError("El correo electrónico no es válido.")
        return email

    def clean_contraseña(self):
        contraseña = self.cleaned_data["contraseña"]
        if not re.match(
            r"^(?=.*\d)(?=.*[a-z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$", contraseña
        ):
            raise forms.ValidationError("La contraseña no cumple los requisitos.")
        return contraseña
