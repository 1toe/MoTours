from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        return round(precio, 2)
