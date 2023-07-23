from django.urls import path
from .views import ContactsHome, create_contact, AddContact


urlpatterns = [
    path('', ContactsHome.as_view(), name='home'),
    path('add/', AddContact.as_view(), name='add_contact'),
]