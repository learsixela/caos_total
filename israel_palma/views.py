from django.shortcuts import render, HttpResponse,redirect, get_object_or_404

from .models import Servicio

from django.views.generic import ListView, View


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


def getServicio(request):
    servicio = Servicio.objects.get(id=request.POST['id'])
    context = {
        "servicio": servicio
    }
    return render(request,'israel_palma/edit.html', context)


def update(request):
    servicio = Servicio.objects.get(id=request.POST['id'])

    errores= Servicio.objects.validaciones(request.POST)
    
    if len(errores) == 0:
        servicio.servicio = request.POST['servicio']
        servicio.descripcion = request.POST['descripcion']
        servicio.tiempo = request.POST['tiempo']
        servicio.costo = request.POST['costo']
        servicio.save()
    
    return redirect('/ipalma/')


def delete(request):
    servicio = Servicio.objects.get(id=request.POST['id']).delete()
    return redirect('/ipalma/')


def generarPdf(request):
    servicios = Servicio.objects.all()
    context = {
        'titulo': "Lista de Servicios",
        "servicio": "",
        "object_list": servicios,
    }

    return render(request, 'israel_palma/listaServicios.html', context)


class ServiciosListView(ListView):
    model = Servicio
    template_name = 'israel_palma/listaServicios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['titulo'] = "Lista de Servicios"
        return context