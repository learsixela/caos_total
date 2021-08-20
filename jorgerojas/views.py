from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def index(request):
    return HttpResponse("Esta es la aplicacion de JRojas XD")
=======
def inicio(request):
    #return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, 'showme.html')
>>>>>>> 779c44b5b088c33415fc0f8c4c284e11b50a3dda
