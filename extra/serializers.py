from extra.models import *
from rest_framework import serializers


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class CareerIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class FeedbackIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class AppointmentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


