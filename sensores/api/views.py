from rest_framework.viewsets import ModelViewSet
from sensores.models import Sensor, Lectura
from sensores.api.serializers import SensorSerializer, LecturaSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class LecturaViewSet(ModelViewSet):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer
