from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login),
    path("restaurantes/listar", views.obtenerRestaurante),
    path("categorias/listar", views.obtenerCategorias)
]