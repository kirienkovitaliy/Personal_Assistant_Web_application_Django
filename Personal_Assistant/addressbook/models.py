from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full name')
    email = models.EmailField(null=True, verbose_name='Birthday')
    phone_number = models.CharField(null=True, max_length=15, verbose_name='Phone number')
    address = models.CharField(null=True, max_length=255, verbose_name='Home address')
    birthday = models.DateField(verbose_name='Birthday')