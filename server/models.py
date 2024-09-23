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
class offices(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    apartment_name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    
    
    def __str__ (self):
        return self.Town 
    
class Shops(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    apartment_name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()

    def __str__(self):
        return self.Town

class estates(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    Street_name = models.CharField(max_length=98)
    estate_name= models.CharField(max_length = 30)
    House_number = models.CharField(max_length=10)
    apartment_name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    
    
    def __str__ (self):
        return self.estate_name 
    
class godowns(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    street_name = models.CharField(max_length = 70)
    apartment_name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    
    
    def __str__ (self):
        return self.Town 
    
class hotels(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    hotel_name = models.CharField(max_length = 70)
    street_name = models.CharField(max_length = 70)
    apartment_name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    
    
    def __str__ (self):
        return self.hotel_name

class Bungalow(models.Model):
    County = models.CharField(max_length = 250)
    Town = models.CharField(max_length =124)
    Bungalow_name = models.CharField(max_length = 70)
    estate_name = models.CharField(max_length = 70)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    
    
    def __str__ (self):
        return self.Bungalow_name
    
class StudentHostels(models.Model):
    County = models.CharField(max_length =124)
    Town = models.CharField(max_length =124)
    hostel_name = models.CharField(max_length = 70)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()


    def __str__ (self):
        return self.hostel_name
    

class LadiesHostels(models.Model):
    County = models.CharField(max_length =124)
    hostel_name = models.CharField(max_length = 70)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()

    def __str__ (self):
        return self.hostel_name

class KioskShops(models.Model):
    County = models.CharField(max_length =124)
    Street= models.CharField(max_length = 70)
    location = models.CharField(max_length=70)
    owner = models.CharField(max_length = 70)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='kiosk_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return f"{self.owner}'s shop in {self.location}, {self.County}"