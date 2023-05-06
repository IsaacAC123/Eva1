from django.urls import path
from . import views

urlpatterns = [
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),
    path('gracias/', views.gracias, name='gracias'),
]
