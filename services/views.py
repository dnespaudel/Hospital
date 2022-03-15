from rest_framework import generics
from services.serializers import *
from rest_condition import And, Or
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.permissions import *


class ServicesListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Services.objects.all()
    serializer_class = ServicesIdSerializer


class ServicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class HospitalServicesListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = HospitalServices.objects.all()
    serializer_class = HospitalServicesSerializer


class HospitalServicesListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = HospitalServices.objects.all()
    serializer_class = HospitalServicesIdSerializer


class HospitalServicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = HospitalServices.objects.all()
    serializer_class = HospitalServicesSerializer


