from django.db import models

# Create your models here.
class ClienteJRM(models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
