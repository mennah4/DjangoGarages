
from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from garage import serializers
from .models import Garage,Car
from .serializers import GarageSerializer,CarSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


"""def garage_index(request):
    garage = Garage.objects.all()
    context = {
        'garage': garage
    }
    return render(request, 'garage_index.html', context)

def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, "car_detail.html", {"car":car})


def garage_cars(request,pk):
    try:
        garage = Garage.objects.get(pk=pk)
        cars_g = Car.objects.all().filter(garage_id = garage)
    except Garage.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, "garage_cars.html", {"cars_g":cars_g})"""


"""class GarageView(APIView):
    def get(self, request):
        garages = Garage.objects.all()
        serializer = GarageSerializer(garages,many=True)
        return Response(serializer.data)

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all().select_related('garage')
    serializer_class = serializers.CarSerializer"""



class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class GarageView(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsSuperUser()]
        elif self.request.method == 'POST':
            return [IsSuperUser()]
        else:
            return [IsAuthenticatedOrReadOnly()]

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsSuperUser()]
        elif self.request.method == 'POST':
            return [IsSuperUser()]
        else:
            return [IsAuthenticatedOrReadOnly()]

