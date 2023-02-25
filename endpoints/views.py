from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from .models import Usuario, Categoria, Soporte
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Categoria, Carrito, Restaurante,Usuario


# Create your views here.

def obtenerRestaurante(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categoria")

        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        restaurantesFiltrados = []

        if idCategoria == "-1" :
            restaurantesQS = Restaurante.objects.all()
        else:
            restaurantesQS = Restaurante.objects.filter(categoria__pk=idCategoria)

        for r in restaurantesQS:
            restaurantesFiltrados.append({
                "id" : r.pk,
                "nombre" : r.nombre,
                "url" : r.url,
                "categoria" : {
                    "id": r.categoria.pk,
                    "nombre" : r.categoria.nombre
                },
                "abierto" : r.abierto 
            })
       
        dictResponse = {
            "error": "",
            "restaurantes": list(restaurantesFiltrados)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def codigopedido(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        codigopedido = dictDataRequest["codigopedido"]

        # TODO: Consultar a base de datos
        if codigopedido == "asd":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error codigo de pedido
            dictError = {
                "error": "Error en codigo de pedido"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)     
    
@csrf_exempt
def soporte(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        nombre = dictDataRequest['nombreo']
        correo = dictDataRequest['correo']
        tipoproblema = dictDataRequest['tipoproblema']
        problema = dictDataRequest['problema']

        listaSoportes = Soporte.objects.all()

        for u in listaSoportes:

            newSoporte = Soporte(nombre=nombre, correo=correo, tipoproblema=tipoproblema, problema=problema)
            newSoporte.save()
            dictOK = {
                    'error': ''
                }
            return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            'error': 'peticio no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest['usuario']
        password = dictDataRequest['password']

        usuarios = Usuario.objects.all()

        for u in usuarios: 
            if u.usuario == usuario and u.password == password:
                dictOK = {
                    'error': '',
                    'userid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe esa cuenta'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


@csrf_exempt           
def soporte(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        nombre = dictDataRequest["nombre"]
        correo = dictDataRequest["correo"]
        tipoproblema = dictDataRequest["tipoproblema"]
        problema = dictDataRequest["problema"]

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


def obtenerCarrito(request):
    if request.method == "GET":
        listaCarritoQuerySet = Carrito.objects.filter(estado="A")
        listaCarrito = []
        for c in listaCarritoQuerySet:
            listaCarrito.append({
                "id" : c.id,
                "contenido" : c.contenido,
                "valor":c.valor
            })

        dictOK = {
            "error" : "",
            "carrito" : listaCarrito,
            "valor" : listaCarrito
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


def obtenerCategorias(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoria.objects.filter(estado="A")
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id" : c.id,
                "nombre" : c.nombre
            })

        dictOK = {
            "error" : "",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def registrarCategorias (request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictCategoria = json.loads(request.body)
    nombre = dictCategoria["nombre"]
    estado = dictCategoria["estado"]

    cat = Categoria(nombre=nombre, estado=estado)
    cat.save() # Registra en la bd la nueva categoria

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))




