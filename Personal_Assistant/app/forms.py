from django.forms import ModelForm, CharField, FileInput, TextInput, FileField

from .models import Picture


class PictureForm(ModelForm):
    description = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    path = FileField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Picture
        fields = ['description', 'path']
