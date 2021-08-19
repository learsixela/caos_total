from django.shortcuts import render, HttpResponse

from .models import Cliente

def inicio(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, "index.html")

def agregar(request):
    # request.post['parametro']
    # capturando los parametros enviados por el formulario
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dv = request.POST['dv'],
    email = request.POST['email'],
    password = request.POST['password'],
    direccion = request.POST['direccion']
    )
    return render(request, "index.html")

def leer(request):
    # el tipo de variable es definida por el contenido
    # select * from cliente 
    clientes = Cliente.objects.all()
    return render(request, "index.html")

# render pendiente***
def actualizar(request):
    id = request.POST['id']
    cliente = Cliente.objects.get(id=id)

    errores = Cliente.objects.validador_cliente(request.POST)


    if len(cliente) > 0:
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.rut = request.POST['rut']
        cliente.dv = request.POST['dv']
        cliente.email = request.POST['email']
        cliente.password = request.POST['password']
        cliente.direccion = request.POST['direccion']

