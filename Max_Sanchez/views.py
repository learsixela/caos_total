from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.
def inicio(request):
    render(request,'inicio.html')

def agregar(request):
    Producto.objects.create(
    
    
    )