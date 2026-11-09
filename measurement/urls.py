from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SensorViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet, basename='sensor')

urlpatterns = [
    path('', include(router.urls)),
]
