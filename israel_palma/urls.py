from django.urls import path, include
from . import views
#importar para clases
from israel_palma.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    # CRUD
    # acceso por defecto
    path('', views.inicio),
    path('create', views.create),
    path('update', views.update, name='update'),
    path('getServicio', views.getServicio, name='getServicio'),
    path('read', views.read),
    path('delete', views.delete),
    
    #clases 
    path('generarPdf', views.generarPdf, name='generarPdf'),
    path('servicios/list', views.ServiciosListView.as_view(), name='serviciosList'),
]