import uuid
from django.db import models
from register.models import RegisterLogin


class NewsImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='NewsImages')


class NewsEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(NewsImage, related_name='images')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    is_special = models.BooleanField(default=False)
    user = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    comment = models.TextField(max_length=200)
    user = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)
    news = models.OneToOneField(NewsEvent, on_delete=models.CASCADE)


class Reaction(models.Model):
    reaction_choices = (
        ('LOVE', 'LOVE'),
        ('LIKE', 'LIKE'),
        ('SAD', 'SAD'),
        ('HAPPY', 'HAPPY'),
        ('WOW', 'WOW'),
        ('HAHA', 'HAHA'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)
    reaction = models.CharField(choices=reaction_choices, max_length=10, default='Like')
    news = models.OneToOneField(NewsEvent, on_delete=models.CASCADE)


class ShareOn(models.Model):
    share_choices = (
        ('FACEBOOK', 'Facebook'),
        ('INSTAGRAM', 'Instagram'),
        ('TWITTER', 'Twitter'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(RegisterLogin, on_delete=models.CASCADE)
    share = models.CharField(choices=share_choices, max_length=10, default='Facebook')



