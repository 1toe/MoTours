from django import forms
from .models import UsuarioStandard
from administrador.models import (
    Producto,
)  # Importación absoluta desde administrador.models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        return round(precio, 2)

class RegistroUsuarioStandardForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UsuarioStandard
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password_confirm