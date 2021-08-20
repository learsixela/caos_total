from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_cvega"),
    path('pic', views.show_pic, name="pic_cvega"),
]
