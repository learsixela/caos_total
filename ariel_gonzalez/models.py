from django.db import models
import re
#import bcrypt

# Create your models here.
class ItemManager(models.Manager):
    def validate(self, item_data):
        errores={}
        if len(item_data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(item_data['sku']) == 0:
            errores['sku'] = 'Ingrese un código (sku)'
        if len(item_data['unidad']) == 0:
            errores['unidad'] = 'Ingrese unidad de medida'
        if len(item_data['precio']) == 0:
            errores['precio'] = 'Ingrese el precio del Item'
        return errores


class Item(models.Model):
    nombre = models.CharField(max_length=40)
    sku = models.CharField(max_length=10)
    unidad = models.CharField(max_length=40)
    precio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()