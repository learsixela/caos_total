from django.shortcuts import render, HttpResponse


def inicio(request):
    return render(request, 'indexcc.html')

