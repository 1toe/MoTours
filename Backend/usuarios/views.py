
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import UsuarioCreationForm
import re
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import UsuarioCreationForm

class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('usuarios:login')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data["password"]
        
        # Validar longitud mínima
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        # Validar que contenga al menos una letra mayúscula
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        
        # Validar que contenga al menos una letra minúscula
        if not re.search(r'[a-z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
        
        # Validar que contenga al menos un dígito
        if not re.search(r'\d', password):
            raise ValidationError("La contraseña debe contener al menos un número.")
        
        # Validar que contenga al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")
        
        return password

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
