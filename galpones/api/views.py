from rest_framework.viewsets import ModelViewSet
from galpones.models import Galpon
from galpones.api.serializers import GalponSerializer


class GalponViewSet(ModelViewSet):
    queryset = Galpon.objects.all()
    serializer_class = GalponSerializer
