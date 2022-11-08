from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="User_Profile")
    
    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Account_Information(models.Model):
    first_name=models.CharField(max_length=100, blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    email=models.EmailField(max_length=100, blank=False, unique=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name

class ShippingAddress(models.Model):
    name = models.CharField(max_length=1024 )
    company = models.CharField(max_length=1024 ) 
    city = models.CharField(max_length=1024)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024 )
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=12)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

class Forgot_password(models.Model):
   email=models.EmailField(max_length=100, blank=False, unique=True)
   
   def __str__(self):
        return self.email

class Reset_password(models.Model):
   new_password1 = models.CharField(max_length=32)
   new_password2 = models.CharField(max_length=32)
   
   def __str__(self):
        return self.new_password1

