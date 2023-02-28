from django.db import models

# Create your models here.

class Categoria(models.Model):
    CATEGORIA_ESTADOS = (
        ("A", "Activo"),
        ("I", "Inactivo")
    )
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=CATEGORIA_ESTADOS)

    def __str__(self):
        return self.nombre

class Soporte(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    correo = models.CharField(max_length=25)
    tipoproblema = models.CharField(max_length=25)
    problema = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.usuario

class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    # nombre = models.CharField(max_length=25)
    # categoria = models.ForeignKey(Categoria_Pla, on_delete=models.CASCADE)
    # local = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    # descripcion = models.CharField(max_length=50)
    # valor = models.IntegerField()

    nombre = models.CharField(max_length=100)
    url = models.URLField()
    categoria = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    abierto = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOPEDIDO_ESTADOPEDIDO = (
        ("Recibido", "Recibido"),
        ("Con el repartidor", "Con el repartidor"),
        ("En camino", "En camino"),
        ("Entregado", "Entregado")
    )        

    id = models.AutoField(primary_key=True)
    local = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    codigopedido = models.CharField(max_length=25)
    estado = models.CharField(max_length=20, choices=ESTADOPEDIDO_ESTADOPEDIDO)
    plato = models.CharField(max_length=3)
    valor = models.CharField(max_length=3)


    def __str__(self):
        return self.codigopedido

