from django.shortcuts import render,HttpResponse,render

# Create your views here.
def index(request):
	return HttpResponse("this is the equivalent of @app.route('ariel_gonzalez/')!")

