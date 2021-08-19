from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Producto')
    codigo = models.CharField(max_length=100,verbose_name='Codigo')
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion')
    stock=models.IntegerField(verbose_name='Stock')
    precio=models.DecimalField(max_digits=10,decimal_places=0,verbose_name='Precio')