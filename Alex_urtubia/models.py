from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=12)
    categoria = models.CharField(max_length=20)
    distribuidos = models.CharField(max_length=50)
    precio_venta = models.IntegerField(max_length=10)
    costo = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    