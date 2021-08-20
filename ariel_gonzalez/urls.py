from django.urls import path, include
from . import views
	
urlpatterns = [
	path('', views.index,name='index'),
	path('items/list', views.item_list, name='read'), #Leer lista items
	path('items/<str:sku>/info', views.item_info, name='read_item'), #Leer items
	path('items/<str:sku>/update', views.item_update, name='update'),	#update items
	path('items/<str:sku>/delete', views.item_delete, name='delete'),	#Eliminar Items
	path('items/create', views.item_create, name='create'),	#Crear Items
]
