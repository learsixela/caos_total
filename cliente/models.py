from django.db import models
import re

# Create your models here.
class ClienteManager(models.Manager):
    def validador_cliente(self, data):
        errores = {} #diccionario de errores
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese un apellido'
        if len(data['rut']) == 0:
            errores['rut'] = 'Ingrese un rut'
        if len(data['dv']) == 0:
            errores['dv'] = 'Ingrese un dv'
        #expresiones regulares para validar los datos ingresados
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
            errores['email'] = "email invalido"
        if len(data['direccion']) == 0:
            errores['direccion'] = 'Ingrese una direccion'
        return errores

    def login_cliente(self, data):
        errores = {}
        return errores

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClienteManager()