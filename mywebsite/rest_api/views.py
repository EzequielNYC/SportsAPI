from rest_framework import viewsets
from database.models import MetsData, YankeesData,KnicksData,NetsData,GiantsData,JetsData
from .serializers import NetsDataSerializer,KnicksDataSerializer,YankeesDataSerializer,MetsDataSerializer,JetsDataSerializer,GiantsDataSerializer
from django.http import HttpResponse

class YankeesDataViewSet(viewsets.ModelViewSet):
    queryset = YankeesData.objects.all()
    serializer_class = YankeesDataSerializer
class MetsDataViewSet(viewsets.ModelViewSet):
    queryset = MetsData.objects.all()
    serializer_class = MetsDataSerializer
class KnicksDataViewSet(viewsets.ModelViewSet):
    queryset = KnicksData.objects.all()
    serializer_class = KnicksDataSerializer
class NetsDataViewSet(viewsets.ModelViewSet):
    queryset = NetsData.objects.all()
    serializer_class = NetsDataSerializer
class GiantsDataViewSet(viewsets.ModelViewSet):
    queryset = GiantsData.objects.all()
    serializer_class = GiantsDataSerializer
class JetsDataViewSet(viewsets.ModelViewSet):
    queryset = JetsData.objects.all()
    serializer_class = JetsDataSerializer

