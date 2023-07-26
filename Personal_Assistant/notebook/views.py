from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Note, Tag
from .forms import NoteForm, TagForm
# Create your views here.

class AddNote(CreateView):
    form_class = NoteForm
    template_name = 'notebook/note_form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)