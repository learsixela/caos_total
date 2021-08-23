from django.shortcuts import render, HttpResponse,redirect, get_object_or_404

from .models import Servicio
# Create your views here.
def inicio(request):
    servicios = Servicio.objects.all()
    context = {
        "servicio": "",
        "servicios":servicios,
    }
    return render(request,'israel_palma/index.html', context)

def create(request):
    Servicio.objects.create(
    servicio = request.POST['servicio'],
    descripcion = request.POST['descripcion'],
    tiempo = request.POST['tiempo'],
    costo = request.POST['costo']
    )
    return redirect('/ipalma/')

def read(request):
    return HttpResponse("read")

def update(request):
    servicio = get_object_or_404(Servicio, pk=request.POST['id'])

    errores= Servicio.objects.validaciones(request.POST)
    if len(errores) == 0:
        servicio.servicio = request.POST['servicio']
        servicio.descripcion = request.POST['descripcion']
        servicio.tiempo = request.POST['tiempo']
        servicio.costo = request.POST['costo']
        servicio.save()

    #servicio = Servicio.objects.get(id=request.POST['id'])
    context = {
        "servicio": servicio,
    }
    return render(request,'israel_palma/edit.html', context)
    return redirect('/ipalma/')

def delete(request):
    servicio = Servicio.objects.get(id=request.POST['id']).delete()
    return redirect('/ipalma/')



