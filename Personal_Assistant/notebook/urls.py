from django.urls import path

from .views import AddNote


urlpatterns = [
    path('add', AddNote.as_view(), name='add_note')
]