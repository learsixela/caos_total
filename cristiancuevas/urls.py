from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.index, name="index_ccuevas"),
    path('crear', views.crear),
    path('actualizar', views.actualizar),
    path('eliminar', views.eliminar),    
    path('mostrar', views.mostrar),    
]




