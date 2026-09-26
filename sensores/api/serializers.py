from rest_framework import serializers

from sensores.models import Sensor, Lectura


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'nombre', 'tipo', 'unidad', 'activo', 'galpon']


class LecturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lectura
        fields = ['id', 'sensor', 'valor', 'fecha']
