from django.shortcuts import render

def inicio(request):
    #return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, 'showme.html')