from django.urls import path, include
from . import views
	
urlpatterns = [
	path('', views.index),
	path('items', views.item_info, name='item_info'),
]
