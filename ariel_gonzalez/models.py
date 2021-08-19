from django.db import models
import re
import bcrypt

# Create your models here.
class ItemManager(models.Manager):
    def validate(self, user_data):
        pass


class Items(models.Model):
    nombre = models.CharField(max_length=40)
    sku = models.CharField(max_length=10)
    unidad = models.CharField(max_length=40)
    precio = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()