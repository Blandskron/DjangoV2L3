from django.urls import path
from . import views

urlpatterns = [
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('exito-libro/', views.exito_libro, name='exito_libro'),
]
