import uuid
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from register.manager import CustomUserManager


class RegisterLogin(AbstractUser):
    role_choices = (
        ('A', 'Admin'),
        ('M', 'Manager'),
        ('P', 'Patient'),
        ('D', 'Doctor'),
        ('N', 'Nurse'),
        ('R', 'Receptionist'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.IntegerField(default=1, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999-999999'. Up to "
                                         "15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    role = models.CharField(max_length=1, choices=role_choices, default='P')
    otp = models.IntegerField(null=True, blank=True)
    mfa_hash = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = RegisterLogin.objects.all().aggregate(largest=models.Max('patient_id'))['largest']
            if last_id is not None:
                self.patient_id = last_id + 1
        super(RegisterLogin, self).save()

    def __str__(self):
        return self.email