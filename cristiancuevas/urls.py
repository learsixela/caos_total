from django.urls import path, include
from . import views

urlpatterns = [
    # CRUD
    path('', views.inicio),
]