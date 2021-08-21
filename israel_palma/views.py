from django.shortcuts import render, HttpResponse,redirect
from .models import Servicio
# Create your views here.
def inicio(request):
    servicios = Servicio.objects.all()
    context = {
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
    return HttpResponse("update")

def delete(request):
    servicio = Servicio.objects.get(id=request.POST['id'])
    print(servicio)
    servicio.delete()
    return redirect('/ipalma/')



