from rest_framework import serializers
from register.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLogin
        fields = (
            'id',
            'created_date',
            'updated_date',
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'address',
            'phone_number',
            'patient_id',
            'mfa_hash',
            'role',
            'otp',
            'is_verified',
        )

        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
            'role': {'read_only': True},
            'patient_id': {'read_only': True},
            'is_verified': {'read_only': True},
        }


class RegisterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLogin
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
            'username',
            'address',
        )

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class RegisterLoginIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLogin
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = RegisterLogin
        fields = [
            'id',
            'username'
            'patient_id',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
        }


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLogin
        fields = (
            'id',
            'created_date',
            'updated_date',
            'role',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
