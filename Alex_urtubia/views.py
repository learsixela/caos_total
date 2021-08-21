from django.shortcuts import render, HttpResponse

# Create your views here.
def start(request):
    return render(request, 'alex_urtubia/index.html')

def create(request):
    return HttpResponse("Create")

def update(request):
    return HttpResponse("Read")

def delete(request):
    return HttpResponse("Delete")
