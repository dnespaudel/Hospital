from rest_framework import generics
from about_us.serializers import *
from rest_condition import And, Or
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.permissions import *


class HospitalImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = HospitalImage.objects.all()
    serializer_class = HospitalImageSerializer


class HospitalImageListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = HospitalImage.objects.all()
    serializer_class = HospitalImageIdSerializer


class HospitalImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = HospitalImage.objects.all()
    serializer_class = HospitalImageSerializer


class AboutHospitalListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = AboutHospital.objects.all()
    serializer_class = AboutHospitalSerializer


class AboutHospitalListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = AboutHospital.objects.all()
    serializer_class = AboutHospitalIdSerializer


class AboutHospitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = AboutHospital.objects.all()
    serializer_class = AboutHospitalSerializer


class RecordListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Record.objects.all()
    serializer_class = RecordIdSerializer


class RecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class DepartmentImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DepartmentImage.objects.all()
    serializer_class = DepartmentImageSerializer


class DepartmentImageListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DepartmentImage.objects.all()
    serializer_class = DepartmentImageIdSerializer


class DepartmentImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = DepartmentImage.objects.all()
    serializer_class = DepartmentImageSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Department.objects.all()
    serializer_class = DepartmentIdSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorImageListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorImage.objects.all()
    serializer_class = DoctorImageSerializer


class DoctorImageListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorImage.objects.all()
    serializer_class = DoctorImageIdSerializer


class DoctorImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = DoctorImage.objects.all()
    serializer_class = DoctorImageSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = Doctor.objects.all()
    serializer_class = DoctorIdSerializer


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailsListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorDetails.objects.all()
    serializer_class = DoctorDetailsSerializer


class DoctorDetailsListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorDetails.objects.all()
    serializer_class = DoctorDetailsIdSerializer


class DoctorDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = DoctorDetails.objects.all()
    serializer_class = DoctorDetailsSerializer


class AboutDoctorListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = AboutDoctor.objects.all()
    serializer_class = AboutDoctorSerializer


class AboutDoctorListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = AboutDoctor.objects.all()
    serializer_class = AboutDoctorIdSerializer


class AboutDoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = AboutDoctor.objects.all()
    serializer_class = AboutDoctorSerializer


class DoctorListingListCreateView(generics.ListCreateAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorListing.objects.all()
    serializer_class = DoctorListingSerializer


class DoctorListingListView(generics.ListAPIView):
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = DoctorListing.objects.all()
    serializer_class = DoctorListingIdSerializer


class DoctorListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isAdminOrReadOnly]
    queryset = DoctorListing.objects.all()
    serializer_class = DoctorListingSerializer


