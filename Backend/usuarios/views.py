from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import UsuarioCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('usuarios:login')


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'