from django import forms
from .models import File


class FileForm(forms.ModelForm):
    """
    Form for uploading a file.

    This form is responsible for creating a file upload form field.

    Attributes:
        file (forms.FileField): The file upload field.
    """

    file: forms.FileField = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "id": "inputGroupFile04",
                "aria-describedby": "inputGroupFileAddon04",
                "aria-label": "Upload",
            }
        )
    )

    class Meta:
        model = File
        fields = ["file"]
