from django.db import models

# Create your models here.
from django.apps import models


class UsersConfig(models.Models):
    first_name = models.CharDField(max_length =255)
    second_name = models.CharField(max_length = 454)
    password = models.CharField(max_length = 345)
    email = models.EmailField(max_length = 255)
    area = models.CharField()
    def __str__(self): 

        return self.first_name