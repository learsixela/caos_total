from django.shortcuts import render, HttpResponse


def inicio(request):
    return render(request, 'index.html')

def crear(request):
    return HttpResponse("crear")

def actualizar(request):
    return HttpResponse("actualizar")

def eliminar(request):
    return HttpResponse("eliminar")