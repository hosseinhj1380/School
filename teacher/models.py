from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import AbstractUser as ABC
from .validators import phone_validator
class User(models.Model):
    # id =models.AutoField()
    first_name = models.CharField(max_length=25,blank=False,null=False)
    last_name = models.CharField(max_length=25,blank=False,null=False)
    phonenumber = models.CharField(max_length=11,null=False,blank=False,validators=[phone_validator])
    username = models.CharField(max_length=11,null=False,blank=False)
    password = models.CharField(max_length=255,null=False,blank=False)
    email=models.EmailField(max_length=255,default=False)

    def __str__(self):
        return self.username