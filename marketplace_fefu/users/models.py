from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,)

    REQUIRED_FIELDS = ["first_name", "last_name", "email", "phone"]

    address = models.TextField(max_length=200)

    def __str__(self):
        return self.email