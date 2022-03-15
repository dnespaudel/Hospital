from rest_framework import generics
from contact.serializers import *
from rest_condition import And, Or
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.permissions import *


class ContactUsListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactUsListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsIdSerializer


class ContactUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class GetConnectedListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = GetConnected.objects.all()
    serializer_class = GetConnectedSerializer


class GetConnectedListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = GetConnected.objects.all()
    serializer_class = GetConnectedIdSerializer


class GetConnectedDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = GetConnected.objects.all()
    serializer_class = GetConnectedSerializer


class SocialMediaListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class SocialMediaListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser)]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaIdSerializer


class SocialMediaDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


