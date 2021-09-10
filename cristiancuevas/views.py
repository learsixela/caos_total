from django.shortcuts import render, HttpResponse

from .models import Jugador

def index(request):
    """ return HttpResponse("app de Toshi") """
    return render(request, "cristiancuevas/index.html")


def crear(request):
    # request.post['parametro']
    # capturando los parametros enviados por el formulario
    Jugador.objects.create(
    player_name = request.POST['player_name'], # se captura lo que va en el name
    player_number = request.POST['player_number'],
    player_team = request.POST['player_team']
    )

    # Vamos a pasar info
    jugador = request.POST['player_name']
    numero = request.POST['player_number']
    equipo = request.POST['player_team']
    context = {
        'perro': jugador,
        'gato': numero,
        'hamster': equipo,
    }
    return render(request, "cristiancuevas/creado.html", context)

def actualizar(request):
    return HttpResponse("actualizar")

def eliminar(request):
    return HttpResponse("eliminar")