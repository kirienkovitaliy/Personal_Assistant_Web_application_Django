from typing import Any
from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.timezone import now
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm
# Create your views here.


class ContactsHome(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'addressbook/index.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        
        object_list_prefetch = self.model.objects.filter(user=self.request.user)
        if self.request.GET.get('birthday_on_next_week') == 'on':
            print(f'birthday trigger')
            triggered_pk = []
            for obj in object_list_prefetch:
                start_date = now().date()
                end_date = start_date + timedelta(days=7)
                if not obj.birthday:
                    continue
                birthday = obj.birthday.replace(year=start_date.year)
                if start_date <= birthday < end_date:
                    triggered_pk.append(obj.pk)
            
            object_list_prefetch = object_list_prefetch.filter(pk__in=triggered_pk)
            
        q = self.request.GET.get('q')
        if q:
            object_list = object_list_prefetch.filter(
                Q(name__icontains=q) | Q(email__icontains=q) | Q(phone_number__icontains=q) |
                Q(address__icontains=q) | Q(birthday__icontains=q)
            )
        else:
            object_list = object_list_prefetch
        return object_list


class AddContact(LoginRequiredMixin, CreateView):
    form_class = ContactForm
    template_name = 'addressbook/contact_form.html'
    success_url = reverse_lazy('addressbook:home')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditContact(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'addressbook/contact_form.html'
    success_url = reverse_lazy('addressbook:home')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Contact, id=pk)
    

class DeleteContact(LoginRequiredMixin, DeleteView):
    model = Contact
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=204)
        
