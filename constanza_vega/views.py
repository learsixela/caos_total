from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index_cvega.html')


def show_pic(request):


    return render(request, 'error_cvega.html')
