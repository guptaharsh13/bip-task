from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_title = 'Bip Task | Admin Panel'
admin.site.site_header = 'Bip Task Admin Panel'
admin.site.index_title = 'Welcome to Bip Task Admin Panel'

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation | Bip Task",
        default_version='v1.0.0',
        description="API Documentation for Bip Task Backend",
        contact=openapi.Contact(email=settings.DEFAULT_FROM_EMAIL),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('bip-task/admin/', admin.site.urls),
    path('', view=index, name="index"),
    path('blogs/', include("blogs.urls")),

    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
