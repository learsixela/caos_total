from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mrdiv),
    path('productos', views.productos),
    path('register', views.register),
    ]