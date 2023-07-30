from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import NoteForm, TagForm
from .models import Note

# Create your views here.


class NoteHome(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notebook/note_home.html"

    def get_queryset(self) -> QuerySet[Any]:
        object_list_prefetch = self.model.objects.filter(user=self.request.user)
        tag = self.request.GET.get("tag")
        q = self.request.GET.get("q")
        if tag:
            object_list = object_list_prefetch.filter(tags__name=tag)
        elif q:
            object_list = object_list_prefetch.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            )
        else:
            object_list = object_list_prefetch
        return object_list

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        selected_tag = self.request.GET.get("tag")
        if selected_tag:
            context["selected_tag"] = selected_tag

        return context


class ShowNote(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notebook/note_detail.html"


class AddNote(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = "notebook/note_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTag(LoginRequiredMixin, CreateView):
    form_class = TagForm
    template_name = "notebook/tag_form.html"
    success_url = reverse_lazy("note_home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditNote(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notebook/note_form.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Note, id=pk)


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
