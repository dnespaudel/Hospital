from contact.models import *
from rest_framework import serializers


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class ContactUsIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class GetConnectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetConnected
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class GetConnectedIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetConnected
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class SocialMediaIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }



