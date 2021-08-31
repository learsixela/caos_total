from django.db import models

class JugadorManager(models.Manager):
    def validar(self, data):
        errors = {}
        if len(data['player_name']) == 0:
            errors['player_name'] = 'Ingrese un nombre'
        if len(data['player_number']) == 0:
            errors['player_number'] = 'Ingrese un numero'
        if len(data['player_team']) == 0:
            errors['player_team'] = 'Ingrese un equipo'


class Jugador(models.Model):
    player_name = models.CharField(max_length=50)
    player_number = models.IntegerField()
    player_team = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JugadorManager()