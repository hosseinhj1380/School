from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    activation_code = models.CharField(max_length=200, verbose_name='ایمیل فعال سازی')

    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'
