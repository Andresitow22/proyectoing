from rest_framework.routers import DefaultRouter

from .views import SensorViewSet, LecturaViewSet


router_sensores = DefaultRouter()

router_sensores.register(
    prefix='sensores',
    viewset=SensorViewSet,
    basename='sensores'
)

router_sensores.register(
    prefix='lecturas',
    viewset=LecturaViewSet,
    basename='lecturas'
)
