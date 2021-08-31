from django.shortcuts import render
from .models import Elemento

# Create your views here.
def start(request):
    return render(request, "index-dmix.html")

def productos(request):
    return render(request, "david_mix/index.html")

def register(request):
    Elemento.objects.create(
    nombre = request.POST['nombre'],
    descripcion = request.POST['descripcion'],
    precio = request.POST['precio'],
    peso = request.POST['peso']
    )
    return render(request, "david_mix/index.html")