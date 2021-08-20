from django.shortcuts import render,HttpResponse,render

# Create your views here.
def index(request):
	return render(request, 'index1.html')

def item_info(request):
	return render(request,'info.html')

