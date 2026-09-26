from rest_framework.routers import DefaultRouter

from .views import GalponViewSet


router_galpones = DefaultRouter()

router_galpones.register(
    prefix='galpones',
    viewset=GalponViewSet,
    basename='galpones'
)
