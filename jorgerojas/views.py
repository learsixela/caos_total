from django.shortcuts import render,HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la aplicacion de JRojas XD")