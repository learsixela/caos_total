from django.urls import path, include
from . import views

urlpatterns = [
    path('index_rca', views.start),
    
]