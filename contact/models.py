import uuid
from django.db import models
from register.models import RegisterLogin


class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)
    user = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)


class GetConnected(models.Model):
    address_choices = (
        ('PHONE NUMBER', 'Phone Number'),
        ('EMAIL', 'Email'),
        ('LOCATION', 'Location'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    address = models.CharField(choices=address_choices, max_length=50, default='Phone Number')


class SocialMedia(models.Model):
    social_media_choices = (
        ('FACEBOOK', 'Facebook'),
        ('TWITTER', 'Twitter'),
        ('LINKEDIN', 'LinkedIn'),
        ('YOUTUBE', 'YouTube'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    social_media = models.CharField(choices=social_media_choices, max_length=50, default='Facebook')


