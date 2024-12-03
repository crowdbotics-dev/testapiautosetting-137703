from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137703ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137703", Testconnectors137703ViewSet, basename="testconnectors137703"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
