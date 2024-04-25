from django.urls import path
from . import views

urlpatterns = [
    path('', views.llenar_tablas, name='llenar_tablas'),
    path('exito/', views.exito, name='exito'),
]
