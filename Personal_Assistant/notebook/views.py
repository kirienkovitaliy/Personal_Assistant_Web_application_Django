from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Note, Tag
from .forms import NoteForm, TagForm
# Create your views here.

class NoteHome(ListView):
    model = Note
    template_name = 'notebook/note_home.html'
    

class ShowNote(DetailView):
    model = Note
    template_name = 'notebook/note_detail.html'
    pk_url_kwarg = 'note_id'


class AddNote(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = 'notebook/note_form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTag(CreateView):
    form_class = TagForm
    template_name = 'notebook/tag_form.html'
    success_url = reverse_lazy('')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

