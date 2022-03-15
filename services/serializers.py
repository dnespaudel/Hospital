from services.models import *
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class ServicesIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class HospitalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalServices
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class HospitalServicesIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalServices
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


