from django.shortcuts import render
from .models import Cliente


def inicio(request):
    return render(request,"index.html")


def agregar(request):
    #request.post['parametro']
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    email = request.POST['email']
    )

    return render(request,"index.html")