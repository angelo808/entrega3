from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Usuario)
admin.site.register(models.Restaurante)
admin.site.register(models.Categoria)

