# Generated by Django 4.0.1 on 2022-01-24 07:58

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
                ('experience', models.TextField(max_length=500)),
                ('no_of_vacancies', models.PositiveIntegerField()),
                ('remarks', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999-999999'. Up to 15 digits allowed.", regex='\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
