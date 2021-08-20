from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pic', views.show_pic)
]
