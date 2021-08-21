from django.db import models

# Create your models here.
class ServicioManager(models.Manager):
    def validaciones(self, data):
        errores = {}
        if len(data['servicio']) == 0:
            errores['servicio'] = 'Ingrese un servicio'
        if len(data['descripcion']) == 0:
            errores['descripcion'] = 'Ingrese una descripcion'
        if len(data['tiempo']) == 0:
            errores['tiempo'] = 'Ingrese el tiempo'
        if len(data['costo']) == 0:
            errores['costo'] = 'Ingrese el costo del servicio'

class Servicio(models.Model):
    
    servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tiempo = models.IntegerField()
    costo = models.IntegerField()
    objects = ServicioManager()
