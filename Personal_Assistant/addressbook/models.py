from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True,unique=True)
    phone_number = models.CharField(null=True, blank=True,max_length=15, unique=True)
    address = models.TextField(null=True, blank=True,  max_length=255)
    birthday = models.DateField(null=True, blank=True)