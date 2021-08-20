from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    path('', views.inicio),
    #path('/inicio', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar),# create
    path('leer', views.leer),
    path('actualizar', views.actualizar),
    ]