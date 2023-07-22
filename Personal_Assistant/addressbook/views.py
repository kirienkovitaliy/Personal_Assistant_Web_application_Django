from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Contact
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'addressbook/index.html')


class ContactsHome(ListView):
    model = Contact
    template_name = 'addressbook/index.html'


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