from django.urls import path, include
from rest_framework import routers
from .views import (
    MetsDataViewSet,
    YankeesDataViewSet,
    KnicksDataViewSet,
    NetsDataViewSet,
    GiantsDataViewSet,
    JetsDataViewSet,
)

router = routers.DefaultRouter()
router.register(r'mets', MetsDataViewSet)
router.register(r'yankees', YankeesDataViewSet)
router.register(r'knicks', KnicksDataViewSet)
router.register(r'nets', NetsDataViewSet)
router.register(r'giants', GiantsDataViewSet)
router.register(r'jets', JetsDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
