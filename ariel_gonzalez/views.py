from django.shortcuts import render,HttpResponse,render,redirect
from .models import Item
from django.contrib import messages

# Create your views here.

#cambiar los nombres de los index para que funcione en diferentes app

def index(request):
	return render(request, 'ariel_gonzalez/index.html')

#Aqui se leerá la lista de todos los items que existen en la Base de datos
def item_list(request):
	list_items=Item.objects.all()
	context={'list_items':list_items}
	return render(request,"ariel_gonzalez/info.html",context)
	#return HttpResponse("Esta es la ruta para mostrar todos los items")

#Muestra la información del Item con sku=sku
def item_info(request,sku):
	#Validar que sku exista

	#si existe sku mostrar info del sku

	#Si no existe enviar errores
	return HttpResponse("Esta es la ruta para mostrar item: "+sku)

def item_update(request,sku):
	#Validar que sku exista

	#hacer update de sku

	#Si no existe redireciono a index enviar errores
	return HttpResponse("Esta es la ruta para actualizar item: "+sku)

def item_delete(request,sku):
	#Validar que sku exista

	#Si existe elimino items con sku=sku

	#Si no existe redirecione a index enviar errores
	return HttpResponse("Esta es la ruta para eliminar item: "+sku)

def item_create(request):
	errors = Item.objects.validate(request.POST)
	if len(errors) > 0:
		#Tratamiento de errores
		return redirect('/agonzalez')
	else:
		item = Item.objects.create(
				nombre=request.POST['name'],
				sku=request.POST['sku'],
				precio=request.POST['precio'],
				unidad=request.POST['unidad'],
			)
		messages.success(request,"Item Creado Satisfactoriamente")
		return redirect('/agonzalez')
		#return HttpResponse("Esta es la ruta para crear items")