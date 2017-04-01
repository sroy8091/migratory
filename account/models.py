# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    gen = (("Male", "MALE"),("Female", "FEMALE"))
    age = (("Below 18", "Below 18"), ("18 to 25", "18 to 25"), ("26 to 35", "26 to 35"), ("Above 35", "Above 35"))
    gender = models.CharField(max_length=6, choices=gen, blank=False, null=True)
    age = models.CharField(max_length=15, choices=age, blank=False, null=True)