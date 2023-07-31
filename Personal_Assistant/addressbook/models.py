from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    """
    Model class for representing contact information.

    Attributes:
        name (CharField): The name of the contact.
        email (EmailField): The email address of the contact.
        phone_number (CharField): The phone number of the contact.
        address (TextField): The address of the contact.
        birthday (DateField): The birthday date of the contact.
        user (ForeignKey): The user associated with the contact (Foreign key to User model).
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    address = models.TextField(null=True, blank=True, max_length=255)
    birthday = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        """
        Returns a string representation of the Contact instance.

        Returns:
            str: The string representation (name) of the contact.
        """
        return self.name
