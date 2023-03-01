from django.urls import path
from . import views

urlpatterns = [
    path("codigopedido", views.codigopedido),
    path("buscarcodigopedido", views.buscarcodigopedido),
    path("login", views.login),
    path("loginR", views.loginR),
    path("restaurantes/listar", views.obtenerRestaurante),
    path("categorias/listar", views.obtenerCategorias),
    path("platos/categorias", views.obtenerCategoriasPlatos),
    path("categorias/crear", views.registrarCategorias),
    path("platos/listar ", views.obtenerPlato),
    path("soporte", views.soporte),
]