from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user
from galpones.api.router import router_galpones
from sensores.api.router import router_sensores


schema_view = get_schema_view(
    openapi.Info(
        title="Avisens API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirige la raíz automáticamente a Swagger
    path('', RedirectView.as_view(url='swagger/', permanent=False)),

    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),

    # Swagger
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),

    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),

    # Redoc
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),

    # API de usuarios
    path('api/', include(router_user.urls)),
    path('api/', include('users.api.router')),

    # API de galpones
    path('api/', include(router_galpones.urls)),

    # API de sensores y lecturas
    path('api/', include(router_sensores.urls)),
]