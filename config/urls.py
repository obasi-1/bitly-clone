from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Bitly Clone API",
      default_version='v1',
      description="A URL shortener API built with Django Rest Framework",
      contact=openapi.Contact(email="obasonz61@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 1. Admin and Swagger come FIRST
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # 2. The Shortener app comes LAST (because it catches everything else)
    path('', include('shortener.urls')),
]