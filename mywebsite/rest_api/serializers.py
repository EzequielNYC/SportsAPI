from rest_framework import serializers
from database.models import MetsData,YankeesData,KnicksData,NetsData,GiantsData,JetsData


class MetsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetsData
        fields = '__all__'
class YankeesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YankeesData
        fields = '__all__'
class KnicksDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnicksData
        fields = '__all__'
class NetsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetsData
        fields = '__all__'
class JetsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JetsData
        fields = '__all__'
class GiantsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiantsData
        fields = '__all__'
