from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .models import Categoria


# /endpoints/login
@csrf_exempt
def login(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        # TODO: Consultar a base de datos
        if usuario == "pw" and password == "123":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def obtenerRestaurante(request):
    
    if request.method == "GET":
        categoria = request.GET.get("categoria")

        if categoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query parameter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
    
        restaurantes = [
            {
                "id": 1,
                "nombre": "Starbucks",
                "url": "https://media.revistagq.com/photos/5d5d383031110c000879872d/1:1/w_1080,h_1080,c_limit/logo-starbucks.jpg",
                "categoria": 1,
            },
            {
                "id": 2,
                "nombre": "Bembos",
                "url": "https://brandemia.org/sites/default/files/sites/default/files/bembos_burger_despues.jpg",
                "categoria": 2,
            },
            {
                "id": 3,
                "nombre": "Listo",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0qb3Wgq_D-CAy9MLiRWrtPqV8fE42OFgxcGrxZnXt&s",
                "categoria": 3,
            },
            {
                "id": 4,
                "nombre": "MrSushi",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyx7-qakbPo8qao2HfVdmyW0Siar-BnUpUlvapwrI&s",
                "categoria": 2,
            },
            {
                "id": 5,
                "nombre": "Nevera Fit",
                "url": "https://media.licdn.com/dms/image/C4E0BAQEHx4OUHL0xVA/company-logo_200_200/0/1646418799033?e=2147483647&v=beta&t=BUIXtFelPC4U0umbGZK4WiDQV7XDZ-ha86SHYS7MxjQ",
                "categoria": 4,
            },
            {
                "id": 6,
                "nombre": "Chifa Express",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsc9Mz_rp1iM8CGdQX3Z284fHXZ3Q0lt2n77PQMuepRQ&s",
                "categoria": 2,
            },
            {
                "id": 7,
                "nombre": "Marianne",
                "url": "data:image/jpeg;base64,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",
                "categoria": 5,
            }
            
        ]

        
        restaurantesFiltrados = []
        if categoria == "-1":
            #No se debe filtrar nada
            restaurantesFiltrados = restaurantes
        else:
            for r in restaurantes:
                if r["categoria"] == (categoria):
                    restaurantesFiltrados.append(r)

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