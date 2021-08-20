from django.shortcuts import render
from .models import Cliente_jsilva


def inicio(request):
    return render(request,"index.html")


def agregar(request):
    Cliente_jsilva.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    email = request.POST['email'],
    password = request.POST['password']
    )

    return render(request,"index.html")