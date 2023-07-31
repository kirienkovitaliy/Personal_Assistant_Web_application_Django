from django import forms
from .models import Note, Tag


class TagForm(forms.ModelForm):
    """
    Form for creating or editing a Tag object.

    Attributes:
        Meta (class): Inner class to specify the model and fields for the form.
    """

    class Meta:
        model = Tag
        fields = ["name"]


class NoteForm(forms.ModelForm):
    """
    Form for creating or editing a Note object.

    Attributes:
        Meta (class): Inner class to specify the model and fields for the form.
    """

    class Meta:
        model = Note
        fields = ["title", "content", "tags"]
