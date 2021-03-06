# Generated by Django 4.0.1 on 2022-01-26 07:50

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999-999999'. Up to 15 digits allowed.", regex='\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(max_length=100)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.CharField(choices=[('10AM - 11AM', '10am - 11am'), ('11AM - 12PM', '11am - 12pm'), ('12PM - 1PM', '12pm - 1pm'), ('3PM - 4PM', '3pm - 4pm'), ('4PM - 5PM', '4pm - 5pm')], max_length=100)),
                ('select_department', models.CharField(choices=[('CARDIOLOGY', 'Cardiology'), ('NEUROLOGY', 'Neurology'), ('DENTAL CARE', 'Dental Care'), ('EYE CARE', 'Eye Care'), ('ENT', 'ENT'), ('NEPHROLOGY', 'Nephrology'), ('RADIATION & INTERVENTION', 'Radiation & Intervention'), ('PLASTIC & COSMETIC SURGERY', 'Plastic & Cosmetic Surgery'), ('UROLOGY', 'Urology')], max_length=100)),
                ('problem', models.TextField(max_length=500)),
            ],
        ),
    ]
