from django.db import models

class Room(models.Model):
    name= models.CharField(max_length = 30)
    description = models.TextField()
    apartment = models.CharField(max_length= 30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    tenant_name = models.CharField(max_length=30)
    def  __str__(self):
        return self.name
    
class Tenant(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length=15, unique= True)
    contact = models.IntegerField()
    email = models.EmailField(unique= True)

    def  __str__ (self):
        return self.username
    