from typing import Any

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
        return Contact.objects.all()


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