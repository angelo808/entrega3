from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Soporte)
admin.site.register(models.Usuario)
admin.site.register(models.UsuarioR)
admin.site.register(models.Carrito)
admin.site.register(models.Restaurante)
admin.site.register(models.Categoria)
admin.site.register(models.CategoriaPlato)
admin.site.register(models.Plato)
admin.site.register(models.Cliente)
admin.site.register(models.Pedido)
admin.site.register(models.PedidoXPlato)



