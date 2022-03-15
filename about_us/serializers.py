from about_us.models import *
from rest_framework import serializers


class HospitalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalImage
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class HospitalImageIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalImage
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class AboutHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHospital
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class AboutHospitalIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHospital
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class RecordIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DepartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentImage
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DepartmentImageIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentImage
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DepartmentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DoctorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorImage
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DoctorImageIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorImage
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DoctorIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DoctorDetailsIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class AboutDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutDoctor
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class AboutDoctorIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutDoctor
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class DoctorListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorListing
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class DoctorListingIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorListing
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


