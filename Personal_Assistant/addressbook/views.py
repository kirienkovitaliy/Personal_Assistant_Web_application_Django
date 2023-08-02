from datetime import timedelta
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ContactForm
from .models import Contact


class ContactsHome(LoginRequiredMixin, ListView):
    """
    View class for displaying the list of contacts.

    Attributes:
        model (Contact): The model class for contact information.
        template_name (str): The name of the template to be rendered.
    """

    model = Contact
    template_name = "addressbook/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        """
        Retrieve the queryset of contacts.

        Returns:
            QuerySet[Any]: The queryset of contacts based on the request parameters.
        """
        object_list_prefetch = self.model.objects.filter(user=self.request.user)
        date_range = self.request.GET.get("birthday_for_next_day")
        if date_range:
            triggered_pk = []
            start_date = now().date()
            end_date = start_date + timedelta(days=int(date_range))
            for obj in object_list_prefetch:
                if not obj.birthday:
                    continue
                if (
                    end_date.year > start_date.year
                    and obj.birthday.month < start_date.month
                ):
                    birthday = obj.birthday.replace(year=end_date.year)
                else:
                    birthday = obj.birthday.replace(year=start_date.year)
                if start_date <= birthday < end_date:
                    triggered_pk.append(obj.pk)

            object_list_prefetch = object_list_prefetch.filter(pk__in=triggered_pk)

        q = self.request.GET.get("q")
        if q:
            object_list = object_list_prefetch.filter(
                Q(name__icontains=q)
                | Q(email__icontains=q)
                | Q(phone_number__icontains=q)
                | Q(address__icontains=q)
                | Q(birthday__icontains=q)
            )
        else:
            object_list = object_list_prefetch
        return object_list


class AddContact(LoginRequiredMixin, CreateView):
    """
    View class for adding a new contact.

    Attributes:
        form_class (BaseModelForm): The form class for contact information.
        template_name (str): The name of the template to be rendered.
        success_url (str): The URL to redirect after successful form submission.
    """

    form_class = ContactForm
    template_name = "addressbook/contact_form.html"
    success_url = reverse_lazy("addressbook:home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        Save the contact instance with the user who created it.

        Args:
            form (BaseModelForm): The form containing contact information.

        Returns:
            HttpResponse: The response after successful form submission.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditContact(LoginRequiredMixin, UpdateView):
    """
    View class for editing an existing contact.

    Attributes:
        model (Contact): The model class for contact information.
        form_class (BaseModelForm): The form class for contact information.
        template_name (str): The name of the template to be rendered.
        success_url (str): The URL to redirect after successful form submission.
    """

    model = Contact
    form_class = ContactForm
    template_name = "addressbook/contact_form.html"
    success_url = reverse_lazy("addressbook:home")

    def get_object(self):
        """
        Retrieve the contact instance to be edited.

        Returns:
            Contact: The contact instance to be edited.
        """
        pk = self.kwargs.get("pk")
        return get_object_or_404(Contact, id=pk)


class DeleteContact(LoginRequiredMixin, DeleteView):
    """
    View class for deleting a contact.

    Attributes:
        model (Contact): The model class for contact information.
    """

    model = Contact

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """
        Delete the contact instance.

        Args:
            request (HttpRequest): The HTTP request.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        Returns:
            HttpResponse: The response after successful contact deletion.
        """
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
