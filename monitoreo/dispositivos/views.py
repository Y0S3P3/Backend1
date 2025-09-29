from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    contexto = {"nombre": "Profe javi"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "sensor 2", "valor": 200},
        {"nombre": "sensor 3", "valor": 300}
    ]
    return render(request, "dispositivos/inicio.html", {"contexto":contexto, "productos": productos})
