from django.shortcuts import render
from .models import ClienteAlvaro


# Create your views here.
def index(request):
    return render(request, "index.html")

def add(request):
    ClienteAlvaro.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    email = request.POST['email'],
    password = request.POST['password']
    )
    return render(request,"index.html")