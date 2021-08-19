"""proyecto_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('cliente.urls')), # ruta por defecto
    path('cliente/', include('cliente.urls')),
    path('alex_urtubia/', include('Alex_urtubia.urls')),
    path('jorgerojas/', include('jorgerojas.urls')),
    path('ccuevas/', include('cristiancuevas.urls')),  
    path('max_sanchez/',include('Max_Sanchez.urls')),
    path('cvega/', include('constanza_vega.urls')),
    path('jsilva/', include('juan_silva.urls')),
    path('julloa/', include('jose_ulloa.urls')),
    path('e_salas', include('Erik_Salas.urls')),
    path('agonzalez/', include('ariel_gonzalez.urls')),
    path('alvaro/', include('alvaro_castillo.urls')),
    path('ipalma/', include('israel_palma.urls')),
]