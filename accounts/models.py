from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  # null for databse  ///  blank for form