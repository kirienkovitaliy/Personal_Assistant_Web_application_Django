import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the Contact model.

    Attributes:
        Meta (class): Configuration options for the form.
    """

    class Meta:
        """
        Configuration options for the ContactForm.

        Attributes:
            model (Model): The model to be used for the form.
            fields (list): The fields from the model to be included in the form.
            widgets (dict): Custom widgets to be used for specific form fields.
        """

        model = Contact
        fields = ["name", "email", "phone_number", "address", "birthday"]
        widgets = {
            "address": forms.TextInput(attrs={"class": "form-input"}),
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_phone_number(self) -> str:
        """
        Custom validation method for the phone_number field.

        Returns:
            str: The cleaned phone number if it's valid.

        Raises:
            ValidationError: If the phone number is not valid according to the pattern.
        """
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number:
            pattern = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
            if not re.match(pattern, phone_number):
                raise ValidationError("Phone number is not valid.")
        return phone_number
