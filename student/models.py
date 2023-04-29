from django.db import models
# from django.contrib.auth.models import AbstractUser as ABC
from .validator import phone_validator
class User(models.Model):
    # id =models.AutoField()
    first_name = models.CharField(max_length=25,blank=False,null=False)
    last_name = models.CharField(max_length=25,blank=False,null=False)
    phonenumber = models.CharField(max_length=11,null=False,blank=False,validators=[phone_validator])
    username = models.CharField(null=False,blank=False,max_length=255)
    password = models.CharField(max_length=255,null=False,blank=False)
    email=models.EmailField(max_length=255,default=None)

    def __str__(self):
        return self.username