from django import forms

from .models import File


class FileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", 
                                                         "id": "inputGroupFile04", 
                                                         "aria-describedby":"inputGroupFileAddon04", 
                                                         "aria-label": "Upload"}))

    class Meta:
        model = File
        fields = ["file"]