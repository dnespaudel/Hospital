# Generated by Django 4.0.1 on 2022-01-24 07:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GetConnected',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('address', models.CharField(choices=[('PHONE NUMBER', 'Phone Number'), ('EMAIL', 'Email'), ('LOCATION', 'Location')], default='Phone Number', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('social_media', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('TWITTER', 'Twitter'), ('LINKEDIN', 'LinkedIn'), ('YOUTUBE', 'YouTube')], default='Facebook', max_length=50)),
            ],
        ),
    ]