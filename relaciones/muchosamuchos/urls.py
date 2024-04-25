from django.urls import path
from . import views

urlpatterns = [
    path('agregar-articulo/', views.agregar_articulo, name='agregar_articulo'),
    path('envio-exitoso/', views.envio_exitoso, name='envio_exitoso'),
]
