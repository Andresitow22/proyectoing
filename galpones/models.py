from django.db import models
from django.conf import settings


class Galpon(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='galpones')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
