from django.contrib import admin
from .models import Galpon


@admin.register(Galpon)
class GalponAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ubicacion', 'capacidad', 'usuario']
