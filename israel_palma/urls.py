from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.inicio),
    path('create', views.create),
    path('read', views.read),
    path('update', views.update),
    path('delete', views.delete),
]