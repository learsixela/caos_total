from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.inicio),
    #path('/inicio', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar),# create
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    path('mensajes', views.mensajes, name ='mensajes'),
]