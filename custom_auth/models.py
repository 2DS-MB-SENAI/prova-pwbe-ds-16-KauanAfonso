from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models her
class CustomUser(AbstractUser):
    phone = models.CharField(unique=True, max_length=50)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return super().__str__()