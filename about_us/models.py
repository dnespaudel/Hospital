import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HospitalImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='HospitalImage')


class AboutHospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    images = models.ForeignKey(HospitalImage, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    numbers = models.CharField(max_length=5)
    image = models.ForeignKey(HospitalImage, on_delete=models.CASCADE)


class DepartmentImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='DepartmentImage')


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ForeignKey(DepartmentImage, on_delete=models.CASCADE)


class DoctorImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='DoctorImage')


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    doctor_image = models.OneToOneField(DoctorImage, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.full_name


class DoctorDetails(models.Model):
    achievements_choice = (
        ('EXPERIENCE', 'Experience'),
        ('AWARDS', 'Awards'),
        ('PATIENT-CHECKED', 'Patient-Checked'),
        ('SURGERY-DONE', 'Surgery-Done'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    achievement = models.CharField(choices=achievements_choice, max_length=50, default='Experience')
    icon_name = models.CharField(max_length=100)
    counts = models.IntegerField(blank=False)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)


class AboutDoctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)


class DoctorListing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    doctors = models.ManyToManyField(Doctor, related_name='doctors')

