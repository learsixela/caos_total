from django.db import models

# Create your models here.

class ProductoManager(models.Manager):
    def validaciones(self, data):
        errores = {}
        if len(data['nombre']) == 0:
            errores['nombre'] = "Ingrese un nombre"
        if len(data['codigo']) == 0:
            errores['codigo'] = "Ingrese un codigo"
        if len(data['categoria']) == 0:
            errores['categoria'] = "Ingrese una categoria"
        if len(data['distribuidor']) == 0:
            errores['distribuidor'] = "Ingrese un distribuidor"
        if len(data['precio_venta']) == 0:
            errores['precio_venta'] = "Ingrese un precio de venta"
        if len(data['costo']) == 0:
            errores['costo'] = "Ingrese un costo"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=12)
    categoria = models.CharField(max_length=20)
    distribuidor = models.CharField(max_length=50)
    precio_venta = models.IntegerField()
    costo = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductoManager()
    