from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm
# Create your views here.

class ContactsHome(ListView):
    model = Contact
    template_name = 'addressbook/index.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(name__icontains=q) | Q(email__icontains=q) | Q(phone_number__icontains=q) |
                Q(address__icontains=q) | Q(birthday__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class AddContact(CreateView):
    form_class = ContactForm
    template_name = 'addressbook/contact_form.html'
    success_url = reverse_lazy('home')


class EditContact(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'addressbook/contact_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Contact, id=pk)
    

class DeleteContact(DeleteView):
    model = Contact
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
        
