from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def inicio(request):
    return redirect(request,'israel_palma/index.html')

def create(request):
    return HttpResponse("create")

def read(request):
    return HttpResponse("read")

def update(request):
    return HttpResponse("update")

def delete(request):
    return HttpResponse("delete")



