from django.db import models

# Create your models here.
class pizzaManager(models.Manager): # se define el manager de cliente
    def validador_cliente(self, data):
        errors = {}
        if len(data['nombre']) == 0:
            errors['nombre'] = 'Ingrese un nombre para la pizza'
        if len(data['ingredientes']) == 0:
            errors['ingredientes'] = 'Ingrese descripcion de ingredientes que contendria la pizza'
        if len(data['valor']) == 0:
            errors['valor'] = 'Ingrese valor'
        return errors

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=150)
    valor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = pizzaManager()