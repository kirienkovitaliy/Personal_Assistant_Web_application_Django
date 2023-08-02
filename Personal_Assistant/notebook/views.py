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


class NoteHome(LoginRequiredMixin, ListView):
    """
    View to display a list of notes.

    Attributes:
        model (Note): The model for the view.
        template_name (str): The name of the template to render.
    """

    model: Note = Note
    template_name: str = "notebook/note_home.html"

    def get_queryset(self) -> QuerySet[Any]:
        """
        Get the queryset for displaying the list of notes.

        Returns:
            QuerySet[Any]: The queryset of notes filtered by tag or search query.
        """
        object_list_prefetch: QuerySet[Any] = self.model.objects.filter(
            user=self.request.user
        )
        tag: str = self.request.GET.get("tag")
        q: str = self.request.GET.get("q")
        if tag:
            object_list: QuerySet[Any] = object_list_prefetch.filter(tags__name=tag)
        elif q:
            object_list = object_list_prefetch.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            )
        else:
            object_list = object_list_prefetch
        return object_list

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get additional context data for the template.

        Returns:
            Dict[str, Any]: The context data.
        """
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        selected_tag: str = self.request.GET.get("tag")
        if selected_tag:
            context["selected_tag"] = selected_tag
        return context


class ShowNote(LoginRequiredMixin, DetailView):
    """
    View to display details of a note.

    Attributes:
        model (Note): The model for the view.
        template_name (str): The name of the template to render.
    """

    model: Note = Note
    template_name: str = "notebook/note_detail.html"


class AddNote(LoginRequiredMixin, CreateView):
    """
    View to create a new note.

    Attributes:
        form_class (NoteForm): The form class for creating a note.
        template_name (str): The name of the template to render.
    """

    form_class: NoteForm = NoteForm
    template_name: str = "notebook/note_form.html"

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Creates kwargs for form.

        Add to default kwargs user to filter tag choise field

        Returns:
            Dict[str, Any]: Dict of kwargs for form.
        """
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Handle form validation for creating a new note.

        Args:
            form (BaseModelForm): The form instance.

        Returns:
            HttpResponse: The HTTP response after successful form validation.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddTag(LoginRequiredMixin, CreateView):
    """
    View to create a new tag.

    Attributes:
        form_class (TagForm): The form class for creating a tag.
        template_name (str): The name of the template to render.
        success_url (str): The URL to redirect after successful tag creation.
    """

    form_class: TagForm = TagForm
    template_name: str = "notebook/tag_form.html"
    success_url: str = reverse_lazy("notebook:note_home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Handle form validation for creating a new tag.

        Args:
            form (BaseModelForm): The form instance.

        Returns:
            HttpResponse: The HTTP response after successful form validation.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditNote(LoginRequiredMixin, UpdateView):
    """
    View to edit a note.

    Attributes:
        model (Note): The model for the view.
        form_class (NoteForm): The form class for editing a note.
        template_name (str): The name of the template to render.
    """

    model: Note = Note
    form_class: NoteForm = NoteForm
    template_name: str = "notebook/note_form.html"

    def get_object(self):
        """
        Get the note object to edit.

        Returns:
            Any: The note object to edit or None if not found.
        """
        pk: str = self.kwargs.get("pk")
        return get_object_or_404(Note, id=pk)

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class DeleteNote(LoginRequiredMixin, DeleteView):
    """
    View to delete a note.

    Attributes:
        model (Note): The model for the view.
    """

    model: Note = Note

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """
        Handle HTTP POST request to delete a note.

        Args:
            request (HttpRequest): The HTTP POST request object.
            args (Any): Variable length argument list.
            kwargs (Any): Arbitrary keyword arguments.
        Returns:
            HttpResponse: The HTTP response with status code 204 (No Content).
        """
        self.object: Note = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
