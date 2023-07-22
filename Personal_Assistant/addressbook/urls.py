from django.urls import path
from .views import index, create_contact


urlpatterns = [
    path('', index, name='home'),
    path('add/', create_contact, name='add_contact'),
]