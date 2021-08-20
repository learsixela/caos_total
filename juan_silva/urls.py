from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar),
]