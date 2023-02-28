from django.urls import path
from . import views

urlpatterns = [
    path("codigopedido", views.codigopedido),
    path("buscarcodigopedido", views.buscarcodigopedido),
    path("login", views.login),
    path("restaurantes/listar", views.obtenerRestaurante),
    path("categorias/listar", views.obtenerCategorias),
    path("categorias/crear", views.registrarCategorias),
    path("soporte", views.soporte),
]