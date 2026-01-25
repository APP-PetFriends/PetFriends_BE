"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# config/urls.py 상단에 추가
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drug/', include('drug.urls')),
    # path('api/drug/', include('drug.urls')),
    # path('api/health/', include('health.urls')),
    path('api/', include('pet.urls')),
    path('api/users/', include('users.urls')),
    path('api/walk/', include('walk.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 이 줄 추가
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 이 줄 추가
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
