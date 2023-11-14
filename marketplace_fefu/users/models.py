from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from pytils.translit import slugify

from django.urls import reverse

class User(AbstractUser):

    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    vk = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='users', blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    