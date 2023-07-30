from django.forms import ModelForm, CharField, FileInput, TextInput, FileField

from .models import Picture


class PictureForm(ModelForm):
    """
    Form for creating and updating Picture instances.

    This form is used to create and update instances of the Picture model.
    It includes fields for entering a description and uploading an image file.

    Attributes:
        description (CharField): A field for entering the picture description.
            It uses a TextInput widget with a "form-control" class for styling.
        path (FileField): A field for uploading the image file.
            It uses a FileInput widget with a "form-control" class for styling.
    """

    description = CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control"})
    )
    path = FileField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Picture
        fields = ["description", "path"]
