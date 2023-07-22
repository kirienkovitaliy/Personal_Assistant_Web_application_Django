import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address', 'birthday']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            pattern = r'/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/gm'
            if not re.match(pattern, phone_number):
                raise ValidationError('Phone number is not valid')
        return phone_number