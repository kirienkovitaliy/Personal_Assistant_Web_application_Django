from django.urls import path

from .views import ContactsHome, AddContact, EditContact, DeleteContact

app_name = "addressbook"

urlpatterns = [
    path("", ContactsHome.as_view(), name="home"),
    path("add/", AddContact.as_view(), name="add_contact"),
    path("edit/<int:pk>", EditContact.as_view(), name="edit_contact"),
    path("delete/<int:pk>", DeleteContact.as_view(), name="delete_contact"),
]
