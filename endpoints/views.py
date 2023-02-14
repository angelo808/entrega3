from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

# Create your views here.

def obtenerRestaurante(request):
    if request.method == "GET":
        idRestaurante = request.GET.get("categoria")

        if idRestaurante == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        restaurantesFiltrados = []

        if idRestaurante == "-1" :
            peliculasQS = Pelicula.objects.all()
        else:
            peliculasQS = Pelicula.objects.filter(categoria__pk=idRestaurante)
        
        for p in peliculasQS:
            peliculasFiltradas.append({
                "id" : p.pk,
                "nombre" : p.nombre,
                "url" : p.url,
                "categoria" : {
                    "id" : p.categoria.pk,
                    "nombre" : p.categoria.nombre
                }
            })

        dictResponse = {
            "error": "",
            "peliculas": peliculasFiltradas
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)