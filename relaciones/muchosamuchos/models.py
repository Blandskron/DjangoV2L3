from django.db import models

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.titulo
