from django.db import models

# Create your models here.
class AlvaroManager(models.Manager): # se define el manager de cliente
    def validador_cliente(self, data):
        errors = {}
        if len(data['nombre']) == 0:
            errors['nombre'] = 'Ingrese un nombre'
        if len(data['ingredientes']) == 0:
            errors['ingredientes'] = 'Ingrese descripcion de ingredientes'
        if len(data['valor']) == 0:
            errors['valor'] = 'Ingrese valor'
        return errors

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=150)
    valor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AlvaroManager()