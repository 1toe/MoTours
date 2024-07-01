from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("app.urls")),
    path("administrador/", include("administrador.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('MotoAdventure', views.MotoAdventure, name='MotoAdventure'),
    path('MotoCompeticion', views.MotoCompeticion, name='MotoCompeticion'),
    path('MotoDeportiva', views.MotoDeportiva, name='MotoDeportiva'),
    path('MotoScooter', views.MotoScooter, name='MotoScooter'),
    path('MotoTouring', views.MotoTouring, name='MotoTouring'),
    path('MotoUrbana', views.MotoUrbana, name='MotoUrbana'),
    path('tienda/', views.tienda, name='tienda'),  # Nueva URL para la tienda
    path('carrito/', views.carrito, name='carrito'),  # Nueva URL para el carrito
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
