from django.db import models
from galpones.models import Galpon


class Sensor(models.Model):
    TIPOS = [
        ('temperatura', 'Temperatura'),
        ('humedad', 'Humedad'),
        ('amoniaco', 'Amoniaco'),
        ('co2', 'CO2'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    unidad = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    galpon = models.ForeignKey(Galpon, on_delete=models.CASCADE, related_name='sensores')

    def __str__(self):
        return f'{self.nombre} ({self.tipo})'


class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor.nombre}: {self.valor}'
