from news.models import *
from rest_framework import serializers


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class NewsImageIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class NewsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEvent
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class NewsEventIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEvent
        fields = (
            'id'
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class CommentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class ReactionIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ShareOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareOn
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'updated_date': {'read_only': True},
        }


class ShareOnIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareOn
        fields = (
            'id',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


