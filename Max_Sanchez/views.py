from django.shortcuts import render

# Create your views here.
def inicio(request):
    render(request,'inicio.html')