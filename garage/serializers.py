from rest_framework import serializers
from .models import Garage,Car
from django.contrib.auth.models import User

"""class GarageSerializer(serializers.ModelSerializer):
    cars = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='garage:car-detail',
    )

    class Meta:
        model = Garage
        fields = ('id','url','name','cars',)"""
class GarageSerializer(serializers.ModelSerializer):
    cars = serializers.SlugRelatedField(many=True, read_only=True,
                                          slug_field='model')

    class Meta:
        model = Garage
        fields = ('name', 'cars')

"""class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id','garage_id','manufacturer','color','model','year',)"""

class CarSerializer(serializers.HyperlinkedModelSerializer):
    #garage_cars = serializers.RelatedField(source='garage', read_only=True)
    #garage = GarageSerializer(many=False, read_only=True)


    class Meta:
        model = Car
        fields = ('id','url','model','manufacturer','color','garage','year',)


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        # Specify the model we are using
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')

