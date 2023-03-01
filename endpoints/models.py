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

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    abierto = models.BooleanField(default=True)

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

class UsuarioR(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.usuario

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
        return self.nombre


class CategoriaPlato(models.Model):
    CATEGORIA_ESTADOS = (
        ("A", "Activo"),
        ("I", "Inactivo")
    )
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=CATEGORIA_ESTADOS)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='platos')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

class PedidoC(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    platos = models.ManyToManyField(Plato, through='PedidoXPlato')

    def __str__(self):
        return self.cliente

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


class PedidoXPlato(models.Model):
    pedido = models.ForeignKey(PedidoC, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return self.pedido

