from django.urls import path, include
from rest_framework import routers
from .views import ArchiveViewSet

router = routers.DefaultRouter()
router.register(r'api',ArchiveViewSet,basename="API")


urlpatterns = [
    path('', include(router.urls))
]