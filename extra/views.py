from rest_framework import generics
from extra.serializers import *
from rest_condition import And, Or
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.permissions import *


class CareerListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class CareerListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Career.objects.all()
    serializer_class = CareerIdSerializer


class CareerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated, isPatient)]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackIdSerializer


class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isPatient)]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class AppointmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated, isPatient)]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentIdSerializer


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isPatient)]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


