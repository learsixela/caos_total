from django.db import models

# Create your models here.
class ElementoManager(models.Manager):
    def validador_producto(self, data):
        errores = {}
        if len(data['id']) == 0:
            errores['id'] = 'Ingrese id'
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese nombre'
        if len(data['descripcion']) == 0:
            errores['descripcion'] = 'Ingrese descripcion'
        if len(data['precio']) == 0:
            errores['precio'] = 'Ingrese precio'
        if len(data['peso']) == 0:
            errores['peso'] = 'Ingrese peso'

class Elemento(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=50)
    peso = models.IntegerField()
    objects = ElementoManager()