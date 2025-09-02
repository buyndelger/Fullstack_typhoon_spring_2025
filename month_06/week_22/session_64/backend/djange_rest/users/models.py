from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Багш'),
        ('student', 'Оюутан'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

# Create your models here.
