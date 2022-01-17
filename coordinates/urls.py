from rest_framework import routers

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import UserViewSet, LocationViewSet, PropertyViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
