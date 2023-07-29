from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
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


class AddNote(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = 'notebook/note_form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTag(CreateView):
    form_class = TagForm
    template_name = 'notebook/tag_form.html'
    success_url = reverse_lazy('note_home')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditNote(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notebook/note_form.html'
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk)


class DeleteNote(DeleteView):
    model = Note
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
