from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    contexto = {"nombre": "Profe javi"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "sensor 2", "valor": 200},
        {"nombre": "sensor 3", "valor": 300}
    ]
    return render(request, "dispositivos/inicio.html", {"contexto":contexto, "productos": productos})



@login_required
def dashboard(request):
    return render(request, "dispositivos/dashboard.html")

# devices/views.py (ejemplo)
from .models import Device

@login_required
def devices_list(request):
    org = request.user.userprofile.organization
    qs = Device.objects.filter(organization=org).select_related("category", "zone")
    return render(request, "devices/list.html", {"devices": qs})

