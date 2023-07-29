from django import forms

from .models import Note, Tag


class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ["name"]


class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ["title", "content", "tags"]
        