from django.urls import path
from .views import ContactsHome, create_contact


urlpatterns = [
    path('', ContactsHome.as_view(), name='home'),
    path('add/', create_contact, name='add_contact'),
]