import uuid
from register.models import RegisterLogin
from django.core.validators import RegexValidator
from django.db import models


class Career(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.TextField(max_length=500)
    no_of_vacancies = models.PositiveIntegerField()
    remarks = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.post


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999-999999'. Up to "
                                         "15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=200)


class Appointment(models.Model):
    appointment_time_choices = (
        ('10AM - 11AM', '10am - 11am'),
        ('11AM - 12PM', '11am - 12pm'),
        ('12PM - 1PM', '12pm - 1pm'),
        ('3PM - 4PM', '3pm - 4pm'),
        ('4PM - 5PM', '4pm - 5pm'),
    )
    select_department_choices = (
        ('CARDIOLOGY', 'Cardiology'),
        ('NEUROLOGY', 'Neurology'),
        ('DENTAL CARE', 'Dental Care'),
        ('EYE CARE', 'Eye Care'),
        ('ENT', 'ENT'),
        ('NEPHROLOGY', 'Nephrology'),
        ('RADIATION & INTERVENTION', 'Radiation & Intervention'),
        ('PLASTIC & COSMETIC SURGERY', 'Plastic & Cosmetic Surgery'),
        ('UROLOGY', 'Urology'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999-999999'. Up to "
                                         "15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    address = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.CharField(choices=appointment_time_choices, max_length=100)
    select_department = models.CharField(choices=select_department_choices, max_length=100)
    patient = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)
    problem = models.TextField(max_length=500)


