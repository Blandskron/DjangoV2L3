from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    biografia = models.TextField()

