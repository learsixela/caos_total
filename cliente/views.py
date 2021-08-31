from django.shortcuts import render, HttpResponse,redirect
#email
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage

from .models import Cliente

def inicio(request):
    request.session['email'] = []
    return render(request,'cliente/index.html')

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

    return render(request, "cliente/index.html")

def leer(request):
    # el tipo de variable es definida por el contenido
    # select * from cliente 
    clientes = Cliente.objects.all()
    return render(request, "cliente/index.html")

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

def mensajes(request):
    msg = ""
    if request.method == "POST":
        subject = request.POST['asunto']
        mensaje = request.POST['mensaje']
        email = request.POST['email']
        recipient_list=[]
        recipient_list.append(email)
        email_from = settings.EMAIL_HOST_USER

        #send_mail(subject, mensajes, email_from, recipient_list)

        try:
            #send_mail(subject, mensajes, email_from, recipient_list)
            send_mail(subject, mensaje, email_from, ['sephitor@gmail.com'])
            msg="Gracias por su mensaje"
            messages.success(request, msg)

            #creando variable 'email' de session 
            request.session['email'] = request.POST['email']

        except BadHeaderError:
            msg_error="Dirección no encontrada"
            messages.error(request, msg_error)

        return render(request, "cliente/contacto.html")

    print()
    #si no existe la variable 'email' en session, le asigna a@a.cl por defecto
    email = request.session.get('email','a@a.cl')
    print(email)
    #si no existe error, keyerror
    email = request.session['email']
    print(email)
    if request.session.get('email', False):
        request.session['email'] = True
    print(request.session['email'])

    return render(request, "cliente/contacto.html")

def send_email(request):
    correo = EmailMessage('Mensaje de envio','aca el mensaje de salida.', to=['test.fullstack.python@gmail.com'])
    correo.send()
    msg="Gracias por su mensaje"
    messages.error(request, msg)
    return render(request, "cliente/contacto.html")