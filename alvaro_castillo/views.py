from django.shortcuts import render
from .models import Pizza


# Create your views here.
def index(request):
    return render(request, "alvaro_castillo/index.html")

def add(request):
    Pizza.objects.create(
    nombre = request.POST['nombre'],
    ingredientes = request.POST['ingredientes'],
    valor = request.POST['valor'],
    )
    return render(request,"alvaro_castillo/index.html")

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass