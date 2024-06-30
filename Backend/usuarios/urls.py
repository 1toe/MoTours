from django.urls import path
from .views import CustomLoginView, RegistroUsuarioView

app_name = 'usuarios'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegistroUsuarioView.as_view(), name='register'),
]
