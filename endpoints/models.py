from django.db import models

# Create your models here.
class Carrito(models.Model):
    CARRITO_ESTADOS = (
        ("A", "Activo"),
        ("I", "Inactivo") #inactivo es cuando ya se realizo el pedido
                        #(el pago se hizo y el contenido del carrito pasa a ser compra)
    )
    contenido = models.CharField(max_length=50)
    valor = models.CharField(max_length=3)
    estado = models.CharField(max_length=1, choices=CARRITO_ESTADOS)

    def __str__(self):
        return self.contenido


class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    CATEGORIA_ESTADOS = (
        ("A", "Activo"),
        ("I", "Inactivo")
    )
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=CATEGORIA_ESTADOS)

    def __str__(self):
        return self.nombre