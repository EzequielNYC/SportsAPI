from django.urls import include, path
from frontend.views import home, contact, data_preview, use_api
from django.contrib import admin
from rest_framework import routers
from rest_api.views import (
    MetsDataViewSet,
    YankeesDataViewSet,
    KnicksDataViewSet,
    NetsDataViewSet,
    GiantsDataViewSet,
    JetsDataViewSet,
)

router = routers.DefaultRouter()
router.register('yankees-data', YankeesDataViewSet)
router.register('mets-data', MetsDataViewSet)
router.register('knicks-data', KnicksDataViewSet)
router.register('nets-data', NetsDataViewSet)
router.register('giants-data', GiantsDataViewSet)
router.register('jets-data', JetsDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('data_preview/', data_preview, name='data_preview'),
    path('use_api/', use_api, name='use_api'),
    path('api/', include(router.urls)),
    path('yankees-data/', YankeesDataViewSet.as_view({'get': 'list'}), name='yankees-data'),
    path('mets-data/', MetsDataViewSet.as_view({'get': 'list'}), name='mets-data'),
    path('knicks-data/', KnicksDataViewSet.as_view({'get': 'list'}), name='knicks-data'),
    path('nets-data/', NetsDataViewSet.as_view({'get': 'list'}), name='nets-data'),
    path('giants-data/', GiantsDataViewSet.as_view({'get': 'list'}), name='giants-data'),
    path('jets-data/', JetsDataViewSet.as_view({'get': 'list'}), name='jets-data'),
]
