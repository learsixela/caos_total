from django.shortcuts import render, HttpResponse

from .models import Registro

# Create your views here.


def inicio(request):
	# return HttpResponse("this is the equivalent of @app.route('/')!")
	return render(request, "index.html")


def agregar(request):
	Registro.objects.create(
	nombre=request.POST['nombre'],
	apellido=request.POST['apellido'],
	email=request.POST['email'],
	password=request.POST['password'],
	return render(request, "index.html"))

def leer(request):
	registros=Registro.objects.all()
	return render(request, "index.html")

def actualizar(request):
	id=request.POST['id']
	registro=Registro.objects.get(id=id)

	errores=Registro.objects.validador_registro(request.POST)

	if len(registro) > 0:
		registro.nombre=request.POST['nombre']
		registro.apellido=request.POST['apellido']
		registro.email=request.POST['email']
		registro.password=request.POST['password']
