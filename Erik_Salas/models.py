from django.db import models

# Create your models here.
class RegistroManager(models.Manager):
    def validador_registro(self, data):
        errores = {}
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese un apellido'
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
            errores['email'] = "email invalido"
        return errores

    def login_registro(self, data):
        errores = {}
        return errores

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistroManager()