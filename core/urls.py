"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

#drf-yasg 
schema_view = get_schema_view(
   openapi.Info(
      title="BlogAPI",
      description="API for the BlogAPI",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls', namespace='blog')),
    path("api/", include('blog_api.urls', namespace='blog_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('users.urls', namespace='users')),
    
    
    # path('schema/', get_schema_view(
    #     title="BlogAPI",
    #     description="API for the BlogAPI",
    #     version="1.0.0"
    # ), name = 'openapi-schema'),

    #[Not Working] path('docs/', include_docs_urls(title="BlogAPI")),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

#allows to work with media folder locally
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
