from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from .models import CategoriaPlato, Cliente, PedidoC, Plato, Usuario, Categoria, Soporte, UsuarioR
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Categoria,Restaurante,Usuario,Pedido


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

def obtenerPlato(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categoria")
        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        platosFiltrados = []

        if idCategoria == "-1" :
            platosQS = Plato.objects.all()
        else:
            platosQS = Plato.objects.filter(categoria__pk=idCategoria)

        for r in platosQS:
            platosFiltrados.append({
                "id" : r.pk,
                "nombre" : r.nombre,
                "url": r.url,
                "precio" : r.precio,
                "categoria" : {
                    "id": r.categoria.pk,
                    "nombre" : r.categoria.nombre
                },
                "restaurante" : r.restaurante 
            })
       
        dictResponse = {
            "error": "",
            "platos": list(platosFiltrados)
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
def pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        email = data.get('email')
        restaurante_id= data.get('restaurante')
        
        
        cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
        cliente.save()

        restaurante = Restaurante.objects.get(id=restaurante_id)

        pedido = Pedido(cliente=cliente, restaurante=restaurante, fecha_pedido=timezone.now())
        pedido.save()

        return JsonResponse({'message': 'Pedido creado con exito'})

        
        

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

def codigopedido(request):
    if request.method == "GET":

        codigopedidos = PedidoC.objects.all()  
        listadepedidos = []

        for v in codigopedidos: 
            listadepedidos.append({
                "id": v.id,
                "codigopedido":v.codigopedido,
                "estado": v.estado,
                "plato": v.plato,
                "valor": v.valor,

            })

        dictOK = {
            "error" : "",
            "codigopedido" : listadepedidos
        }
        return HttpResponse(json.dumps(dictOK))
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)      

@csrf_exempt
def buscarcodigopedido(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        codigopedido = dictDataRequest['codigopedido']


        codigopedidos = PedidoC.objects.all()

        for u in codigopedidos: 
            if u.codigopedido == codigopedido:
                dictOK = {
                    'error': '',
                    'codigopedidoid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe un pedido con ese codigo'
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
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        tipoproblema = data.get('tipoproblema')
        problema = data.get('problema')

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
            'error': 'peticion no existe'
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
def loginR(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest['usuario']
        password = dictDataRequest['password']

        usuarios = UsuarioR.objects.all()

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

def obtenerCategoriasPlatos(request):
    if request.method == "GET":
        listaCategoriasQuerySet = CategoriaPlato.objects.filter(estado="A")
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

@csrf_exempt
def registrarCategoriasPlatos (request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictCategoria = json.loads(request.body)
    nombre = dictCategoria["nombre"]
    estado = dictCategoria["estado"]

    cat = CategoriaPlato(nombre=nombre, estado=estado)
    cat.save() # Registra en la bd la nueva categoria

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))


