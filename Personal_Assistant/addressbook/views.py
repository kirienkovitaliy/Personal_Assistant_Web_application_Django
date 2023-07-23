from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm
# Create your views here.


class ContactsHome(ListView):
    model = Contact
    template_name = 'addressbook/index.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Contact.objects.all()


class AddContact(CreateView):
    form_class = ContactForm
    template_name = 'addressbook/add_contact.html'
    
    
    
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    context = {
        'form': form,
        'title': 'Add new contact'
    }
    return render(request, 'addressbook/add_contact.html', context=context)