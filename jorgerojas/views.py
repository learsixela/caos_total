from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Esta es la aplicacion de JRojas XD")

def inicio(request):
    #return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, 'showme.html')

