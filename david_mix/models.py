from django.db import models

# Create your models here.
class ProductoManager(models.Manager):
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

class Producto(models.Model):
    def __init__(self, nombre, descripcion, precio, peso):
        self.id = models.AutoField(auto_created=True, primary_key=True)
        self.nombre = models.CharField(max_length=50)
        self.descripcion = models.CharField(max_length=200)
        self.precio = models.CharField(max_length=50)
        self.peso = models.IntegerField()
        objects = ProductoManager()