from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'index_rca.html')