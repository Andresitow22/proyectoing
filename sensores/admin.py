from django.contrib import admin
from .models import Sensor, Lectura


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'tipo', 'unidad', 'activo', 'galpon']


@admin.register(Lectura)
class LecturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'valor', 'fecha']
