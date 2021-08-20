from django.shortcuts import render, HttpResponse
from .models import Cliente

def inicio(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, "index.html")

""" def agregar(request):
    # request.post['parametro']
    # capturando los parametros enviados por el formulario
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dv = request.POST['dv'],
    )
    return render(request, "index.html")

def leer(request):
    return render(request, "index.html")


def actualizar(request):
    return render(request, "index.html")


def eliminar(request):
    return render(request, "index.html") """

