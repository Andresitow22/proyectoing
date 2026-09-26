from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, getPerfilView


router_user = DefaultRouter()

router_user.register(
    prefix='users',
    viewset=UserViewSet,
    basename='users'
)

urlpatterns = [
    path('auth/me/', getPerfilView.as_view()),
] + router_user.urls
