from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('apps.common.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.tasks.urls'))
]