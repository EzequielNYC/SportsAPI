from rest_framework import viewsets
from .permissions import ReadOnly
from database.models import MetsData, YankeesData,KnicksData,NetsData,GiantsData,JetsData
from .serializers import NetsDataSerializer,KnicksDataSerializer,YankeesDataSerializer,MetsDataSerializer,JetsDataSerializer,GiantsDataSerializer

class YankeesDataViewSet(viewsets.ModelViewSet):
    queryset = YankeesData.objects.all()
    serializer_class = YankeesDataSerializer
    permission_classes = [ReadOnly]

class MetsDataViewSet(viewsets.ModelViewSet):
    queryset = MetsData.objects.all()
    serializer_class = MetsDataSerializer
class KnicksDataViewSet(viewsets.ModelViewSet):
    queryset = KnicksData.objects.all()
    serializer_class = KnicksDataSerializer
    permission_classes = [ReadOnly]

class NetsDataViewSet(viewsets.ModelViewSet):
    queryset = NetsData.objects.all()
    serializer_class = NetsDataSerializer
class GiantsDataViewSet(viewsets.ModelViewSet):
    queryset = GiantsData.objects.all()
    serializer_class = GiantsDataSerializer
    permission_classes = [ReadOnly]

class JetsDataViewSet(viewsets.ModelViewSet):
    queryset = JetsData.objects.all()
    serializer_class = JetsDataSerializer
    permission_classes = [ReadOnly]


