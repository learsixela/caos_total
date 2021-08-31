# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Objetos, atributos en minúscula

class Client(models.Model): # nombres de clases en singular
    id = models.AutoField(db_columns='client_id', primary_key=True) # la columna en base de datos se llama db_columns
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    joined_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clients'  # Como se va a llamar la tabla en la base de datos en plural


class Site(models.Model):
    id = models.AutoField(db_columns='site_id', primary_key=True)
    domain_name = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    client = models.ForeignKey(Client, related_name="sites", on_delete=models.CASCADE ) # client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sites'


class Lead(models.Model):
    id = models.AutoField(db_columns='leads_id', primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registered_datetime = models.DateTimeField()
    email = models.CharField(max_length=50)
    site = models.ForeignKey(Site, related_name="leads", on_delete=models.CASCADE)   #site_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leads'


class Documento(models.Model):
    id = models.AutoField(db_columns='billing_id', primary_key=True)
    amount = models.FloatField()
    charged_datetime = models.DateTimeField()
    client = models.ForeignKey(Client, related_name="billing", on_delete=models.CASCADE ) # client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'billing'




