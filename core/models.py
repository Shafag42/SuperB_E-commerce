from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class ContactUs(models.Model):
    first_name = models.CharField(max_length=255,verbose_name='First Name', help_text='Max 255 character')
    email = models.EmailField(verbose_name='Email Address')
    company = models.TextField(verbose_name='Company', null=True, blank=True)
    telephone = models.CharField(max_length=25 ,verbose_name='Telephone')
    address_one = models.TextField(verbose_name='Address_one')
    address_two = models.TextField(verbose_name='Addres_two', null=True, blank=True)
    comment = models.TextField(verbose_name='Comment')

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.first_name

class ContactInfo(models.Model):
    first_name=models.CharField(max_length=100, blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    company=models.CharField(max_length=200, blank=True)
    telephone=models.CharField(default='', max_length=50, blank=False)
    fax=models.CharField(max_length=25, blank=True)
    address_one = models.TextField(verbose_name='Street Address')
    address_two = models.TextField(verbose_name='Street Address 2')
    zip = models.CharField(max_length=100,blank=False)
    state_province = models.CharField(max_length=200,blank=False)
    country = CountryField(max_length=255, verbose_name='Country')
    comments=models.TextField(max_length=200,blank=False)
    
    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.first_name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return f'{self.question, self.answer}'


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email


class BlockedIP(models.Model):
    ip_addr = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.ip_addr

    class Meta:
        verbose_name = "BlockedIP"
        verbose_name_plural = "BlockedIPs"