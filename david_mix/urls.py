from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start, name='dmix'),
    path('productos', views.productos, name='dmixStore'),
    path('register', views.register),
]