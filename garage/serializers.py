from rest_framework import serializers
from .models import Garage,Car

class GarageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Garage
        fields = ('id','url','name',)


"""class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','garage_id','manufacturer','color','model','year',)"""

class CarSerializer(serializers.HyperlinkedModelSerializer):
    #garage_cars = serializers.RelatedField(source='garage', read_only=True)
    #garage = GarageSerializer(many=False, read_only=True)
    class Meta:
        model = Car
        fields = ('id','url','model','manufacturer','color','garage')