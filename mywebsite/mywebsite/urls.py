from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rest_api.views import (
    MetsDataViewSet,
    YankeesDataViewSet,
    KnicksDataViewSet,
    NetsDataViewSet,
    GiantsDataViewSet,
    JetsDataViewSet,
    home,
)

router = routers.DefaultRouter()
router.register('yankees-data', YankeesDataViewSet)
router.register('mets-data', MetsDataViewSet)
router.register('knicks-data',KnicksDataViewSet)
router.register('nets-data', NetsDataViewSet)
router.register('giants-data',GiantsDataViewSet)
router.register('jets-data',JetsDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('api/', include(router.urls)),
    path('yankees-data/', YankeesDataViewSet.as_view({'get': 'list'}), name='yankees-data'),
    path('mets-data/', MetsDataViewSet.as_view({'get': 'list'}), name='mets-data'),
    path('knicks-data/', KnicksDataViewSet.as_view({'get': 'list'}), name='knicks-data'),
    path('nets-data/', NetsDataViewSet.as_view({'get': 'list'}), name='nets-data'),
    path('giants-data/', GiantsDataViewSet.as_view({'get': 'list'}), name='giants-data'),
    path('jets-data/', JetsDataViewSet.as_view({'get': 'list'}), name='jets-data'),
]